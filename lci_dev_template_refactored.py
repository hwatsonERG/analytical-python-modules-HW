# -*- coding: utf-8 -*-

"""
LCI DEVELOPMENT TEMPLATE

Author: Harrison Watson

Purpose
-------
Template for developing life cycle inventory datasets and exporting
openLCA-compatible JSON objects.

Design Philosophy
-----------------
Keep all major dataframe transformations visible.

The core pipeline remains linear so intermediate dataframe states
can be inspected during development and debugging.

Only repeated utility operations are wrapped in functions.



checklist: 
    1. import packages
    2. establish project path and pull in raw data
    3. create olca schema functions (df_olca)
    4. index alignment and string cleaning
    5. inputs and reference to false (for raw pollutant data)
    6. standardize process names
    7. uuids
    8. elementary flow map 
    9. technosphere flow map (with or without providers)
    10. create reference flows
    11. assign flow types 
    12. assign location and context
    13. link internal providers (e.g. unit processes within the dataset, not from the commons)
    14. create and assign parameters 
    15. validate exchanges
    16. build metadata objects according to flcac guidelines
        -- important for commons data, not strictly necessary for all data development tasks
    17. build process dict 
    18. write to a folder 
    19. optional unzip 
"""

# %% Imports

from pathlib import Path
import pandas as pd
import numpy as np
import copy
import yaml
import zipfile

from esupy.util import make_uuid

from flcac_utils.generate_processes import (
    build_flow_dict,
    build_process_dict,
    write_objects,
    validate_exchange_data
)

# %% Project Setup

PATH_PROJECT = Path(__file__).parent
INPUT_PATH = PATH_PROJECT / "inputs"
OUTPUT_PATH = PATH_PROJECT / "output"

#%% Utility Functions

def nan_check(df):
    print("\nMissing Value Report")
    for col in df.columns:
        count = df[col].isna().sum()
        if count > 0:
            print(f"{col}: {count}")


def split_by_nan(df, column):
    present = df[df[column].notna()]
    missing = df[df[column].isna()]
    return present, missing


def check_dups(df, process_col, flow_col):
    temp = (
        df[process_col].astype(str)
        + "__"
        + df[flow_col].astype(str)
    )
    return temp.value_counts()


def print_shape(df, label):
    print(f"\n{label}")
    print(df.shape)

#%% Data Import

df_raw = pd.read_csv(INPUT_PATH / "inventory.csv")
print_shape(df_raw, "Raw Import")

#%% Create Schema

SCHEMA_COLUMNS = [
    "ProcessID",
    "ProcessCategory",
    "ProcessName",
    "FlowUUID",
    "FlowName",
    "Context",
    "IsInput",
    "FlowType",
    "reference",
    "default_provider",
    "default_provider_name",
    "amount",
    "amountFormula",
    "unit",
    "avoided_product",
    "exchange_dqi",
    "location"
]

df_olca = df_raw.copy()

for col in SCHEMA_COLUMNS:
    if col not in df_olca.columns:
        df_olca[col] = ""

#%% Alignment and Cleaning

df_olca.columns = df_olca.columns.str.strip()

for col in df_olca.select_dtypes(include="object"):
    df_olca[col] = df_olca[col].str.strip()

df_olca = df_olca.reset_index(drop=True)

nan_check(df_olca)

#%% Default Exchange Flags

df_olca["IsInput"] = False
df_olca["reference"] = False
df_olca["avoided_product"] = False

#%% Process Naming

name_map = {
    # 'original': 'standardized'
}

#Example:
df_olca['ProcessName'] = df_olca['SourceProcess'].replace(name_map, regex=True)

#%% UUID Generation
'''
generally, make new uuids based on ProcessName
sometimes ProcessName matches FlowName, so we must pass multiple arguments into make_uuid to get truly unique IDs 
identical strings will yield identical uuids 

'''

if 'ProcessName' in df_olca.columns:
    df_olca['ProcessID'] = df_olca['ProcessName'].apply(make_uuid)

#%% Elementary Flow Mapping


flow_map = pd.read_csv(INPUT_PATH / 'elementary_flow_map.csv')
df_olca = df_olca.merge(...)

#%% bringing in  data provider flows/ technosphere flows 

'''
if pulling data providers from uslci, we need to do an api call to avoid overwriting 
flow level properties in the new dataset. 

prepare_tech_flow_mappings() takes in a csv with these columns:
 [SourceFlowName,SourceFlowUUID,SourceFlowContext,SourceUnit,MatchCondition,
  ConversionFactor, TargetRepoName, TargetFlowName, TargetUnit, Provider, Bridge, BridgeFlowName]

otherwise, pull in tehcnosphere flows in the same manner as elementary flows.
'''
from flcac_utils.mapping import prepare_tech_flow_mappings

techno_df = pd.read_csv(INPUT_PATH / 'technosphere_flow_map.csv') 

fuel_dict, flow_objs, provider_dict = prepare_tech_flow_mappings(techno_df)

from flcac_utils.mapping import apply_tech_flow_mapping

df_olca = apply_tech_flow_mapping(df_olca.rename(columns={'FlowName':'name'}),
                                  fuel_dict, flow_objs, provider_dict)

#%% Reference Flows


#working example for programmatically creating the reference flow for multiple unique processes
new_rows = []

unique_process = df_olca['ProcessName'].unique()

process_id_map = (
    df_olca[['ProcessName', 'ProcessID']]
    .drop_duplicates()
    .set_index('ProcessName')['ProcessID']
)

for process in unique_process:
    # Get process uuid and name for each new ref flow
    processID = process_id_map.loc[process]
    processName = df_olca[df_olca['ProcessName'] == process]['ProcessName'].iloc[0]
    
    # Create FlowName by modifying the string
    flowName = '----'
    
    #prevent overwriting flow uuids
    for key in new_rows:
            if key['FlowName'] == flowName:
                flowUUID = key['FlowUUID']
                break
    else:
        flowUUID = make_uuid([flowName, processName, processID])
        
        new_row = {
            'ProcessName': process,
            'ProcessID': processID,
            'FlowName': flowName,
            'FlowUUID': flowUUID,
            'IsInput': False,
            'reference': True,
            'amount': 1.0,
            'unit': 'kg',
            #'default_provider': 'nan',
            #'default_provider_name': 'nan'
                                            }
        #put new_row into new_rows
        new_rows.append(new_row)

reflows_df = pd.DataFrame(new_rows)

# Append to original DataFrame
df_olca = pd.concat([df_olca, reflows_df], ignore_index=True)

#%% Flow Types

# assign PRODUCT_FLOW vs ELEMENTARY_FLOW-- sets ref flows to product, all else to elementary 
# other useful methods would be to .apply() based on IsInput, or mask and assign with .loc[mask, ...] 
df_olca['FlowType'] = df_olca['reference'].apply(
    lambda x: 'PRODUCT_FLOW' if x else 'ELEMENTARY_FLOW'
)


#%% Metadata Assignment

# location
df_olca['location'] = 'US'

# context and category-- if all go to same folder, just assign df['context'] = ''
#for more complex assignment, do keyword based assignments 
category_key = {
    'keyword' : 'context 1',
    'keyword2' : 'context2',
    }

pattern = r'(' + '|'.join(category_key.keys()) + r')'
matches = (
    df_olca['ProcessName']
    .str.lower()
    .str.extract(pattern, expand=False)
)

df_olca['ProcessCategory'] = matches.map(category_key).fillna('-----')
df_olca['Context'] = '-------' 


# year
df_olca['Year'] = 2026

#avoided product
df_olca['avoided_product'] = False

#%% Internal Provider Assignment

# provider logic
def assign_providers(df):
    """
    Generic template for assigning default providers.

    Pattern:
        1. Identify provider processes
        2. Extract provider IDs
        3. Identify target exchanges
        4. Assign provider IDs to exchanges
    """

    provider_map = {
        "Provider A": (
            df["reference"]
            & df["ProcessName"].str.contains("provider a", case=False)
        ),
        "Provider B": (
            df["reference"]
            & df["ProcessName"].str.contains("provider b", case=False)
        ),
    }

    target_map = {
        "Provider A": (
            df["IsInput"]
            & df["FlowName"].str.contains("input a", case=False)
        ),
        "Provider B": (
            df["IsInput"]
            & df["FlowName"].str.contains("input b", case=False)
        ),
    }

    for provider, provider_mask in provider_map.items():

        provider_id = (
            df.loc[provider_mask, "ProcessID"]
            .iloc[0]
        )

        df.loc[
            target_map[provider],
            "default_provider"
        ] = provider_id

    return df


#assigning diff providers to duplicate exchanges (e.g. Diesel from 2 upstream data sets)
def assign_providers_sequentially(df):

    provider_ids = (
        df.loc[
            df["reference"],
            "ProcessID"
        ]
        .drop_duplicates()
        .tolist()
    )

    target_mask = (
        df["IsInput"]
        & df["FlowName"].str.contains(
            "target flow",
            case=False
        )
    )

    temp = df.loc[target_mask].copy()

    temp["default_provider"] = (
        temp.groupby("ProcessName")
        .cumcount()
        .map(
            lambda i:
            provider_ids[i]
            if i < len(provider_ids)
            else None
        )
    )

    df.loc[
        temp.index,
        "default_provider"
    ] = temp["default_provider"]

    return df
#%% Parameters

df_params = pd.read_csv(PATH_PROJECT / 'params.csv')
# parameter logic
params_edit = pd.DataFrame()

#creates the df that we feed to populate the parameters tab
for process in unique_process:

    process_name = process.lower().strip()

    mask = (
        df_params["EquipmentType"]
        .str.lower()
        .str.strip()
        .apply(lambda x: x in process_name)
    )

    matches = (
        df_params.loc[mask]
        .drop(columns="EquipmentType")
        .copy()
    )

    matches["processName"] = process

    params_edit = pd.concat(
        [params_edit, matches],
        ignore_index=True
    )
    
 
#exchange level parameter assignments 
keywords = {
    "emissions": [
        "Flow A",
        "Flow B",
        "Flow C"
    ]
}

parameter_name = "emission_factor"

def assign_formula(
        df,
        flow_list,
        parameter_name):

    mask = (
        df["FlowName"]
        .isin(flow_list)
    )

    df.loc[
        mask,
        "amountFormula"
    ] = (
        parameter_name
        + "*"
        + df.loc[mask, "amount"].astype(str)
    )

    return df

   
#%% Validation

# validate_exchange_data(df_olca)
flows, new_flows = build_flow_dict(df_olca)

nan_check(df_olca)

#%% build process dict 

id_to_name = df_olca.set_index("ProcessName")["ProcessID"].to_dict()
processes = {}

for process_name in id_to_name.keys():

    # Filter rows where 'ProcessName' matches 'process_name'
    filtered_df = df_olca[df_olca['ProcessName'] == process_name]
    p_dict = build_process_dict(
        filtered_df,
        flows,
        meta={},
        location_objs = {},
        source_objs={},
        actor_objs={},
        dq_objs={}, df_params=params_edit
    )
    processes.update(p_dict)

#%% Export

write_objects('----', flows, new_flows, processes,
              location_objs, dq_objs, source_objs, actor_objs,
              out_path = OUTPUT_PATH
              )


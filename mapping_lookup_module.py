"""
Python Workbook Module: Mapping and Lookup Workflows
Author: Harrison Watson

Purpose:
Build intuition for mapping, merging, and relationship validation.
"""

import pandas as pd

# ==========================================
# SECTION 1: MAP BASICS
# ==========================================

def exercise_1_map():
    df = pd.DataFrame({"flow":["CO2","CH4","N2O"]})
    mapping = {"CO2":"Carbon","CH4":"Methane", "N20" : "Nitrogen"}
    df["category"] = df["flow"].map(mapping)
    print(df)

# ==========================================
# SECTION 2: MISSING MAPS
# ==========================================

def exercise_2_missing_maps():
    df = pd.DataFrame({"material":["Steel","Plastic"]})
    mapping = {"Steel":"Metal"}
    print(df["material"].map(mapping))

# ==========================================
# SECTION 3: SIMPLE MERGE
# ==========================================

def exercise_3_merge():
    left = pd.DataFrame({"fuel":["Diesel","Gasoline"]})
    right = pd.DataFrame({"fuel":["Diesel","Gasoline"],"factor":[2.7,2.3]})
    print(left.merge(right,on='fuel'))

# ==========================================
# SECTION 4: LEFT JOIN BEHAVIOR
# ==========================================

def exercise_4_left_join():
    activity = pd.DataFrame({"fuel":["Diesel","Coal"]})
    factors = pd.DataFrame({"fuel":["Diesel"],"ef":[2.7]})
    print(activity.merge(factors,on='fuel',how='left'))
# %%


# ==========================================
# SECTION 5: COMPLETE THE ANALYSIS
# ==========================================

def exercise_5_analysis():
    activity = pd.DataFrame({"fuel":["Diesel","Gasoline","Natural Gas","Coal"],"amount":[100,150,200,50]})
    factors = pd.DataFrame({"fuel":["Diesel","Gasoline","Natural Gas"],"ef":[2.7,2.3,1.9]})
    # Merge factors
    # Calculate emissions
    # Identify missing factors

# %%


# ==========================================
# SECTION 6: JOIN VALIDATION
# ==========================================

def exercise_6_validation():
    print("--- Exercise 6: Validation ---")

    emissions = pd.DataFrame({
        "facility": ["A", "A", "B", "B", "C"],
        "emissions": [10, 20, 30, 40, 50]
    })

    facility_info = pd.DataFrame({
        "facility": ["A", "B", "B", "C"],
        "region": ["East", "West", "Western", "Central"]
    })

    # TASK 1:
    # Merge with validate='many_to_one'
    
    # TASK 2:
    # If the merge fails, determine which facility
    # appears more than once in facility_info.
    
    print(emissions)
    print(facility_info)
    
# %%


def mini_project():
    print("--- Mini Project: Classified Emissions Inventory ---")

    emissions = pd.DataFrame({
        "facility": ["A", "A", "B", "B", "C", "C"],
        "source": ["Boiler", "Fleet", "Boiler", "Process", "Fleet", "Process"],
        "emissions": [50, 20, 40, 60, 15, 35]
    })

    source_lookup = pd.DataFrame({
        "source": ["Boiler", "Fleet", "Process"],
        "scope": ["Scope 1", "Scope 1", "Scope 1"]
    })

    print(emissions)
    print(source_lookup)
    
    # Create a new dataframe called inventory:
    # Use validate='many_to_one'
    
    
    #groupby analysis challenge:
    # Create facility_total
    # Create percent_of_facility_emissions

    #summary table challenge:
    # One row per facility
    # Include:
    # total_emissions
    # average_source_emissions
    # source_count

# %%


if __name__ == '__main__':
    exercise_1_map()
    exercise_2_missing_maps()
    exercise_3_merge()
    exercise_4_left_join()
    exercise_5_analysis()
    exercise_6_validation()
    mini_project()

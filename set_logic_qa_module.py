"""
Python Workbook Module: Set Logic for Data Validation
Author: Harrison Watson

Purpose:
Develop intuition for using set operations to validate data integrity,
test assumptions, and diagnose risky transformations in LCA workflows.
"""

import pandas as pd

# %%

# ==========================================
# SECTION 1: BASIC SET COMPARISONS
# ==========================================

def exercise_1_missing_keys():
    print("--- Exercise 1: Missing Keys ---")
    df = pd.DataFrame({"flow": ["CO2", "CH4", "N2O"]})
    mapping = pd.DataFrame({"flow": ["CO2", "CH4"]})

    df_set = set(df["flow"])
    map_set = set(mapping["flow"])

    # TODO: Identify missing keys
    missing = df_set - map_set
    print("Missing flows:", missing)

# %%
# ==========================================
# SECTION 2: EXTRA / UNEXPECTED VALUES
# ==========================================

def exercise_2_extra_keys():
    print("--- Exercise 2: Extra Keys ---")
    df = pd.DataFrame({"flow": ["CO2", "CH4"]})
    mapping = pd.DataFrame({"flow": ["CO2", "CH4", "SF6"]})

    df_set = set(df["flow"])
    map_set = set(mapping["flow"])

    extra = map_set - df_set
    print("Unused mapping entries:", extra)

# %%
# ==========================================
# SECTION 3: COMPLETE COVERAGE CHECK
# ==========================================

def exercise_3_coverage():
    print("--- Exercise 3: Coverage ---")
    df = pd.DataFrame({"flow": ["CO2", "CH4", "N2Os"]})
    mapping = pd.DataFrame({"flow": ["CO2", "CH4", "N2O"]})

    df_set = set(df["flow"])
    map_set = set(mapping["flow"])

    # TODO: Confirm full coverage
    assert df_set.issubset(map_set), "Not all flows are mapped"
    print("All flows are mapped")

# %%
# ==========================================
# SECTION 4: VALIDATING MERGE IMPACT
# ==========================================

def exercise_4_merge_diagnostics():
    print("--- Exercise 4: Merge Diagnostics ---")
    df = pd.DataFrame({"flow": ["CO2", "CH4", "N2O"]})
    mapping = pd.DataFrame({
        "flow": ["CO2", "CH4"],
        "factor": [1, 25]
    })

    before_set = set(df["flow"])

    merged = df.merge(mapping, on="flow", how="left")

    after_set = set(merged["flow"])

    # TODO: Check if any rows lost or changed
    assert before_set == after_set, "Flow values changed during merge"

    missing = merged[merged["factor"].isna()]["flow"]
    print("Unmapped after merge:", set(missing))

# %%
# ==========================================
# SECTION 5: DUPLICATE KEY DIAGNOSTICS
# ==========================================

def exercise_5_duplicate_keys():
    print("--- Exercise 5: Duplicate Keys ---")
    mapping = pd.DataFrame({
        "flow": ["CO2", "CO2", "CH4"],
        "factor": [1, 1, 25]
    })

    key_counts = mapping["flow"].value_counts()
    duplicates = key_counts[key_counts > 1]

    print("Duplicate keys:", duplicates)

    # TODO: Convert to set for quick inspection
    dup_set = set(duplicates.index)
    print("Duplicate key set:", dup_set)

# %%

# ==========================================
# SECTION 6: SET-BASED PIPELINE QA MINI-PROJECT
# ==========================================

def set_based_qa(df, mapping):
    print("--- Set-Based QA ---")

    df_set = set(df["flow"])
    map_set = set(mapping["flow"])

    print("Total unique flows in data:", len(df_set))
    print("Total unique flows in mapping:", len(map_set))

    missing = df_set - map_set
    extra = map_set - df_set

    print("Missing mappings:", missing)
    print("Unused mappings:", extra)

    assert len(missing) == 0, "There are unmapped flows"

# %%
# ==========================================
# RUN ALL
# ==========================================

if __name__ == "__main__":
    exercise_1_missing_keys()
    exercise_2_extra_keys()
    exercise_3_coverage()
    exercise_4_merge_diagnostics()
    exercise_5_duplicate_keys()

    df_example = pd.DataFrame({"flow": ["CO2", "CH4"]})
    mapping_example = pd.DataFrame({"flow": ["CO2", "CH4", "N2O"]})

    set_based_qa(df_example, mapping_example)

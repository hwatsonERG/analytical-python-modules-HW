"""
Python Workbook: LCA-Focused Skills Training
Author: Harrison Watson

Instructions:
- Work through exercises in order.
- Predict outputs before running.
- Fill in TODO sections.
- Use print statements and assertions to validate results.

I recommend getting out scrap paper and hand-drawing the dataframes before predicting outputs.
"""
import pandas as pd
# %%


# ==========================================
# SECTION 1: DATA STRUCTURE & ALIGNMENT
# ==========================================

def exercise_1_alignment():
    print("--- Exercise 1: Alignment ---")
    df = pd.DataFrame({"A": [1, 2, 3]}, index=["x", "y", "z"])
    s = pd.Series([10, 20, 30], index=["x", "z", "y"])
    
    # TODO: Predict result before running
    df["B"] = s
    print(df)
    
# %%

def exercise_2_copy_vs_view():
    print("--- Exercise 2: Copy vs View ---")
    df = pd.DataFrame({"A": [1, 2, 3]})
    subset = df[df["A"] > 1]
    
    # TODO: Does this modify original df?
    subset["A"] = 100
    print("Subset:", subset)
    print("Original:", df)

# %%


# ==========================================
# SECTION 2: GROUP OPERATIONS
# ==========================================

def exercise_3_groupby():
    print("--- Exercise 3: Groupby ---")
    df = pd.DataFrame({
        "facility": ["A", "A", "B", "B"],
        "emissions": [10, 20, 30, 40]
    })

    # TODO: Compute total per facility
    result = df.groupby("facility")["emissions"].transform("sum")
    print(result)

# %%


def exercise_4_normalization():
    print("--- Exercise 4: Normalization ---")
    df = pd.DataFrame({
        "group": ["x", "x", "y"],
        "value": [10, 30, 60]
    })

    # TODO: Normalize within group
    df["share"] = df["value"] / df.groupby("group")["value"].transform("sum")
    print(df)

# %%


# ==========================================
# SECTION 3: LOOKUPS & MERGING
# ==========================================

def exercise_5_merges():
    print("--- Exercise 5: Merge ---")
    flows = pd.DataFrame({"flow": ["CO2", "CH4"]})
    factors = pd.DataFrame({
        "flow": ["CO2", "CH4"],
        "factor": [1, 25]
    })

    merged = flows.merge(factors, on="flow", how="left")
    print(merged)

    # TODO: Add assertion for no missing factors
    assert merged["factor"].notna().all(), "Missing factors detected"

# %%


# ==========================================
# SECTION 4: BOOLEAN LOGIC
# ==========================================

def exercise_6_masks():
    print("--- Exercise 6: Boolean Masks ---")
    df = pd.DataFrame({
        "flow": ["CO2 air", "CO2 water", "CH4 air"]
    })

    is_air = df["flow"].str.contains("air")
    is_co2 = df["flow"].str.contains("CO2")

    mask = is_air & is_co2
    print(df[is_air])
    print(df[is_co2])
    print(df[mask])

# %%


# ==========================================
# SECTION 5: PIPELINES
# ==========================================

def load_data():
    return pd.DataFrame({
        "flow": ["CO2", "CH4"],
        "value": [100, 50]
    })


def clean_data(df):
    df = df.copy()
    df["flow"] = df["flow"].str.strip().str.upper()
    return df


def transform_data(df):
    df = df.copy()
    df["scaled"] = df["value"] * 2
    return df


def validate_data(df):
    assert (df["value"] >= 0).all(), "Negative values detected"
    return True


def pipeline_demo():
    print("--- Pipeline Demo ---")
    df = load_data()
    df = clean_data(df)
    df = transform_data(df)
    validate_data(df)
    print(df)

# %%


# ==========================================
# SECTION 6: QA CHECKER MINI-PROJECT
# ==========================================

def qa_checker(df):
    print("--- QA CHECKER ---")
    print("Row count:", len(df))
    print("Nulls:", df.isnull().sum())
    print("Duplicates:", df.duplicated().sum())

# %%


# ==========================================
# RUN ALL
# ==========================================

if __name__ == "__main__":
    exercise_1_alignment()
    exercise_2_copy_vs_view()
    exercise_3_groupby()
    exercise_4_normalization()
    exercise_5_merges()
    exercise_6_masks()
    pipeline_demo()

    df_example = pd.DataFrame({"a": [1, 2, 2], "b": [3, None, 3]})
    qa_checker(df_example)

"""
Python Workbook Module: Groupby, Transform, and Aggregation
Author: Harrison Watson

Purpose:
Build intuition for grouped calculations before applying them
in analytical workflows.
"""

import pandas as pd

# ==========================================
# SECTION 1: GROUPBY BASICS
# ==========================================

def exercise_1_groupby_sum():
    print("--- Exercise 1: Groupby Sum ---")
    df = pd.DataFrame({"facility":["A","A","B"],"value":[10,20,30]})
    result = df.groupby("facility")["value"].sum()
    print(result)
    # Predict the output before running.

# ==========================================
# SECTION 2: AGGREGATION
# ==========================================

def exercise_2_aggregation():
    print("--- Exercise 2: Aggregation ---")
    df = pd.DataFrame({"facility":["A","A","B"],"value":[10,20,30]})
    result = df.groupby("facility").agg(total=("value","sum"),avg=("value","mean"))
    print(result)

# ==========================================
# SECTION 3: TRANSFORM
# ==========================================

def exercise_3_transform():
    print("--- Exercise 3: Transform ---")
    df = pd.DataFrame({"facility":["A","A","B"],"value":[10,20,30]})
    result = df.groupby("facility")["value"].transform("sum")
    print(result)

# ==========================================
# SECTION 4: AGG VS TRANSFORM
# ==========================================

def exercise_4_compare():
    print("--- Exercise 4: Compare ---")
    df = pd.DataFrame({"group":["A","A","B"],"value":[10,20,30]})
    print(df.groupby("group")["value"].sum())
    print(df.groupby("group")["value"].transform("sum"))

# ==========================================
# SECTION 5: COMPLETE THE ANALYSIS
# ==========================================

def exercise_5_analysis():
    print("--- Exercise 5: Analysis ---")
    df = pd.DataFrame({"facility":["A","A","A","B","B"],"emissions":[10,15,25,8,12]})
    # TASK 1 Create facility_total
    df['facility_total'] = df.groupby('facility')['emissions'].transform('sum')
    # TASK 2 Create facility_mean
    df['facility_mean'] = df.groupby('facility')['emissions'].transform('mean')
    # TASK 3 Create percentage_of_facility_total
    df['percent_total'] = df['emissions'] / df.groupby('facility')['emissions'].transform('sum')
    print(df)

# ==========================================
# SECTION 6: VALIDATION
# ==========================================

def exercise_6_validation():
    print("--- Exercise 6: Validation ---")

    emissions = pd.DataFrame({
        "facility": ["A", "A", "B", "B"],
        "emissions": [10, 20, 30, 40]
    })

    source_totals = pd.DataFrame({
        "facility": ["A", "B"],
        "reported_total": [30, 75]
    })

    calculated = (
        emissions
        .groupby("facility")["emissions"]
        .sum()
        .reset_index(name="calculated_total")
    )

    validation = calculated.merge(source_totals, on="facility")

    validation["matches"] = (
        validation["calculated_total"]
        == validation["reported_total"]
    )

    print(validation)
    
    
# ==========================================
# SECTION 7: MINI PROJECT
# ==========================================

def mini_project():
    print("--- Mini Project ---")
    # Build facility summary table with totals,
    # averages, highest emitters, and contributions.
  
# %%


if __name__ == "__main__":
    exercise_1_groupby_sum()
    exercise_2_aggregation()
    exercise_3_transform()
    exercise_4_compare()
    exercise_5_analysis()
    exercise_6_validation()
    mini_project()

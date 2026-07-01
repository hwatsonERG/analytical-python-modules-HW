"""
Python Workbook Module: Comprehensions & Vectorized Thinking
Author: Harrison Watson

Purpose:
Build fluency with list/dict comprehensions and lambda-based patterns
to replace clunky row-wise loops with concise, performant logic.

Focus:
- Translating loops → comprehensions
- Thinking in transformations (not iteration)
- Bridging to pandas vectorized patterns
"""

import pandas as pd

# %%
# ==========================================
# SECTION 1: LIST COMPREHENSIONS
# ==========================================

def exercise_1_basic_list():
    print("--- Exercise 1: List Comprehension ---")
    values = [1, 2, 3, 4]

    # TODO: Replace loop with comprehension
    result = [v * 2 for v in values]
    print(result)

# %%
# ==========================================
# SECTION 2: CONDITIONAL LOGIC
# ==========================================

def exercise_2_conditional():
    print("--- Exercise 2: Conditional Logic ---")
    values = [1, 2, 3, 4]

    # TODO: Keep only even values, multiply by 10
    result = [v * 10 for v in values if v % 2 == 0]
    print(result)

# %%
# ==========================================
# SECTION 3: DICT COMPREHENSIONS
# ==========================================

def exercise_3_dict():
    print("--- Exercise 3: Dict Comprehension ---")
    flows = ["CO2", "CH4"]

    # TODO: Create dictionary mapping flow → index
    result = {flow: i for i, flow in enumerate(flows)}
    print(result)

# %%
# ==========================================
# SECTION 4: LAMBDA FUNCTIONS (LIGHT USE)
# ==========================================

def exercise_4_lambda():
    print("--- Exercise 4: Lambda ---")
    values = [10, 20, 30]

    # TODO: Use lambda with map
    result = list(map(lambda x: x / 10, values))
    print(result)

# %%
# ==========================================
# SECTION 5: APPLY VS LOOP (PANDAS)
# ==========================================

def exercise_5_apply():
    print("--- Exercise 5: apply() ---")
    df = pd.DataFrame({"value": [10, 20, 30]})

    # TODO: Replace loop with apply
    df["scaled"] = df["value"].apply(lambda x: x * 3)
    print(df)

# %%
# ==========================================
# SECTION 6: VECTORIZED OPERATIONS (PREFERRED)
# ==========================================

def exercise_6_vectorized():
    print("--- Exercise 6: Vectorized ---")
    df = pd.DataFrame({"value": [10, 20, 30]})

    # BEST PRACTICE: avoid apply if possible
    df["scaled"] = df["value"] * 3
    print(df)

# %%
# ==========================================
# SECTION 7: FROM LOOP → PROFESSIONAL PATTERN
# ==========================================

def exercise_7_conversion():
    print("--- Exercise 7: Loop Conversion ---")
    df = pd.DataFrame({
        "flow": ["CO2", "CH4", "N2O"],
        "value": [100, 50, 25]
    })

    # OLD (clunky loop)
    result = []
    for v in df["value"]:
        result.append(v * 2)

    print("Loop result:", result)

    # TODO: Replace with vectorized version
    df["scaled"] = df["value"] * 2
    print("Vectorized:", df)

# %%
# ==========================================
# SECTION 8: MINI-PROJECT — CLEAN TRANSFORMATIONS
# ==========================================

def mini_project():
    print("--- Mini Project ---")

    df = pd.DataFrame({
        "flow": ["co2 ", " CH4", "n2o"],
        "value": [100, 50, 25]
    })

    # TODO 1: Clean strings (vectorized)
    df["flow_clean"] = df["flow"].str.strip().str.upper()

    # TODO 2: Scale values
    df["scaled"] = df["value"] * 2

    # TODO 3: Build mapping dict (flow → scaled value)
    mapping = {row["flow_clean"]: row["scaled"] for _, row in df.iterrows()}

    print(df)
    print("Mapping:", mapping)

# %%
# ==========================================
# RUN ALL
# ==========================================

if __name__ == "__main__":
    exercise_1_basic_list()
    exercise_2_conditional()
    exercise_3_dict()
    exercise_4_lambda()
    exercise_5_apply()
    exercise_6_vectorized()
    exercise_7_conversion()
    mini_project()

# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:22:07 2026

@author: HWatson

simple python pandas dataframe problems to work through
testing index alignment principles
groupby behavior 
etc
"""
# %%


import pandas as pd

s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([10, 20, 30], index=['b', 'c', 'd'])

print(s1 + s2)




# %%


df = pd.DataFrame({"A": [1, 2, 3]})

df["B"] = pd.Series([10, 20])

print(df)


# %%

df = pd.DataFrame({"A": [1, 2, 3]})

df["B"] = pd.Series([10, 20], index=[1, 2])
print(df)


# %%


df = pd.DataFrame({"A": [1, 2, 3]})

print(df + 100)


# %%


df = pd.DataFrame({
    "A": [1, 2],
    "B": [3, 4]
})

print(df + df.iloc[0])


# %%


df = pd.DataFrame({
    "A": [1, 2],
    "B": [3, 4]
})

s = pd.Series([10, 20])

print(df + s)


# %%
df = pd.DataFrame({
    "A": [1, 2],
    "B": [3, 4]
})
s = pd.Series([10, 20], index=["A", "B"])
print(df + s)


# %%


df = pd.DataFrame({
    "A": [1, 2, 3]
}, index=[10, 11, 12])

mask = pd.Series([True, False, True], index=[10, 11, 12])

print(df[mask])


# %%
mask = pd.Series([True, False, True], index=[0, 1, 2])
print(df[mask])


# %%
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([10, 20], index=[1, 2])

print(s1 + s2)


# %%

df1 = pd.DataFrame({"A": [1, 2]}, index=[0, 1])
df2 = pd.DataFrame({"A": [10, 20]}, index=[1, 2])

print(df1 + df2)


# %%


df = pd.DataFrame({"A": [1, 2, 3]})
print(df)

df.loc[[0, 1], "A"] = pd.Series([10, 20], index=[1, 2])

print(df)


# %%

df = pd.DataFrame({"A": [1, 2, 3]})
df.loc[[0, 1], "A"] = [10, 20]

print(df)


# %%

df1 = pd.DataFrame(
    {"A": [1, 2], "B": [3, 4]},
    index=[0, 1]
)
print(df1)

df2 = pd.DataFrame(
    {"B": [10, 20], "C": [30, 40]},
    index=[1, 2]
)
print(df2)

df3 = pd.Series([100, 200], index=["A", "C"])
print(df3)

print((df1 + df2) + df3)


# %%

df = pd.DataFrame({
    "group": ["a", "a", "b"],
    "value": [1, 2, 3]
}, index=[0, 1, 2])

print(df)


means = df.groupby("group")["value"].mean()

print(means)

df["centered"] = df["value"] - means

print(df)


# %%

index = pd.MultiIndex.from_tuples([
    ("A", 1), ("A", 2), ("B", 1)
])

print(index)

df = pd.DataFrame({"val": [10, 20, 30]}, index=index)

print(df)

s = pd.Series([100, 200], index=["A", "B"])

print(df + s)


# %%

df = pd.DataFrame({"A": [1, 2, 3]}, index=[0, 0, 1])

print(df)
s = pd.Series([10], index=[0])

print(df + s)


# %%

df = pd.DataFrame({"A": [1, 2, 3]})

df["A"] = df["A"] + pd.Series([0.5], index=[1])

print(df)


# %%

df = pd.DataFrame({"A": [10, 20, 30]}, index=[0, 1, 2])

mask = pd.Series([True, False], index=[1, 2])

df.loc[mask, "A"] = [100, 200]

df

# %%

df = pd.DataFrame({
    "A": [1, 2],
    "B": [3, 4]
}, index=[0, 1])

s = pd.Series([10, 20], index=[0, 1])

print(df.add(s, axis=1))


# %%

df = pd.DataFrame({"A": [1, 2, 3]}, index=[0, 1, 2])

s = pd.Series([10, 20], index=[1, 2])

df.loc[s.index, "A"] = s

print(df)


# %%

df = pd.DataFrame({
    "A": [1, 2],
    "B": [3, 4]
})

print(df)

result = df + pd.Series([10], index=["A"]) + 5

print(result)



# %%

df1 = pd.DataFrame({"A": [1, 2]}, index=[0, 1])
df2 = pd.DataFrame({"A": [10]}, index=[2])

print(df1 + df2)



# %%

s1 = pd.Series([1, 2], index=[0, 1])
s2 = pd.Series([10, 20], index=[1, 2])
s3 = pd.Series([100, 200], index=[2, 3])

print(s1 + s2 + s3)


# %%


df = pd.DataFrame({"A": [1, 2]})

df["B"] = pd.Series([10, 20], index=[1, 2])
df["C"] = df["A"] + df["B"]

print(df)



# %%


s1 = pd.Series([1, 2], index=[0, 1])
s2 = pd.Series([10, 20], index=[1, 2])
s3 = pd.Series([100, 200], index=[2, 3])

step1 = s1 + s2
final = step1 + s3

print(step1)
print(final)

# %%

df1 = pd.DataFrame({"A": [1, 2]}, index=[0, 1])
df2 = pd.DataFrame({"A": [10]}, index=[1])
s = pd.Series([100, 200], index=["A", "B"])

step1 = df1 + df2
final = step1 + s

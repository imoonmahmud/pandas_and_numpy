import pandas as pd
import numpy as np

# ------ Pandas Series -------
# Series: 1D array with a labeled index
s = pd.Series([10, 20, 30, 40, 50])
# 0    10
# 1    20
# dtype: int64


# Custom index
s_name = pd.Series(
    [85, 92, 78, 96],
    index = ['Math', 'Science', 'English', 'History'],
    name = 'Alice_scores')

print(s_name)
print(f"\nMath score: {s_name['Math']}")
print(f"Average score: {s_name.mean():.1f}")


# Series from dict
city_pop = pd.Series({
    'Chicago': 2.7,
    'NYC': 8.3,
    'LA': 3.9,
    'Houston': 2.3})

print(city_pop.sort_values(ascending=False))




# ---------- Pandas DataFrame ------------
# DataFrame:2D table - the primary Pandas structure

data = {
    'Employee': ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'Department': ['Engineering', 'Marketing', 'Engineering', 'Sales', 'HR'],
    'Salary': [85000, 62000, 91000, 55000, 58000],
    'Experience': [5, 3, 8, 2, 4],
    'Rating': [4.5, 3.8, 4.9, 3.5, 4.1]
}

df = pd.DataFrame(data)
print(df)
print("\nShape:", df.shape)
print("Cols:", list(df.columns))
print("Index:", list(df.index))

# DataFrame attributes
print(df.dtypes)
print(df.info())
print(df.describe())



# ---------- Accessing Data ------------
# Column access
print(df['Salary'])                      # Single column → Series
print(df[['Employee', 'Salary']])        # Multiple columns → DataFrame

# Row access
print(df.head(3))              # First 3 rows
print(df.tail(2))              # Last 2 rows
print(df.iloc[0])              # First row by position
print(df.loc[2])               # Row with index label 2

# Quick statistics
print(df['Salary'].mean())
print(df['Salary'].max())
print(df['Department'].value_counts())
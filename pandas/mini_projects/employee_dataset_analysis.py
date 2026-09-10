import pandas as pd
import numpy as np

employees = pd.DataFrame({
    'Name': ['Alice','Bob','Carol','David','Eve','Frank','Grace','Henry'],
    'Dept': ['Eng','Mkt','Eng','Sales','HR','Eng','Mkt','Sales'],
    'Salary': [85000, 62000, 91000, 55000, 58000, 78000, 67000, 49000],
    'Experience': [5, 3, 8, 2, 4, 6, 4, 1],
    'Rating': [4.5, 3.8, 4.9, 3.5, 4.1, 4.3, 4.0, 3.2]
})


print("=" * 50)
print("EMPLOYEE ANALYSIS REPORT")
print("=" * 50)

# Basic Info
print(f"\nTotal Employee: {len(employees)}")
print(f'Departments: {employees['Dept'].unique()}')

# Salary Analysis
print("\nSalary Statistics")
print(f"Average Salary: {employees['Salary'].mean():.0f}")
print(f"Highest: {employees['Salary'].max():,} ({employees.loc[employees['Salary'].idxmax(), 'Name']})")
print(f"Lowest: {employees['Salary'].min():,} ({employees.loc[employees['Salary'].idxmin(), 'Name']})")


# Department Summary
print("\nDepartment Summary:")
dept_summary = employees.groupby('Dept').agg(
    count = ('Name', 'count'),
    Avg_salary = ('Salary', 'mean'),
    Avg_rating = ('Rating', 'mean')
).round(2)
print(dept_summary)

# Top performers
print("\nTop Performers (Rating >= 4.3):")
top = employees[employees['Rating'] >= 4.3][['Name', 'Dept', 'Salary', 'Rating']]
print(top.to_string(index=False))

# Salary vs experience correlation
correlation = employees['Salary'].corr(employees['Experience'])
print(f"\nSalary-Experience Correlation: {correlation:.3f}")
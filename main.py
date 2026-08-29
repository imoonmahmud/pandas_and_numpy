import pandas as pd
import numpy as np

students = {
    'Name': ['Alice', 'Bob', 'Carol', 'David', 'Eve', 'Frank'],
    'Math': [92, 78, 85, 60, 95, 72],
    'Science': [88, 82, 90, 55, 97, 65],
    'English': [76, 88, 84, 70, 89, 80],
    'Grade': ['A', 'B', 'B', 'C', 'A', 'B']}

df = pd.DataFrame(students)
#print(f"\nShape: {df.shape}") # (6, 5) — 6 rows, 5 columns

# Statistical Summary with numpy
math_scores = np.array(df['Math'])

mean = np.mean(math_scores)
median = np.median(math_scores)
std = np.std(math_scores)
min = np.min(math_scores)
max = np.max(math_scores)

# Overall score
df['Total'] = df['Math'] + df['Science'] + df['English']
df['Average'] = round((df['Total'] / 3), 1)

# Rank students
df = df.sort_values('Average', ascending=False).reset_index(drop=True)
df.index = df.index + 1
df.index.name = 'Rank'

# Grade distribution
#print(df['Grade'].value_counts())

# Top performers
top_students = df[df['Average'] >= 85]
print(f"\nTop performers (avg >= 85): {list(top_students['Name'])}")
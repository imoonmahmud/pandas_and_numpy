import numpy as np
from prettytable import PrettyTable

# Student marks: 5 subjects, 6 students
marks = np.array([
    [85, 92, 78, 88, 91],  # Alice
    [72, 68, 75, 80, 70],  # Bob
    [95, 97, 92, 94, 96],  # Carol
    [60, 55, 62, 58, 65],  # David
    [88, 84, 90, 87, 85],  # Eve
    [76, 79, 73, 81, 77],  # Frank
])

names = np.array(['Alice', 'Bob', 'Carol', 'David', 'Eve', 'Frank'])
subjects = np.array(['Math', 'Science', 'English', 'History', 'CS'])

totals = np.sum(marks, axis=1)
averages = np.average(marks, axis=1)
ranks = np.argsort(averages)[::-1]

table1 = PrettyTable()
table1.field_names = ['Rank', 'Name', 'Total', 'Average', 'Grade']
for rank, idx in enumerate(ranks, 1):
    avg = averages[idx]
    grade = 'A+' if avg >= 90 else 'A' if avg >= 80 else 'B' if avg >= 70 else 'C'
    table1.add_row([
        rank,
        names[idx],
        totals[idx],
        avg,
        grade])
print(table1)

print("\nSubject Averages:")
table2 = PrettyTable()
table2.field_names = ['Subject', 'Average']
for subj, avg in zip(subjects, np.mean(marks, axis=0)):
    table2.add_row([subj, round(avg, 1)])
print(table2)

print(f"\nClass Top Score: {np.max(marks)}")
print(f"Class Low Score: {np.min(marks)}")
print(f"Pass rate (avg>=60): {np.mean(averages >= 60) * 100:.0f}%")
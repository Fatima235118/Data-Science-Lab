import numpy as np
import pandas as pd

# Task 1: NumPy Temperature

temperatures = np.array([28, 32, 35, 30, 27, 33, 31])

print("Celsius:", temperatures)
print("Shape:", temperatures.shape)
print("Data type:", temperatures.dtype)

fahrenheit = temperatures * 9 / 5 + 32

print("Fahrenheit:", fahrenheit)

print("Average:", round(np.mean(temperatures), 2))
print("Max:", np.max(temperatures))
print("Min:", np.min(temperatures))

above_30 = temperatures > 30

print("Above 30 C:", above_30)

# Task 2: Employee DataFrame

employees = {
    "Name": [
        "fatima", "Sara", "Ahmed", "sakina",
        "Hamza", "Zainab", "Ayesha", "Usman"
    ],
    "Department": [
        "IT", "HR", "IT", "IT",
        "HR", "Fin", "IT", "Fin"
    ],
    "Salary": [
        65000, 55000, 58000, 72000,
        58000, 61000, 70000, 52000
    ],
    "YearsExperience": [
        4, 3, 2, 6,
        5, 5, 7, 2
    ]
}
employee_df = pd.DataFrame(employees)
print("\nEmployee DataFrame:")
print(employee_df)
selected_rows = employee_df.loc[[2, 4], ["Name", "Salary"]]
print("\nSelected rows (loc):")
print(selected_rows)
first_four = employee_df.iloc[0:4, 0:2]
print("\nFirst 4 rows and first 2 columns (iloc):")
print(first_four)

high_earners = employee_df[employee_df["Salary"] > 60000]

print("\nHigh earners (Salary > 60000):")
print(high_earners)

it_experienced = employee_df[
    (employee_df["Department"] == "IT") &
    (employee_df["YearsExperience"] > 3)
]

print("\nIT staff with >3 years experience:")
print(it_experienced) 

# Task 3: Merge, GroupBy and Vectorized Operation

students = pd.DataFrame({
    "StudentID": [101, 102, 103, 104, 105, 106],
    "Name": ["Ali", "Sara", "Bilal", "Ayesha", "Hamza", "Zainab"],
    "Department": ["CS", "SE", "CS", "AI", "AI", "CS"]
})

cgpa_data = pd.DataFrame({
    "StudentID": [101, 102, 103, 104, 105, 106],
    "CGPA": [3.80, 3.20, 3.65, 3.45, 3.45, 3.70]
})

# (a) Merge DataFrames
merged = pd.merge(students, cgpa_data, on="StudentID")

print("\nMerged Data:")
print(merged)

# (b) Average CGPA per department
dept_avg = merged.groupby("Department")["CGPA"].mean()

print("\nAverage CGPA per Department:")
print(dept_avg)

# (c) Mean, max and count
dept_summary = merged.groupby("Department")["CGPA"].agg(
    ["mean", "max", "count"]
)

print("\nCGPA Summary per Department:")
print(dept_summary)

# (d) Scholarship or Regular
merged["Status"] = np.where(
    merged["CGPA"] >= 3.5,
    "Scholarship",
    "Regular"
)

print("\nMerged Data with Status:")
print(merged)
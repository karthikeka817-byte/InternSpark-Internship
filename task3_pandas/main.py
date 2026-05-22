import pandas as pd

# Read CSV file
data = pd.read_csv("students.csv")

print("\nStudent Records")
print(data)

# Average marks
average = data["Marks"].mean()

print("\nAverage Marks:", average)

# Top student
top_student = data.loc[data["Marks"].idxmax()]

print("\nTop Student")
print(top_student)

# Filter students with marks above 85
filtered = data[data["Marks"] > 85]

print("\nStudents Scoring Above 85")
print(filtered)
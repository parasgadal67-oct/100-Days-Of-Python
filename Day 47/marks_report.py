import pandas as pd
# load data
df = pd.read_csv("students.csv")
# Split into passed and failed
passed = df[df["Marks"] >=50]
failed = df[df["Marks"] <50]
# Finding Highest and Lowest 
highest = df["Marks"].max()
lowest = df["Marks"].min()
topper = df[df["Marks"]== highest]["Name"]
bottom = df[df["Marks"]== lowest]["Name"]
# Printing student report card
print("==== STUDENTS REPORT CARD ====")
print("Students:", len(df))
print(f"Average: {df["Marks"].mean():.2f}")
print(f"Highest: {highest} ({', '.join(topper)})")
print(f"Lowest: {lowest} ({', '.join(bottom)})")
print("Passed(>=50):",len(passed),"students")
print("Failed(<50):",', '.join(failed["Name"]))
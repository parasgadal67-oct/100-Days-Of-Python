import numpy as np
# The marks
marks = np.array([72, 85, 90, 48, 77, 50, 99, 65, 70])
# Calculate the marks
average = marks.mean()
highest = marks.max()
lowest = marks.min()
passed = (marks>=50).sum()
#Bonus marks
bonus = np.minimum(marks +5, 100)
# print th report
print("==== Class Marks Report ====")
print("Marks:", marks)
print(f"Average: {average:.2f}")
print("Highest:", highest)
print("Lowest:", lowest)
print("Passed(>=50):", passed, "students")
print("After +5 bonus:", bonus)
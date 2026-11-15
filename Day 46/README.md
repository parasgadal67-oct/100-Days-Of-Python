# Day 46 – Student Marks Statistics (NumPy)

A small app that uses NumPy to calculate class statistics from a list of student marks.

## What it does
- Shows all marks
- Calculates the average (2 decimal places), highest and lowest mark
- Counts how many students passed (50 or more)
- Adds a +5 bonus to every mark, capped at 100

## How to run
```
cd "Day 46"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python marks_stats.py
```

## Sample output
```
==== Class Marks Report ====
Marks: [72 85 90 48 77 50 99 65 70]
Average: 72.89
Highest: 99
Lowest: 48
Passed(>=50): 8 students
After +5 bonus: [ 77  90  95  53  82  55 100  70  75]
```

## What I learned
- `np.array()` creates a NumPy array from a list
- `.mean()`, `.max()`, `.min()` and `.sum()` give stats without writing loops
- Maths on an array works on every number at once (`marks + 5`)
- `marks >= 50` gives True/False for each mark, and `.sum()` counts the Trues (True = 1, False = 0)
- `np.minimum(marks + 5, 100)` caps marks at 100
- `:.2f` formats a number to 2 decimal places

## Planned upgrades
- Day 47–48: student names + load marks from a CSV file (Pandas)
- Day 49: bar chart of marks (Matplotlib)
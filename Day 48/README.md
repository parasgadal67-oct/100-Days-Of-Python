# Day 48 – Student Ranking (Pandas sorting)

Ranks students by marks from a CSV file and shows the top 3, with ties handled fairly.

## What it does
- Loads student names and marks from `students.csv`
- Sorts students from highest to lowest marks
- Gives each student a rank (students with the same marks share a rank)
- Shows the full ranking table without the index
- Shows the top 3 ranks, including tied students

## How to run
```
cd "Day 48"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python rank_students.py
```

## Sample output
```
==== CLASS REPORT ====
 Rank   Name  Marks
    1  Paras    100
    2  Ayush     99
    2  Rizan     99
    2 Subash     99
    5 Sharda     88
    6  Anmol     50
    7  Rahul     45
    8  Reeta     38
Top 3: Paras, Ayush, Rizan, Subash
```

## What I learned
- `sort_values("Marks", ascending=False)` – sorts rows from highest to lowest
- The index stays with each row after sorting, like a roll number
- `.rank(ascending=False, method="min")` – ties share the best rank, and the next student skips ahead (Rank = students with more marks + 1)
- `.astype(int)` – shows ranks as `1` instead of `1.0`
- `ranked[["Rank", "Name", "Marks"]]` – picks columns in a chosen order
- `.to_string(index=False)` – prints the table without the index

### Bug I found by testing
- `.head(3)` takes the first 3 **rows**, not the top 3 **ranks**
- With a 3-way tie at 99, Subash (rank 2) was left out of the top 3
- Fixed with filtering: `ranked[ranked["Rank"] <= 3]`

## Planned upgrades
- Day 49: bar chart of marks (Matplotlib)
- Day 58: student management system with SQLite
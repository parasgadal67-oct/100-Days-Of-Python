# Day 47 – Student Marks Report (Pandas)
## What it does
It shows the report of the students which were imported from the csv file called students.csv.
Inside the csv file it contains the data of students such as names and marks.
It is able to show the followings:
 - Highest marks.
 - Lowest marks.
 - Topper student.
 - Bottom student.
 - Passed and failed students.
 - Average marks.
## How to run
```
cd "Day 47"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python marks_report.py
```
## Sample output
```
==== STUDENTS REPORT CARD ====
Students: 8
Average: 73.88
Highest: 100 (Paras)
Lowest: 38 (Reeta)
Passed(>=50): 6 students
Failed(<50): Rahul, Reeta
```
## What I learned
- pd.read_csv = loads CSV file into a Dataframe(table).
- Data frame vs Series
  - DataFrame is the whole table and is the 2-Dimensional  structure.
  - Series is one column of the table, a 1-dimensional structure..
- Filtering:df[df["Marks"]>=50] = Keeps only the rows where the conditions is True.
- len()- counts the rows and ', '.join()-joins the names with comma and a space.
- Reading and fixing errors thoroughly like:
  - KeyError:"Names" instead of "Name"
  - TypeError:'>=' not supported between 'list' and 'int' wrote '>=50' without df
## Planned upgrades
- Day 48(sort/rank,top3)
- Day 49(bar chart)
- Day 58(student management with SQLite)
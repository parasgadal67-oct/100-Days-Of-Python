import pandas as pd
# Load the Data.
df = pd.read_csv("students.csv")
# Sort and rank
ranked = df.sort_values("Marks", ascending=False)
ranked["Rank"] = ranked["Marks"].rank(ascending=False, method="min").astype(int)
# Top 3
top_ranked = ranked[ranked["Rank"] <= 3]
# Print Report
print("==== CLASS REPORT ====")
print(ranked[["Rank", "Name", "Marks"]].to_string(index=False))
print("Top 3:", ", ".join(top_ranked["Name"]))


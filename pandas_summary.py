import pandas as pd

# 1️⃣ Read CSV file
df = pd.read_csv("sample.csv")

print("===== BASIC INFO =====")
print(df.info())

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== NUMERIC SUMMARY =====")
print(df.describe())

print("\n===== MEAN OF NUMERIC COLUMNS =====")
print(df.mean(numeric_only=True))

# Optional: Save summary to file
with open("summary_output.txt", "w") as f:
    f.write("Missing Values:\n")
    f.write(str(df.isnull().sum()))
    f.write("\n\nNumeric Summary:\n")
    f.write(str(df.describe()))

print("\nSummary saved to summary_output.txt")

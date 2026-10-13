import numpy as np
import pandas as pd

#-------------LOAD DATASET------------- 
df = pd.read_csv("students.csv")
df.columns = df.columns.str.strip()

df["Name"] = df["Name"].astype(str).str.strip().str.title()
df["Department"] = df["Department"].astype(str).str.strip().str.strip()

print("\n==== STUDENT DATASET =====")
print(df.to_string(index=False))

#------------CHECK AND ORGANIZE DATA------------
print("\n==== DATASET INFORMATION =====")
print(df.info())

print("\n==== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DATASET SHAPE =====")
print(df.shape)

print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())

#----------IDENTIFY SUBJECT COLUMNS----------
possible_subjects = [
    "Mathematics", "MAths", "Python", "Statistics", "Science", "English"
]
subject_columns = [
    col for col in possible_subjects if col in df.columns
]

if not subject_columns and "Subjectmarks" in df.columns:
    subject_columns = ["Subjectmarks"]

if not subject_columns:
    raise ValueError("No subject marks columns found in the dataset.")

for col in subject_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["Attendance"] = pd.to_numeric(
    df["Attendance"], errors="coerce"
)

df = df.dropna(
    subset=subject_columns + ["Attendance"]
).copy()

#----------CALCULATE TOTAL AND AVERAGE MARKS-----------
def calculate_total(marks):
    """Calculate total marks for a student."""
    return marks.sum()


def calculate_average(marks):
    """Calculate average marks for a student."""
    return marks.mean()


df["Total_Marks"] = df[subject_columns].sum(axis=1)
df["Average_Marks"] = df[subject_columns].mean(axis=1)

print("\n===== TOTAL AND AVERAGE MARKS =====")
print(
    df[
        ["Student ID", "Name", "Total_Marks", "Average_Marks"]
    ].to_string(index=False)
)

#----------CALCULATE PERCENTAGE-------------
MAX_MARKS_PER_SUBJECT = 10

total_possible_marks = (
    len(subject_columns) * MAX_MARKS_PER_SUBJECT
)

df["Percentage"] = (
    df["Total_Marks"] / total_possible_marks
) * 100

print("\n===== STUDENT PERCENTAGES =====")
print(
    df[["Student ID", "Name", "Percentage"]]
    .to_string(index=False)
)

#----------- ASSIGN GRADES USING A REUSABLE FUNCTION-----------
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


df["Grade"] = df["Percentage"].apply(calculate_grade)

print("\n===== STUDENT GRADES =====")
print(
    df[["Student ID", "Name", "Percentage", "Grade"]]
    .to_string(index=False)
)

#---------IDENTFY PASS AND FAIL STUDENTS----------
PASS_PERCENTAGE = 40

def check_result(row):
    """Check whether a student passes every subject."""

    for subject in subject_columns:
        subject_percentage = (
            row[subject] / MAX_MARKS_PER_SUBJECT
        ) * 100

        if subject_percentage < PASS_PERCENTAGE:
            return "Fail"

    return "Pass"


df["Result"] = df.apply(check_result, axis=1)

print("\n===== PASS / FAIL RESULTS =====")
print(
    df[["Student ID", "Name", "Result"]]
    .to_string(index=False)
)

passed = (df["Result"] == "Pass").sum()
failed = (df["Result"] == "Fail").sum()

print("\nTotal Passed:", passed)
print("Total Failed:", failed)

#-----------CHECK ATTENDANCE ELIGIBILITY------------
ATTENDANCE_LIMIT = 60

def check_attendance(attendance):
    if attendance >= ATTENDANCE_LIMIT:
        return "Eligible"
    else:
        return "Not Eligible"


df["Attendance_Status"] = df["Attendance"].apply(
    check_attendance
)

print("\n===== ATTENDANCE STATUS =====")
print(
    df[
        ["Student ID", "Name", "Attendance", "Attendance_Status"]
    ].to_string(index=False)
)
#-----------HIGHEST, LOWEST AND AVERAGE PERFORMANCE-------------
highest_marks = df["Average_Marks"].max()
lowest_marks = df["Average_Marks"].min()
average_marks = df["Average_Marks"].mean()

print("\n===== OVERALL PERFORMANCE =====")
print("Highest Average Marks:", round(highest_marks, 2))
print("Lowest Average Marks:", round(lowest_marks, 2))
print("Class Average Marks:", round(average_marks, 2))

top_student = df.loc[df["Average_Marks"].idxmax()]
lowest_student = df.loc[df["Average_Marks"].idxmin()]

print("\n===== TOP-PERFORMING STUDENT =====")
print("Name:", top_student["Name"])
print("Student ID:", top_student["Student ID"])
print("Average Marks:", round(top_student["Average_Marks"], 2))

print("\n===== LOWEST-PERFORMING STUDENT =====")
print("Name:", lowest_student["Name"])
print("Student ID:", lowest_student["Student ID"])
print("Average Marks:", round(lowest_student["Average_Marks"], 2))

#------------SUBJECT-WISE PERFORMANCE ANALYSIS------------
print("\n===== SUBJECT-WISE PERFORMANCE =====")

subject_analysis = []

for subject in subject_columns:
    subject_analysis.append({
        "Subject": subject,
        "Highest Marks": df[subject].max(),
        "Lowest Marks": df[subject].min(),
        "Average Marks": df[subject].mean()
    })

subject_analysis_df = pd.DataFrame(subject_analysis)

print(subject_analysis_df.round(2).to_string(index=False))

#-----------DEPARTMENT-WISE PERFORMANCE ANALYSIS----------
print("\n===== DEPARTMENT-WISE PERFORMANCE =====")

department_analysis = df.groupby("Department").agg(
    Total_Students=("Student ID", "count"),
    Average_Marks=("Average_Marks", "mean"),
    Highest_Marks=("Average_Marks", "max"),
    Lowest_Marks=("Average_Marks", "min"),
    Average_Attendance=("Attendance", "mean")
).round(2)

print(department_analysis)

best_department = department_analysis[
    "Average_Marks"
].idxmax()

print("\nBest Performing Department:", best_department)
print(
    "Department Average:",
    department_analysis.loc[best_department, "Average_Marks"]
)

#-----------RANK STUDENTS AND DISPLAY TOP FIVE------------
df["Rank"] = (
    df["Average_Marks"]
    .rank(method="dense", ascending=False)
    .astype(int)
)

ranked_students = df.sort_values(
    by=["Average_Marks", "Name"],
    ascending=[False, True]
)

print("\n===== TOP FIVE STUDENTS =====")
print(
    ranked_students[
        ["Rank", "Student ID", "Name",
         "Department", "Average_Marks", "Grade"]
    ].head(5).to_string(index=False)
)

#----------USE NUMPY FOR NUMERICAL CALCULATIONS------------

print("\n===== NUMPY STATISTICS =====")

marks_array = df["Average_Marks"].to_numpy()

print("Maximum Marks:", np.max(marks_array))
print("Minimum Marks:", np.min(marks_array))
print("Mean Marks:", round(np.mean(marks_array), 2))
print("Median Marks:", np.median(marks_array))
print("Standard Deviation:", round(np.std(marks_array), 2))



#-----------GENERATE COMPLETE STUDENT PERFORMANCE REPORT-------------
print("\n===== COMPLETE STUDENT PERFORMANCE REPORT =====")

report_columns = [
    "Student ID", "Name", "Department"
] + subject_columns + [
    "Total_Marks", "Average_Marks", "Percentage",
    "Grade", "Result", "Attendance",
    "Attendance_Status", "Rank"
]

print(df[report_columns].to_string(index=False))









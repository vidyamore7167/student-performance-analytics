# Student Performance Analytics Using Python

## 1. Project Overview

Student Performance Analytics is a Python-based project that analyzes student academic scores, department information, and attendance records using Pandas and NumPy.

The project processes student data, assigns grades, identifies pass/fail status, analyzes department-wise performance, and identifies top-performing students.

## 2. Objectives

- Analyze student academic performance.
- Calculate marks, averages, and percentage equivalents.
- Assign grades based on predefined grading criteria.
- Identify pass and fail students.
- Find the highest, lowest, and average scores.
- Perform department-wise performance analysis.
- Analyze student attendance.
- Generate a processed student performance report.

## 3. Technologies Used

- **Python** – Programming logic, functions, loops, and conditions.
- **Pandas** – Data cleaning, filtering, grouping, and analysis.
- **NumPy** – Numerical calculations and conditional operations.
- **CSV** – Input dataset format.
- **GitHub** – Source code management and project hosting.

## 4. Project Files

| File Name | Description |
|---|---|
| `main.py` | Python source code for student performance analysis |
| `students.csv` | Input dataset containing student records |
| `README.md` | Project description, instructions, and documentation |

The program may also generate `student_performance_report.csv` after execution.

## 5. Dataset Description

The dataset contains the following columns:

- **Student ID:** Unique student identifier.
- **Name:** Student name.
- **Department:** Student department, such as AIDS, COMP, IT, and AIML.
- **Subjectmarks:** Academic score on a 10-point scale.
- **Attendance:** Student attendance percentage.

## 6. Features

- Data preprocessing and column-name cleaning.
- Detection and removal of duplicate records.
- Calculation of score percentages.
- Grade assignment using conditional statements.
- Pass/fail classification.
- Highest, lowest, and average performance calculations.
- Department-wise average score analysis.
- Identification of top-performing students.
- Attendance eligibility analysis.
- Export of processed results to a CSV report.

## 7. Grading Criteria

| Marks out of 10 | Grade |
|---|---|
| 9.0–10.0 | A+ |
| 8.0–8.99 | A |
| 7.0–7.99 | B |
| 6.0–6.99 | C |
| 4.0–5.99 | D |
| Below 4.0 | F |

**Pass condition:** Marks greater than or equal to 4.0.

**Attendance condition:** Attendance greater than or equal to 60% is classified as eligible for this project's analysis.

These are project-defined thresholds and can be modified according to institutional rules.

## 8. How to Run the Project

### Step 1: Install Python

Install Python on your computer if it is not already installed.

### Step 2: Install the required libraries

Open a terminal and run:

```bash
pip install pandas numpy
```

### Step 3: Download the project files

Download or clone this repository and keep `main.py` and `students.csv` in the same folder.

### Step 4: Run the program

```bash
python main.py
```

### Step 5: View the results

The program displays the analysis results in the terminal. If report-export functionality is included in the code, it also saves the processed data as a CSV file.

## 9. Analysis Performed

The project can answer questions such as:

1. Who is the highest-performing student?
2. Who has the lowest score?
3. What is the overall average score?
4. Which department has the highest average score?
5. How many students passed or failed?
6. Which students have attendance below 60%?
7. Who are the top five students?

Actual numerical results depend on the dataset used when running the program.

## 10. Limitations

The current dataset contains a single academic score column, `Subjectmarks`. Therefore, the project performs score-based and department-wise analysis rather than comparing individual subjects such as Mathematics, Science, or English.

## 11. Future Enhancements

- Add individual subject marks.
- Create performance charts and graphs.
- Develop an interactive dashboard.
- Generate downloadable PDF reports.
- Analyze performance trends over time.

## 12. Conclusion

This project demonstrates how Python, Pandas, and NumPy can be used to preprocess student records and analyze academic performance and attendance. It provides practical experience in data analysis, conditional statements, functions, and data manipulation.

## 13. Author

**Name:** [Your Name]  
**Department:** [Your Department]

## 14. GitHub Repository

[Student Performance Analytics Repository](https://github.com/vidyamore7167/student-performance-analytics)

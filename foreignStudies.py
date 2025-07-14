## IMPORT MODULES
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

## LOAD DATASET
df = pd.read_csv('/Users/sahana/Desktop/global_student_migration.csv')
## VISUALIZE DATA

# top countries students are migrating from
country_counts = df['origin_country'].value_counts().head(3)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=country_counts.values, y=country_counts.index, palette='viridis', ax=ax)
ax.set_title("Top 3 Countries Students Are Migrating From")
ax.set_xlabel("Number of Students")
ax.set_ylabel("Origin Country")
st.pyplot(fig)

# top countries students are migrating to
country_counts = df['destination_country'].value_counts().head(3)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=country_counts.values, y=country_counts.index, palette='viridis', ax=ax)
ax.set_title("Top 3 Countries Students Are Migrating To")
ax.set_xlabel("Number of Students")
ax.set_ylabel("Destination Country")
st.pyplot(fig)

# top reasons students are migrating
reason_counts = df['enrollment_reason'].value_counts().head(3)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=reason_counts.values, y=reason_counts.index, palette='viridis', ax=ax)
ax.set_title("Top 3 Reasons Why Students Are Migrating")
ax.set_ylabel("Number of Students")
ax.set_xlabel("Reason")
st.pyplot(fig)

# top field of studies
field_counts = df['field_of_study'].value_counts().head(3)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=field_counts.values, y=field_counts.index, palette='viridis', ax=ax)
ax.set_title("Top 3 Fields of Study")
ax.set_ylabel("Number of Students")
ax.set_xlabel("Field of Study")
st.pyplot(fig)

# academic profiles
gifted_students = 0
for i in range(len(df)):
    row = df.iloc[i]
    if row['gpa_or_score'] >= 3.75 or row['scholarship_received'] == True or row['test_score'] >= 8.5:
        gifted_students += 1
average_students = len(df) - gifted_students
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=['Gifted Students', 'Average Students'], y=[gifted_students, average_students], palette='viridis', ax=ax)
ax.set_title("Academic Profiles of Students")
ax.set_ylabel("Number of Students")
ax.set_xlabel("Gifted or Not (Based on Scholarships, GPA, and Test Scores)")
st.pyplot(fig)

# starting salaries
bins = [0, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000,float('inf')]
labels = [
    '0–20k', '20k–40k', '40k–60k', '60k–80k', '80k–100k',
    '100k–120k', '120k-140k', '140k-160k', '160k+'
]
df['salary_range'] = pd.cut(df['starting_salary_usd'], bins=bins, labels=labels, include_lowest=True)
salary_counts = df['salary_range'].value_counts().sort_index()  # sort by bin order
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=salary_counts.index, y=salary_counts.values, palette='viridis', ax=ax)
ax.set_title("Starting Salary Distribution")
ax.set_xlabel("Salary Range (USD)")
ax.set_ylabel("Number of Students")
plt.xticks(rotation=45)
st.pyplot(fig)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Deep_cleaned_patient_data.csv")
print(df)

# %%
print(df.info)

# %%
print("Duplicates",df.duplicated().sum())
print("Rows:",df.shape[0],"Columns:",df.shape[1])
print(df.isnull().sum())

# %%
# Fill missing categorical lab test results with 'None'
df['max_glu_serum'].fillna('None', inplace=True)
df['A1Cresult'].fillna('None', inplace=True)
df[['max_glu_serum', 'A1Cresult']].isnull().sum()


# %%
# Count how many "?" symbols appear in each column
for col in df.columns:
    count = (df[col] == '?').sum()
    if count > 0:
        print(f"{col}: {count} '?' values")
        
df['race'] = df['race'].replace('?', 'unknown')
df['medical_specialty'] = df['medical_specialty'].replace('?', 'unknown')
df['diag_2'] = df['diag_2'].replace('?', 'unknown')
df['diag_3'] = df['diag_3'].replace('?', 'unknown')

(df == '?').any().any()

# %%
#Explore Data Analysis
#1)Readmission %
readmit_percentage = (df['readmitted'].value_counts(normalize=True).mul(100).rename("percentage").reset_index())
print(readmit_percentage.round(2))
values = readmit_percentage["percentage"]
labels = readmit_percentage["readmitted"]
plt.pie(values,labels = labels,autopct = "%1.2f",data = df)
# plt.title("Readmitted %")
# plt.show()

sns.countplot(x = 'readmitted',data = df, hue = 'readmitted',palette = 'Set2')
plt.title("Readmission Counts")
plt.show()

# %%
#2)Readmission by Gender
gender_readmit = (df.groupby('gender')['readmitted'].value_counts(normalize = True).mul(100).rename('Percentage').reset_index())
print(gender_readmit)
sns.barplot(data = gender_readmit,x = 'gender',y = 'Percentage',hue = 'readmitted',width = 0.5)
plt.show()

# %%
#3)Readmission by Race
race_readmit = df.groupby('race')['readmitted'].value_counts(normalize = True).mul(100).rename("percentage").reset_index()
print(race_readmit)
values = race_readmit['percentage']
labels = race_readmit['race']
sns.barplot(x = 'race',y = 'percentage', hue = 'readmitted',data = race_readmit)
plt.title("Readmission by Race")
plt.show()

# %%
#5)Readmission by Age Group?
age_readmit = df.groupby('age')['readmitted'].value_counts(normalize = True).mul(100).rename("percentage").reset_index()
print(age_readmit)
sns.barplot(x = 'age',y = 'percentage', hue = 'readmitted',data = age_readmit)
plt.title("Readmission by age")
plt.show()

# %%
# Map age ranges to mid-points
age_map = {
    '[0-10)': 5,
    '[10-20)': 15,
    '[20-30)': 25,
    '[30-40)': 35,
    '[50-60)': 55,
   '[40-50)': 45,
   '[60-70)': 65,
    '[70-80)': 75,
    '[80-90)': 85,
    '[90-100)': 95
}

df['age_mid'] = df['age'].map(age_map)

# Map age ranges to mid-points
age_map = {
    '[0-10)': 5,
    '[10-20)': 15,
    '[20-30)': 25,
    '[30-40)': 35,
    '[40-50)': 45,
    '[50-60)': 55,
    '[60-70)': 65,
    '[70-80)': 75,
    '[80-90)': 85,
    '[90-100)': 95
}

df['age_mid'] = df['age'].map(age_map)

age_mid__readmit = (df.groupby('age_mid')['readmitted'].value_counts(normalize = True).mul(100).rename("percentage").reset_index())
sns.barplot(x = 'age_mid',y = 'percentage', hue = 'readmitted',data = age_mid__readmit)
plt.title("Readmission by age_mid")
plt.show()


# %%
#6)Readmission by time_in_hospital
time_in_hospital_readmit = df.groupby('time_in_hospital')['readmitted'].value_counts(normalize = True).mul(100).rename('Percentage').reset_index()
print(time_in_hospital_readmit)
sns.barplot(data = time_in_hospital_readmit,x = 'time_in_hospital',y = 'Percentage',hue = 'readmitted',palette = 'Set1')
plt.show()


# %%

#7) Readmission by number_inpatient
inpatient_readmit = (
    df.groupby('number_inpatient')['readmitted']
    .value_counts(normalize=True)
    .mul(100)
    .rename("Percentage")
    .reset_index()
)

sns.barplot(data=inpatient_readmit, x='number_inpatient', y='Percentage', hue='readmitted', palette='Set2')
plt.title("Readmission Rate by Inpatient Visits")
plt.xlabel("Number of Inpatient Visits")
plt.ylabel("Percentage")
plt.show()


# %%
#8)Insulin usage V/S Readmission
insulin_readmit = (
    df.groupby('insulin')['readmitted']
    .value_counts(normalize=True)
    .mul(100)
    .rename("Percentage")
    .reset_index()
)

sns.barplot(data=insulin_readmit, x='insulin', y='Percentage', hue='readmitted', palette='Set2')
plt.title("Readmission Rate by Insulin Usage")
plt.xlabel("Insulin Usage")
plt.ylabel("Percentage")
plt.show()


# %%
#Readmission by metaform_usage
metformin_readmit = (
    df.groupby('metformin')['readmitted']
    .value_counts(normalize=True)
    .mul(100)
    .rename("Percentage")
    .reset_index()
)

sns.barplot(data=metformin_readmit, x='metformin', y='Percentage', hue='readmitted', palette='Set3')
plt.title("Readmission Rate by Metformin Usage")
plt.xlabel("Metformin Usage")
plt.ylabel("Percentage")
plt.show()


# %%
#10)Readmission by Medical_specialty
specialty_readmit = (
    df.groupby('medical_specialty')['readmitted']
    .value_counts(normalize=True)
    .mul(100)
    .rename("Percentage")
    .reset_index()
)

plt.figure(figsize=(12,6))
sns.barplot(data=specialty_readmit, x='medical_specialty', y='Percentage', hue='readmitted', palette='Set1')
plt.xticks(rotation=90)
plt.title("Readmission Rate by Medical Specialty")
plt.xlabel("Medical Specialty")
plt.ylabel("Percentage")
plt.show()


# %%
#11)Readmission by diagnosis_group
# Group by diag_1 and readmission, calculate percentage
# STEP 1: Filter top 10 diagnosis codes
top10_diag = (
    df['diag_1'].value_counts()
    .head(10)
    .index.tolist()
)

# STEP 2: Filter dataset to include only those top 10 diagnoses
diag_subset = df[df['diag_1'].isin(top10_diag)]

# STEP 3: Group, calculate percentage readmissions
diag_readmit = (
    diag_subset.groupby('diag_1')['readmitted']
    .value_counts(normalize=True)
    .mul(100)
    .rename("Percentage")
    .reset_index()
)

# STEP 4: Plot
plt.figure(figsize=(12,6))
sns.barplot(data=diag_readmit, x='diag_1', y='Percentage', hue='readmitted', palette='Set2')
plt.title("Readmission Rate by Top 10 Primary Diagnoses")
plt.xlabel("Diagnosis Code")
plt.ylabel("Percentage")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%
#Readmission rate by change in medication
change_readmit = (
    df.groupby('change')['readmitted']
    .value_counts(normalize=True)
    .mul(100)
    .rename("Percentage")
    .reset_index()
)
print(change_readmit)

plt.figure(figsize=(6,5))
sns.barplot(data=change_readmit, x='change', y='Percentage', hue='readmitted', palette='Set3')
plt.title("Readmission Rate by Change in Medication")
plt.xlabel("Change in Medication")
plt.ylabel("Percentage")
plt.tight_layout()
plt.show()


# %%
#Readmission rate by Diabeted medication
diabetesMed_readmit = (
    df.groupby('diabetesMed')['readmitted']
    .value_counts(normalize=True)
    .mul(100)
    .rename("Percentage")
    .reset_index()
)
print(diabetesMed_readmit)
plt.figure(figsize=(6,5))
sns.barplot(data=diabetesMed_readmit, x='diabetesMed', y='Percentage', hue='readmitted', palette='Set1')
plt.title("Readmission Rate by Diabetes Medication")
plt.xlabel("Diabetes Medication")
plt.ylabel("Percentage")
plt.tight_layout()
plt.show()


# %%
df.to_csv("deep_cleaned_patient_data.csv",index = False)
df = pd.read_csv("deep_cleaned_patient_data.csv")
print(df)


# %%
from sqlalchemy import create_engine

# MySQL connection

username = "root"

password = "Sri@12345"

host = "localhost"

port = "3306"

database = "healthcare_db"

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

# Write DataFrame to MySQL

table_name = "mytable" # choose any table name

df.to_sql(table_name, engine, if_exists="replace", index=False)

# Read back sample

pd.read_sql("SELECT * FROM mytable LIMIT 5;", engine) 






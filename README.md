# Healthcare Readmission Analysis Project

*(Python + SQL + Excel + Power BI)*

## 1. Project Overview

The Healthcare Readmission Analysis project was developed to analyze hospital patient records and identify the major reasons why patients get readmitted within a short period after discharge.

The project focused on:

* Understanding patient readmission patterns
* Identifying high-risk patients
* Finding important medical and operational factors affecting readmissions
* Creating dashboards and reports for healthcare decision-making
* Helping hospitals improve patient care and reduce unnecessary costs

This project combines:

* **Python** for data cleaning, preprocessing, and analysis
* **SQL** for database management and querying
* **Excel** for initial data validation and quick analysis
* **Power BI** for interactive dashboards and visual storytelling

---

# 2. Problem Statement

Hospital readmissions are a major challenge in the healthcare industry because:

* They increase treatment costs
* They indicate possible gaps in patient care
* They affect hospital performance metrics
* They reduce patient satisfaction

The objective of this project was to:

1. Analyze patient admission and discharge records
2. Detect factors causing frequent readmissions
3. Build visual dashboards for healthcare insights
4. Support hospitals in improving healthcare quality

---

# 3. Dataset Information

The dataset contained healthcare patient records with columns such as:

| Column Name        | Description                              |
| ------------------ | ---------------------------------------- |
| Patient_ID         | Unique patient identifier                |
| Age                | Patient age group                        |
| Gender             | Male/Female                              |
| Admission_Type     | Emergency, Urgent, Elective              |
| Diagnosis          | Disease or medical condition             |
| Time_in_Hospital   | Number of hospitalization days           |
| Num_Lab_Procedures | Number of lab tests                      |
| Num_Medications    | Total medications prescribed             |
| Number_Outpatient  | Outpatient visits                        |
| Number_Emergency   | Emergency visits                         |
| Number_Inpatient   | Previous inpatient visits                |
| DiabetesMed        | Whether diabetic medicine was prescribed |
| Readmitted         | Whether patient was readmitted           |

---

# 4. Tools & Technologies Used

## A. Python

Python

### Purpose of Using Python

Python was mainly used for:

* Data cleaning
* Data preprocessing
* Exploratory Data Analysis (EDA)
* Statistical analysis
* Data transformation

### Python Libraries Used

| Library          | Purpose                         |
| ---------------- | ------------------------------- |
| Pandas           | Data manipulation and cleaning  |
| NumPy            | Numerical operations            |
| Matplotlib       | Data visualization              |
| Seaborn          | Statistical charts and heatmaps |
| Scikit-learn     | Basic predictive analysis       |
| Jupyter Notebook | Development environment         |

### Tasks Performed in Python

#### 1. Handling Missing Values

* Removed null records
* Filled missing data using mean/mode techniques

#### 2. Data Cleaning

* Removed duplicate records
* Standardized column names
* Corrected inconsistent values

#### 3. Exploratory Data Analysis

Analyzed:

* Readmission rate by age
* Readmission rate by disease
* Medication usage
* Emergency visit frequency

#### 4. Feature Engineering

Created:

* Risk categories
* Readmission flags
* Age group segmentation

#### 5. Correlation Analysis

Identified relationships between:

* Hospital stay duration
* Medication count
* Emergency visits
* Readmission probability

---

# 5. SQL Usage

MySQL

## Purpose of SQL in the Project

SQL was used to:

* Store patient records in a database
* Query large healthcare datasets
* Perform aggregations and filtering
* Generate business insights

---

# 6. Excel Usage

Microsoft Excel

## Purpose of Excel

Excel was used for:

* Initial dataset inspection
* Manual validation
* Data formatting
* Quick pivot analysis

---

## Excel Features Used

| Feature                | Purpose                     |
| ---------------------- | --------------------------- |
| Pivot Tables           | Summary analysis            |
| Conditional Formatting | Highlighting high-risk data |
| Filters & Sorting      | Data inspection             |
| Charts                 | Quick visualization         |
| Data Cleaning          | Removing inconsistencies    |

---

# 7. Power BI Dashboard

Microsoft Power BI

## Purpose of Power BI

Power BI was used to:

* Build interactive dashboards
* Visualize patient readmission trends
* Present insights to stakeholders
* Enable data-driven decisions

---

# 8. Dashboard Components

## KPIs Created

| KPI                   | Description                       |
| --------------------- | --------------------------------- |
| Total Patients        | Total patient records             |
| Readmission Rate      | Percentage of readmitted patients |
| Average Hospital Stay | Average stay duration             |
| Emergency Visit Count | Total emergency visits            |
| Medication Usage      | Average medications prescribed    |

---

## Visualizations Used

| Visualization | Purpose                     |
| ------------- | --------------------------- |
| Bar Chart     | Readmission by age          |
| Pie Chart     | Admission type distribution |
| Line Chart    | Monthly readmission trends  |
| Heatmap       | Correlation analysis        |
| KPI Cards     | Key metrics                 |
| Slicers       | Interactive filtering       |

---

# 9. Key Insights Generated

## Major Findings

### 1. Elderly Patients Had Higher Readmission Rates

Patients above certain age groups showed frequent readmissions due to chronic diseases.

---

### 2. Emergency Admissions Increased Readmission Probability

Emergency cases had significantly higher chances of returning to the hospital.

---

### 3. Longer Hospital Stay Indicated Higher Risk

Patients staying more days were more likely to be readmitted.

---

### 4. High Medication Usage Correlated With Readmissions

Patients taking many medications often had complex health conditions.

---

### 5. Certain Diagnoses Were High-Risk

Diseases like diabetes and heart conditions contributed heavily to readmissions.

---

# 10. Business Impact

The project helps hospitals:

* Identify high-risk patients early
* Improve discharge planning
* Reduce unnecessary readmissions
* Optimize healthcare resources
* Enhance patient outcomes

---

# 11. End-to-End Workflow

## Step-by-Step Workflow

### Step 1: Data Collection

Collected healthcare patient data from CSV files.

↓

### Step 2: Data Cleaning in Python

Handled missing values and inconsistencies.

↓

### Step 3: Database Storage Using SQL

Stored cleaned data in MySQL database.

↓

### Step 4: SQL Analysis

Performed data aggregation and filtering for insights.

↓

### Step 5: Visualization in Power BI

Created dashboards and KPIs.

↓

### Step 6: Insight Generation

Identified patterns and healthcare recommendations.

---

# 12. Challenges Faced

| Challenge              | Solution                      |
| ---------------------- | ----------------------------- |
| Missing data           | Used preprocessing techniques |
| Large dataset handling | Optimized data processing     |
| Inconsistent values    | Standardized formats          |
| Dashboard performance  | Reduced unnecessary visuals   |

---

# 13. Skills Demonstrated

## Technical Skills

* Python Programming
* SQL Database Management
* Data Cleaning
* Data Analysis
* Dashboard Development
* Business Intelligence

## Analytical Skills

* Problem Solving
* Insight Generation
* Trend Analysis
* Data Interpretation

---

# 14. Future Improvements

Possible future enhancements:

* Machine learning prediction model
* Real-time hospital monitoring
* Patient risk scoring system
* Cloud database integration
* Automated alerts for high-risk patients

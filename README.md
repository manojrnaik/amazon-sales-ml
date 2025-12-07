# amazon-sales-ml
End-to-end Data Scientist Project: Sales Prediction &amp; Analysis

---

# 📘 Amazon Sales ML Project

### **End-to-End Data Science Project | Data Cleaning → EDA → Feature Engineering → ML Model → Dashboard**

This project demonstrates a complete **Data Scientist workflow** using a real-world-style sales dataset.


* Data cleaning skills
* Exploratory analysis
* Feature engineering
* Machine learning model
* Data visualization
* Dashboard creation
* Clean, modular code
* End-to-end thinking

---

## 🚀 Project Overview

This project analyzes Amazon-style sales data and builds a **prediction model** to understand and forecast product pricing based on quantity, time, and other features.

It includes:

* 🧹 **Data Cleaning**
* 🔍 **EDA (Exploratory Data Analysis)**
* 🏗 **Feature Engineering**
* 🤖 **ML Model (Linear Regression)**
* 📉 **Model Evaluation (MSE, R²)**
* 📊 **Visual Dashboard (Chart.js)**

---

## 🗂️ Project Structure

amazon-sales-ml/
│── data/
│     └── sales.csv
│     └── sales_clean.csv
│     └── sales_features.csv
│
│── notebooks/
│     └── analysis.ipynb
│
│── scripts/
│     ├── clean_data.py
│     ├── feature_engineering.py
│     └── model.py
│
│── dashboard/
│     └── dashboard.html
│
│
│── README.md

---

## 🧹 Data Cleaning

Performed in **clean_data.py**:

* Handled missing values
* Converted dates
* Ensured correct types
* Removed inconsistencies

---

## 🔍 Exploratory Data Analysis (EDA)

Performed inside **analysis.ipynb**:

* Sales over time
* Sales by category
* Regional distribution
* Outlier checks
* Trend analysis

Uses:

* Pandas
* Matplotlib
* Seaborn

---

## 🏗 Feature Engineering

Performed in **feature_engineering.py**:

New features created:

| Feature      | Description         |
| ------------ | ------------------- |
| TotalSales | Quantity × Price    |
| OrderMonth | Extracted from date |
| OrderDay   | Extracted from date |

These features are used for ML.

---

## 🤖 Machine Learning Model

Performed in **model.py** using **scikit-learn**.

Model:

Linear Regression


Metrics:

* **MSE (Mean Squared Error)**
* **R² Score (Model Fit)**


---

## 📊 Dashboard

Interactive HTML dashboard using **Chart.js**.

Shows:

* Total Sales by Category
* Sales Trend Over Time

📄 File: dashboard/dashboard.html

---

## 💼 Skills Demonstrated

### **Data Science Skills**

* Data cleaning
* Exploratory analysis
* Feature engineering
* Machine learning
* Linear regression
* Model evaluation
* Data visualization

### **Technical Skills**

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Chart.js
* Git & GitHub

### **Soft Skills**

* Problem solving
* End-to-end project thinking
* Documentation
* Communication of insights

---

## 🏃 How to Run

### 📌 Run Data Cleaning

python scripts/clean_data.py


### 📌 Run Feature Engineering

python scripts/feature_engineering.py


### 📌 Train Model

python scripts/model.py


### 📌 Open Dashboard

Open:

dashboard/dashboard.html


---

## 🙋 For Recruiters

This project demonstrates my ability to think and work like a **Data Scientist**:

* Ability to take raw data → clean → analyze → engineer → model → visualize
* Strong understanding of ML fundamentals
* Ability to present insights clearly
* Professional GitHub workflow

If you'd like a walkthrough of the project, I would love to connect!

---


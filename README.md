# 🛍️ Shopper Spectrum

## Customer Segmentation & Product Recommendation System

### 📌 Project Overview

Shopper Spectrum is a Machine Learning and Data Analytics project that performs customer segmentation using RFM Analysis and K-Means Clustering and recommends similar products using Item-Based Collaborative Filtering.

The project is developed using Python, Pandas, Scikit-learn, and Streamlit.

---

## 📊 Dataset

Dataset: Online Retail Dataset

The dataset contains customer purchase transactions including:

- Invoice Number
- Product Description
- Quantity
- Invoice Date
- Unit Price
- Customer ID
- Country

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Joblib

---

## 📌 Project Workflow

### 1. Data Preprocessing

- Removed missing CustomerID values
- Removed cancelled invoices
- Removed negative and zero quantities
- Removed negative and zero prices

---

### 2. Exploratory Data Analysis

Performed:

- Transaction analysis by country
- Top-selling products
- Purchase trend over time
- Monetary distribution
- RFM distribution
- Elbow Method
- Customer Cluster Profiles
- Product Similarity Matrix

---

### 3. Customer Segmentation

Used RFM Analysis.

Features:

- Recency
- Frequency
- Monetary

Standardized using StandardScaler.

Applied K-Means Clustering.

Selected the optimal number of clusters using:

- Elbow Method
- Silhouette Score

Customer Segments:

- ⭐ High-Value Customer
- 👤 Regular Customer
- 🛍️ Occasional Customer
- ⚠️ At-Risk Customer

---

### 4. Product Recommendation System

Used Item-Based Collaborative Filtering.

Steps:

- Created Customer–Product Matrix
- Calculated Cosine Similarity
- Recommended Top 5 Similar Products

---

## 📱 Streamlit Application

### Home Page

Displays project overview and technologies used.

### Customer Segmentation

Input:

- Recency
- Frequency
- Monetary

Output:

- Predicted Cluster
- Customer Segment

### Product Recommendation

Input:

- Product Name

Output:

- Top 5 Similar Products

---

## 📂 Project Structure

```
Project 2/
│
├── app.py
├── cleaned_online_retail.csv
├── EDA.ipynb
├── kmeans_model.pkl
├── scaler.pkl
├── similarity_matrix.pkl
├── requirements.txt
├── style.css
│
└── pages/
    ├── Clustering.py
    └── Recommendation.py
```

---

## 🚀 How to Run

Install the required libraries:

```
pip install -r requirements.txt
```

Run the application:

```
streamlit run app.py
```

---

## 📈 Machine Learning Techniques

- Data Cleaning
- Feature Engineering
- RFM Analysis
- StandardScaler
- K-Means Clustering
- Elbow Method
- Silhouette Score
- Item-Based Collaborative Filtering
- Cosine Similarity

---

## 📷 Output

The application provides:

- Customer Segmentation Prediction
- Product Recommendation
- Interactive Streamlit Interface

---

## 👩‍🎓 Developed By

**Trisha Pramanik**

BCA (Analytics)

Customer Segmentation & Product Recommendation System using Machine Learning




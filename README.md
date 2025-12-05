# 🎯 IBM Capstone Project — SpaceX Launch Success Prediction

End-to-end Data Science workflow including **Web Scraping**, **Data Wrangling**, **SQL EDA**, **Visualization**, **Folium Maps**, **Interactive Dashboard**, and **Machine Learning**.

---

## 📁 Repository Structure

```
notebooks/
    01_data_collection_webscraping.ipynb
    02_Data_Wrangling.ipynb
    03_SQL_EDA.ipynb
    04_visual_EDA.ipynb
    05_interactive_map_folium.ipynb
    Interactive_Dashboard_with_Plotly_Dash.ipynb
    Machine_Learning_Prediction_Model.ipynb

scripts/
    data_cleaning.py
    model_training.py
    utils.py

data/
    launch_site_locations.csv
    README.md

results/
    README.md

presentation/
    README.md
```

---

## 🚀 Project Overview

This capstone project aims to **predict Falcon 9 first-stage landing success** using multiple data science techniques:

- Web Scraping  
- API Data Extraction  
- Data Cleaning & Wrangling  
- SQL-based Exploratory Data Analysis  
- Visual EDA (Seaborn & Matplotlib)  
- Interactive Folium Map  
- Plotly Dash Dashboard  
- Predictive Machine Learning Models  
- Hyperparameter Tuning  

All notebooks and scripts in this repository represent a full end-to-end data science workflow.

---

## 📊 Machine Learning Models Used

- Logistic Regression  
- K-Nearest Neighbors (KNN)  
- Support Vector Machine (SVM)  
- Decision Tree Classifier  
- GridSearchCV for Hyperparameter Optimization  

Model comparison and performance evaluation are included in the final notebook.

---

## 🌍 Interactive Folium Map

The map uses **official SpaceX launch site coordinates**:

| Launch Site    | Latitude  | Longitude   |
|----------------|-----------|-------------|
| KSC LC-39A     | 28.608058 | -80.603956  |
| CCAFS LC-40    | 28.561857 | -80.577366  |
| VAFB SLC-4E    | 34.632093 | -120.610829 |

Folium is used to plot markers, popup info, and radius overlays.

---

## 📈 Interactive Dashboard (Plotly Dash)

Features include:

- Launch Site Selector  
- Payload Mass Range Slider  
- Success/Failure Pie Chart  
- Payload vs Outcome Scatter Plot  
- Neon-themed modern dashboard UI  

Dashboard script: **spacex_dash_app.py**

---

## 📚 How to Run the Project

Install required packages:

```
pip install -r requirements.txt
```

Run notebooks sequentially:

```
01 → 07
```

Run dashboard locally:

```
python spacex_dash_app.py
```

---

## ✨ Author

**AQSA ADBULLAH**  
LINGUIST • Data Scientist • CURIOUS TO LEARN

---

## 📄 License

MIT License

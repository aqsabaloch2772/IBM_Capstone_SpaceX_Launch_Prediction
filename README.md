🎯 IBM Capstone Project — SpaceX Launch Success Prediction

End-to-end Data Science workflow including Web Scraping, Data Wrangling, SQL EDA, Visualization, Folium Maps, Interactive Dashboard, and Machine Learning.

📁 Repository Structure
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

🚀 Project Overview

This project predicts the success of SpaceX Falcon 9 first-stage landings using:

✔ Web Scraping
✔ REST API data collection
✔ Data Wrangling & Feature Engineering
✔ SQL Exploratory Data Analysis
✔ Visual EDA (Matplotlib & Seaborn)
✔ Interactive Folium Map
✔ Interactive Plotly Dash Dashboard
✔ Machine Learning Classification Models
✔ Hyperparameter Tuning

This repository contains all notebooks, scripts, datasets, and the final presentation.

📊 Machine Learning Models Used

Logistic Regression

K-Nearest Neighbors (KNN)

Support Vector Machine (SVM)

Decision Tree Classifier

Hyperparameter tuning via GridSearchCV

The best performing model achieved your accuracy will go here once confirmed.

🌍 Interactive Folium Map

Using official SpaceX launch coordinates:

Launch Site	Latitude	Longitude
KSC LC-39A	28.608058	-80.603956
CCAFS LC-40	28.561857	-80.577366
VAFB SLC-4E	34.632093	-120.610829

The map shows launch site markers, circles, and popups for visualization.

📈 Interactive Dashboard (Plotly Dash)

Features include:

Launch Site dropdown

Payload mass slider

Success/Failure pie chart

Payload vs. Outcome scatter plot

Animated neon-themed modern UI

📚 How to Run the Project

Install dependencies:

pip install -r requirements.txt


Run notebooks in order:

01 → 07


Run dashboard locally:

python spacex_dash_app.py

✨ Author

AQSA ABDULLAH 


📄 License

MIT License

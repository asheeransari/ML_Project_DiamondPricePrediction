## ML_Project_DiamondPricePrediction
## Project Info

This is an End-to-End Machine Learning Project that predicts the price of diamonds based on multiple physical and quality-related features such as carat, cut, color, clarity, and dimensions.

The project follows industry-level project architecture, including data preprocessing pipelines, model training, prediction pipelines, and deployment using a Flask web application.
It demonstrates how a machine learning model can be taken from data analysis to real-world deployment.

## Problem Statement

Diamond prices vary significantly based on their physical and quality attributes.
The objective of this project is to build a regression-based machine learning model that accurately predicts the diamond price given its features, helping users estimate fair market value.

## Requirements

1 - Python 3.11<br>
2 - VS Code
3 - Jupyter Notebook<br>
4 - Git<br>
5 - GitHub<br>
6 - Flask<br>
7 - Virtual Environment

# List of Libraries Used

1 - numpy<br>
2 - pandas<br>
3 - matplotlib<br>
4 - seaborn<br>
5 - scikit-learn<br>
6 - flask<br>
7 - jinja2<br>
8 - pickle<br>
9 - logging

## Project Structure
DiamondPricePrediction/<br>
│<br>
├── application.py ----->            <i>Flask entry point</i><br>
├── src/<br>
│   ├── components/ ----->          Data ingestion & transformation<br>
│   ├── pipelines/ ----->          Training & prediction pipelines<br>
│   ├── exception/ ----->          Custom exception handling<br>
│   ├── logger/ ----->          Logging configuration<br>
│<br>
├── templates/ ----->             HTML templates<br>
│   ├── index.html<br>
│   ├── form.html<br>
│   ├── result.html<br>
│<br>
├── artifacts/ ----->               Saved model & preprocessing objects<br>
├── notebooks/ ----->               EDA & model training notebooks<br>
├── setup.py ----->               Package configuration<br>
├── requirements.txt ----->          Project dependencies<br>
├── README.md

## Steps Used in This Project

1 - Data Collection<br>
2 - Data Cleaning and Preparation<br>
3 - Exploratory Data Analysis (EDA)<br>
4 - Data Visualization<br>
5 - Feature Engineering<br>
6 - Handling Missing Values<br>
7 - Feature Scaling and Encoding<br>
8 - Model Training and Evaluation<br>
9 - Hyperparameter Tuning<br>
10 - Saving the Best Model<br>
11 - Creating Prediction Pipeline<br>
12 - Flask Web Application Integration<br>
13 - End-to-End Deployment Ready Setup

## Author

Asheer Ahmad Ansari<br>
B.Tech Graduate | Aspiring Data Scientist<br>
LinkedIn: https://www.linkedin.com/in/asheer-an
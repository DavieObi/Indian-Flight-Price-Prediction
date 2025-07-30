# Indian Flight Price Prediction

## Overview
This project is aimed at predicting the prices of flights in India based on various features such as airline, source city, departure time, number of stops, and more. The goal is to build a predictive model that can estimate the cost of a flight given specific inputs, helping travelers make more informed decisions.

## Problem Statement
Flight prices can vary significantly depending on several factors, making it difficult for travelers to predict the cost of their journey. The problem is to develop a machine learning model that accurately predicts flight prices based on relevant features.

## Objective
The objective of this project is to develop a machine learning model that predicts the price of flights in India using a dataset containing flight details. The model should provide an estimate of the flight price based on input features such as airline, source city, departure time, and others.

## Exploratory Data Analysis (EDA)
Exploratory Data Analysis was performed to understand the distribution of flight prices, examine correlations between variables, and identify any patterns or trends in the data. Visualizations and statistical analyses were used to explore relationships between different features and the target variable (flight price).

## Data Preprocessing
Data preprocessing steps included:
- Handling missing values
- Encoding categorical variables using Label Encoding
- Splitting the dataset into training and testing sets

These steps ensured that the data was in a suitable format for modeling.

## Features
The following features were used in the model:
- **Airline**: The airline operating the flight
- **Source City**: The city from which the flight departs
- **Departure Time**: The time of day when the flight departs
- **Stops**: The number of stops during the flight
- **Arrival Time**: The time of day when the flight arrives
- **Destination City**: The city where the flight arrives
- **Class**: The travel class (Economy, Business)
- **Duration**: The duration of the flight in hours
- **Days Left**: The number of days left before the flight departs

## How It Works
The user inputs details such as airline, source city, departure time, and other relevant features into the app. The pre-trained linear regression model processes these inputs and predicts the flight price. The prediction is displayed on the app interface, providing the user with an estimated flight cost.

## Technologies Used
- **Python**: Programming language used for the entire project
- **Pandas**: For data manipulation and analysis
- **NumPy**: For numerical computations
- **Scikit-learn**: For model training and evaluation
- **Streamlit**: For building and deploying the web app
- **Pickle**: For saving and loading the model and encoders
- **Matplotlib/Seaborn**: For data visualization during EDA
- **Pillow**: For handling images in the Streamlit app

## Additional Features
- **User-Friendly Interface**: An intuitive form for entering data such as number of stops, airline, departure time, etc.
- **Machine Learning Model**: A pre-trained linear regression algprithm ensures accurate and reliable predictions.
- **Real-Time Predictions**: Instant feedback on flight prices are provided upon form submission.
- **Data Preprocessing**: Includes encoding categorical variable into numerical variables to optimize model performance.

## Project Structure
```plaintext
├── data
│   └── Flight price prediction.csv
├── encoders
│   ├── Airline_encoder.pkl
│   ├── Source_city_encoder.pkl
│   ├── Departure_time_encoder.pkl
│   ├── Stops_encoder.pkl
│   ├── Arrival_time_encoder.pkl
│   ├── Destination_city_encoder.pkl
│   └── Class_encoder.pkl
├── images
│   └── airport.png
├── models
│   └── lr_model.pkl
├── notebooks
│   └── flight_price_prediction.ipynb
├── app
│   └── deploy.py
├── README.md
└── requirements.txt

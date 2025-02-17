# Enhancing Fraud Detection Systems for ECommerce and Banking Transactions

## Executive Summary
Adey Innovations Inc., a leader in financial technology, is developing advanced fraud detection systems to secure ecommerce and banking transactions. This project leverages machine learning, geolocation analysis, and transaction pattern recognition to accurately identify fraudulent activities. By analyzing data, engineering fraud revealing features, and deploying real time detection models, the initiative aims to minimize financial losses, enhance customer trust, and ensure efficient monitoring for continuous improvement in combating fraud.

## Business Need
Financial fraud can lead to significant losses for businesses and customers. This system helps Adey Innovations Inc. identify and prevent fraudulent activities using advanced machine learning models. Real-time monitoring and geolocation-based fraud detection provide added layers of security.

## Datasets
- Fraud_Data.csv: Contains e-commerce transactions data with details such as user information, device, purchase details, and fraud labels.
- IpAddress_to_Country.csv: Maps IP addresses to countries to identify the geolocation of the user.
- creditcard.csv: Contains anonymized bank credit card transaction data curated for fraud detection.
  
## Features
- Transaction Frequency and Velocity Features
- Time-Based Features: Hour of day, Day of the week
- Geolocation-based fraud detection using IP-to-country mapping

## Machine Learning Models
The project implements and compares several machine learning models:

- Logistic Regression
- Random Forest
- Decision Tree
- Gradient Boosting
- Neural Networks (MLP, CNN, RNN, LSTM)
  
## Model Explainability
We uses SHAP and LIME to explain model predictions and feature importance. This enhances transparency and trust in the model.

## Flask API and Docker Deployment
The fraud detection model is deployed using Flask, containerized with Docker, and exposed via a REST API for real-time prediction. Logging is integrated for continuous monitoring.

## Dash Dashboard
An interactive dashboard built with Dash to visualize fraud detection insights such as:

- Transaction counts and fraud cases
- Fraud trends over time
- Geolocation analysis of fraud cases
- Device and browser comparisons for fraudulent activities

## Installation

1. clone the repository

```bash
git clone https://github.com/wastb/E-Commerce-and-Credit-Card-Fraud-Detection
```

2. install the required libraries
   
```bash
pip install -r requirements.txt
```

3. Start Exploring

## Contact Information

#### - Name: ***Wasihun Tesfaye***
#### - E-Mail: wasihunpersonal@gmail.com

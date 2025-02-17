from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np
from datetime import datetime
import pickle

import flask_preprocessing

app = Flask(__name__)

# Load the trained fraud detection model
with open("xgboost_fraud.pkl", "rb") as file:
    fraud_model = pickle.load(file)  

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Log the form data to check what's being received
            app.logger.info(f"Form data received: {request.form}")

            # Get form data
            date_sgn = request.form['Signup_Date']
            date_sgn = datetime.strptime(date_sgn, '%Y-%m-%d')
            date_purch = request.form['Purchase_Date']
            date_purch = datetime.strptime(date_purch, '%Y-%m-%d')
            purchase_value = float(request.form['Purchase_Value'])
            source = request.form['Source']
            browser = request.form['Browser']
            sex = request.form['Sex']
            age = int(request.form['Age'])
            ip_address = int(request.form['Ip_Address'])
            frequency = int(request.form['Frequency'])
            velocity = float(request.form['Velocity'])


            # Create a dictionary to pass data to the template
            form_data = {
                "signup_time": date_sgn.strftime('%Y-%m-%d'),
                "purchase_time": date_purch.strftime('%Y-%m-%d'),
                "purchase_value": purchase_value,
                "source": source,
                "browser": browser,
                "sex": sex,
                "age": age,
                "ip_address": ip_address,
                "frequency": frequency,
                "velocity": velocity
            }

            df = pd.DataFrame([form_data])

            ##Preprocess data before prediction
            data = flask_preprocessing.preprocess(df)

            ##Predict fraud 
            prediction = fraud_model.predict(data)

            # Render a result template with extracted form data
            return render_template('result.html', form_data=form_data,prediction=prediction[0])

        except Exception as e:
            app.logger.error(f"Error during form processing: {str(e)}")
            return render_template('error.html', error_message=str(e))
        
    return render_template('index.html')


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True)


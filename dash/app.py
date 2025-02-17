import pandas as pd
from flask import Flask, render_template
import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go

# Initialize Flask app
app = Flask(__name__)

# Initialize Dash app
dash_app = dash.Dash(__name__, server=app, url_base_pathname='/')

# Load the fraud data from CSV
df = pd.read_csv('../data/Fraud_Data.csv') 
df_ip_adress = pd.read_csv('ip.csv')

# Function to map IP to Country
def ip_to_country(ip):
    try:
        return df_ip_adress.country[
            (df_ip_adress.lower_bound_ip_address < ip) & 
            (df_ip_adress.upper_bound_ip_address > ip)
        ].iloc[0]
    except IndexError:
        return "Unknown"

df['country'] = df['ip_address'].apply(ip_to_country)

# Convert date columns to datetime format
df['signup_time'] = pd.to_datetime(df['signup_time'])
df['purchase_time'] = pd.to_datetime(df['purchase_time'])

# Compute statistics
total_transactions = len(df)
fraud_cases = len(df[df['class'] == 1])
fraud_percentage = fraud_cases / total_transactions * 100

# Compute trends
fraud_trends = df.groupby(df['signup_time'].dt.date)['class'].sum().reset_index()
fraud_by_device_browser = df.groupby(['browser'])['class'].sum().reset_index()

# Fraud cases by location (Top 10 Countries)
fraud_by_location = df.groupby('country')['class'].sum().reset_index()
fraud_by_location = fraud_by_location.sort_values(by='class', ascending=False).head(10)  # Top 10

# Flask Route for Homepage
@app.route('/')
def home():
    return render_template('index.html')

# Dash Layout and Visualizations
dash_app.layout = html.Div([
    html.H1('Fraud Detection Dashboard', style={'text-align': 'center'}),

    # Summary Statistics Section (Using Cards)
    html.Div([
        html.Div([
            html.H3('Total Transactions', style={'text-align': 'center'}),
            html.H2(f"{total_transactions:,}", style={'text-align': 'center', 'color': '#2E86C1'}),
        ], className='card'),

        html.Div([
            html.H3('Fraud Cases', style={'text-align': 'center'}),
            html.H2(f"{fraud_cases:,}", style={'text-align': 'center', 'color': '#C0392B'}),
        ], className='card'),

        html.Div([
            html.H3('Fraud Percentage', style={'text-align': 'center'}),
            html.H2(f"{fraud_percentage:.2f}%", style={'text-align': 'center', 'color': '#16A085'}),
        ], className='card'),
    ], style={'display': 'flex', 'justify-content': 'space-around', 'padding': '20px'}),

    # Fraud Trends (Line Chart)
    dcc.Graph(
        id='fraud-trends',
        figure=go.Figure(
            data=[go.Scatter(x=fraud_trends['signup_time'], y=fraud_trends['class'], mode='lines')],
            layout=go.Layout(title='Fraud Trends Over Time', xaxis=dict(title='Date'), yaxis=dict(title='Number of Fraud Cases'))
        )
    ),

    # Fraud by Location (Top 10 Countries)
    dcc.Graph(
        id='fraud-by-location',
        figure=px.bar(
            fraud_by_location, 
            x='country', y='class', 
            title='Top 10 Countries by Fraud Cases', 
            color='class', 
            color_continuous_scale='Reds'
        )
    ),

    # Fraud by Device/Browser (Bar Chart)
    dcc.Graph(
        id='fraud-by-device-browser',
        figure=px.bar(fraud_by_device_browser, x='browser', y='class', title='Fraud by Device and Browser')
    ),
])

if __name__ == '__main__':
    app.run(debug=True, port=5001)

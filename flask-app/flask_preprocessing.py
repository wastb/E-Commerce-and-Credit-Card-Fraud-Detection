import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder

def preprocess(df):
    df_ip_adress = pd.read_csv('ipAddress_to_Country.csv')
    df_ip_adress['lower_bound_ip_address'] = df_ip_adress['lower_bound_ip_address'].astype(int)

    df['ip_address'] = df['ip_address'].astype(int)
    
    ## Change datatypes to datetime
    df['signup_time'] = pd.to_datetime(df['signup_time'])
    df['purchase_time'] = pd.to_datetime(df['purchase_time'])

    ## Merge the df_id and df based on the ip_address 

    def ip_to_country(ip):
        ## Function to get country from ip
        try:
            return df_ip_adress.country[(df_ip_adress.lower_bound_ip_address < ip) & (df_ip_adress.upper_bound_ip_address > ip)].iloc[0]
        except IndexError:
            return "Unknown"   
    
    df['country'] = df['ip_address'].apply(ip_to_country)


    ## Extract time features
    df['month'] = df['purchase_time'].dt.month
    df['day'] = df['purchase_time'].dt.day
    df['weekday'] = df['purchase_time'].dt.weekday
    df['hour'] = df['purchase_time'].dt.hour

    ## Scaling
    columns_to_be_scaled = ['purchase_value', 'age','ip_address','velocity']
    scaler = MinMaxScaler()
    df[columns_to_be_scaled] = scaler.fit_transform(df[columns_to_be_scaled])

    ## One-Hot Encoding for categorical features
    categorical_features = ['source', 'browser', 'sex']

    # Perform One-Hot Encoding and drop the first category to avoid multicollinearity
    df = pd.get_dummies(df, columns=categorical_features, drop_first=True)

    ## Label encode the 'country' feature in the fraud datasets
    label_encoder = LabelEncoder()
    df['country'] = label_encoder.fit_transform(df['country'])

    ## Find the difference between signup and purchase time for fraud datasets
    df['signup_time'] = pd.to_datetime(df['signup_time'])
    df['purchase_time'] = pd.to_datetime(df['purchase_time'])
    df['time_difference'] = (df['purchase_time'] - df['signup_time']).dt.total_seconds()

    ## Scale the the time_difference column
    df['time_difference'] = scaler.fit_transform(df[['time_difference']])

    ## let's drop unwanted columns 
    df.drop(columns=['signup_time','purchase_time','ip_address'], inplace=True)

    columns = ['purchase_value','age','country','hour','month','day','weekday','frequency',
               'velocity','source_Direct','source_SEO','browser_FireFox','browser_IE','browser_Opera',
               'browser_Safari','sex_M','time_difference']
    for col in columns:
        if col not in df.columns:
            df[col] = 0 

    #reorder
    df = df[columns]

    return df


import pandas as pd
import numpy as np


def into_datetime(df):
    ## Change datatypes to datetime
    df['signup_time'] = pd.to_datetime(df['signup_time'])
    df['purchase_time'] = pd.to_datetime(df['purchase_time'])

def into_integer(df1, df2):
    ## Change datatypes to int
    ## Ip into integer format
    df1['ip_address'] = df1['ip_address'].astype(int)
    df2['lower_bound_ip_address'] = df2['lower_bound_ip_address'].astype(int)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def univariate_numerical(df):
    ## Univariate Analysis
    ## Plotting histogram for numerical columns
    columns = ['purchase_value', 'age']
    for col in columns:
        plt.figure(figsize=(10, 5))
        sns.histplot(df[col], kde=True, bins=20)
        plt.title(f'Histogram of {col}', fontweight='bold', fontsize=15)
        plt.xlabel(f'{col}', fontweight='bold', fontsize=12)
        plt.ylabel('count', fontweight='bold', fontsize=12)
        plt.show()

def univariate_categorical(df):
    ## Plotting barplot for categorical columns
    columns = ['source', 'browser','sex']
    for col in columns:
        plt.figure(figsize=(10, 5))
        sns.countplot(df[col])
        plt.title(f'Count plot of {col}', fontweight='bold')
        plt.xlabel(f'{col}', fontweight='bold', fontsize=12)
        plt.ylabel('count', fontweight='bold', fontsize=12)
        plt.show()

def bivariate_numerical(df):
    ## Bivariate Analysis
    ## Plotting scatter plot for numerical columns
    columns = ['purchase_value', 'age']
    for col in columns:
        plt.figure(figsize=(10, 5))
        sns.boxplot(y=col, x=df['class'], data=df)
        plt.title(f'Box plot of {col} vs class', fontweight='bold', fontsize=15)
        plt.xlabel('class', fontweight='bold', fontsize=12)
        plt.ylabel(f'{col}', fontweight='bold', fontsize=12)
        plt.show()

def bivariate_categorical(df):
    ## Plotting barplot for categorical columns
    columns = ['source', 'browser','sex']
    for col in columns:
        plt.figure(figsize=(10, 5))
        sns.countplot(x=df['class'], hue=col, data=df)
        plt.title(f'Count plot of {col} vs class', fontweight='bold', fontsize=15)
        plt.xlabel(f'{col}', fontweight='bold', fontsize=12)
        plt.ylabel('count', fontweight='bold', fontsize=12)
        plt.legend(prop={'weight': 'bold', 'size': 12}, labelcolor='purple')
        plt.show()
def correlation_matrix(df):
    ## Correlation matrix
    columns = ['purchase_value', 'age','class']
    plt.figure(figsize=(10, 5))
    sns.heatmap(df[columns].corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation matrix', fontweight='bold', fontsize=15)
    plt.show()
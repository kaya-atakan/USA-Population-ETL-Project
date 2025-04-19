import pandas as pd
import os

DATA_DIR = '/opt/airflow/dags/data'

def transform():
    df = pd.read_csv(f'{DATA_DIR}/raw_data.csv')
    df_clean = df[['Year', 'Population']].dropna()
    df_clean['Year'] = df_clean['Year'].astype(int)
    df_clean['Population'] = df_clean['Population'].astype(int)
    df_clean.to_csv(f'{DATA_DIR}/clean_data.csv', index=False)
import pandas as pd
import requests
import os

DATA_DIR = '/opt/airflow/dags/data'
# os.makedirs(DATA_DIR, exist_ok=True)

def extract():
    url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
    response = requests.get(url)
    data = response.json()['data']
    df = pd.DataFrame(data)
    df.to_csv(f'{DATA_DIR}/raw_data.csv', index=False)
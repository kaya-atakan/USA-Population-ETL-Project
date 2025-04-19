import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

import os
DATA_DIR = '/opt/airflow/dags/data'


output_path = f"{DATA_DIR}/population_trend.png"
if os.path.exists(output_path):
    os.remove(output_path)



DATA_DIR = '/opt/airflow/dags/data'

def visualize():
    df = pd.read_csv(f'{DATA_DIR}/clean_data.csv')
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Year', y='Population', data=df)

    # Set y-axis to start at 300 million
    plt.ylim(300_000_000, df['Population'].max() * 1.05)

    # Format y-axis ticks to display in millions with 'M'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x/1e6:.0f}M'))

    plt.title("US Population Over Time")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
# US Population ETL Project

This project is a simple ETL (Extract, Transform, Load) pipeline built with **Apache Airflow**, **Docker**, and **Python**.  
It fetches **US population data** from a public API, processes it, and generates a **trend visualization**.

---

## ✨ Features

- **Daily automated data extraction** from [DataUSA API](https://datausa.io/api/data?drilldowns=Nation&measures=Population)
- **Data cleaning and transformation** using `pandas`
- **Visualization** of US population trends using `seaborn`
- **Dockerized** setup for easy deployment
- **Apache Airflow DAG** to orchestrate the workflow

---

## 🚀 Getting Started


### 1. Set Up the Environment
```bash
git clone https://github.com/your-username/us-population-project.git
cd us-population-project
```
Make sure you have Docker and Docker Compose installed.

Check installation:
```bash
docker --version
docker compose version
```
### 2. Build and Start the Services
```bash

sudo docker compose up --build
```

This command will:

- Build the Airflow image

- Start the webserver, scheduler, and other Airflow components

### 3. Access Airflow UI

http://127.0.0.1:8080/

---


### 📈 How the Pipeline Works

**Extract Task**  
Fetches population data from the API and saves it to /dags/data/raw_data.csv.

<br>

**Transform Task**
Cleans and processes the raw data, saves it as /dags/data/clean_data.csv.

<br>

**Visualize Task**
Creates a bar plot of US population over time and saves it as /dags/data/population_trend.png.

The DAG runs daily without backfilling old runs (catchup=False).


### 🛠 Technologies Used

`Apache Airflow`

`Docker`

`Python 3.10`

`Pandas`

`Seaborn`

`Matplotlib`

### ⚡ Troubleshooting
Permission Errors
Make sure `/dags/data/` folder has writable permissions inside the Docker container.

Dependencies Not Found
Double-check your requirements.txt includes `pandas`, `requests`, `seaborn`, and `matplotlib`.

Stuck in Queued State
Run docker compose restart airflow to restart services after major changes.

### 📋 To-Do / Future Improvements

Store processed data in a database (PostgreSQL, etc.)

Add alerting for failed DAG runs

Improve visualization (e.g., dynamic labeling, interactivity)
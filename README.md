# data-integration-pipeline

# Data Integration Pipeline (API + ETL + Flask)

## 📌 Overview
This project demonstrates an end-to-end data integration pipeline that extracts real-time data from an external API, processes it, stores it in a database, and exposes it through a REST API.

## ⚙️ Features
- Extracts real-time data from an external API
- Stores data in a structured SQLite database
- Adds timestamps for tracking historical data
- Provides REST API endpoint to retrieve stored data
- Implements basic ETL (Extract, Transform, Load) workflow

## 🛠️ Technologies Used
- Python
- Flask (API development)
- SQLite (Database)
- Requests (API calls)

## 📂 Project Structure
data_pipeline_project/
│── main.py # Extract & load data
│── api.py # Flask API
│── database.py # Database logic
│── data.db # SQLite database
│── README.md


## How to Run the Project
1. Install dependencies
pip install flask requests
3. Run data pipeline
python3 main.py
4. Start API server
python3 api.py
5. Open in browser
http://127.0.0.1:5000/prices

Example Output
[
  {
    "id": 1,
    "price": "74021",
    "timestamp": "2026-04-15 11:05:00"
  }
]


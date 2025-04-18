# Retail Sales Data Engineering Pipeline

This project demonstrates a complete data engineering pipeline that simulates real-time point-of-sale (POS) transactions, streams them via Apache Kafka, processes them using Apache Spark Structured Streaming, stores the results in a PostgreSQL database, and visualizes them with Streamlit.

## Project Overview

The pipeline simulates the environment of a retail store. It includes:

- Data generation from a Kafka producer
- Real-time stream processing using Spark
- Storage of processed data in PostgreSQL
- Interactive dashboard for visualization using Streamlit

## Features

- Kafka producer that continuously generates fake retail sales transactions
- Apache Spark job that consumes the data stream and writes structured data to PostgreSQL
- PostgreSQL database to persist the data
- Streamlit dashboard to view sales data in real time

## Technologies Used

- Python 3.9
- Apache Kafka
- Apache Spark (Structured Streaming)
- PostgreSQL
- Streamlit
- Kafka-Python
- psycopg2
- PySpark

## Folder Structure

retail_sales_pipeline/
├── kafka/
│   └── producer.py                 # Simulates real-time sales data
├── spark_jobs/
│   └── stream_job.py              # Spark job to consume Kafka stream and write to PostgreSQL
├── frontend/
│   └── dashboard.py               # Streamlit app for visualizing retail sales
├── retail_env/                    # Virtual environment (excluded from version control)
└── requirements.txt               # Python dependencies

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.9
- Apache Kafka and Zookeeper
- Apache Spark
- PostgreSQL
- Git

### Environment Setup

1. Clone the repository:

git clone https://github.com/Ajith3569/Sales_Data_Engineering.git
cd Sales_Data_Engineering

2. Create and activate a virtual environment:

python3 -m venv retail_env
source retail_env/bin/activate

3. Install dependencies:

pip install -r requirements.txt

4. Start Kafka and Zookeeper:

zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties
kafka-server-start /opt/homebrew/etc/kafka/server.properties

5. Create a Kafka topic:

kafka-topics --create --topic retail_sales --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

6. Start the Kafka producer:

python kafka/producer.py

7. Run the Spark streaming job:

python spark_jobs/stream_job.py

8. Launch the Streamlit dashboard:

streamlit run frontend/dashboard.py

## Output Example

Once everything is running, you will:

- See simulated sales data sent to Kafka in your terminal
- Watch PostgreSQL table retail_sales_stream update in real time
- Interact with a live dashboard in your browser showing the latest sales activity

## Author

Ajith Kumar Dugyala

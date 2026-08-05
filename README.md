# Chicago Public Safety ETL

Chicago Public Safety ETL is a beginner-friendly data engineering project that uses Apache Airflow to manage an ETL pipeline. The pipeline collects public safety data from the City of Chicago, cleans and prepares the records, and loads the results into a PostgreSQL database.

## What Is ETL?

ETL stands for Extract, Transform, and Load:

1. **Extract** – Collect data from the source.
2. **Transform** – Clean the data and prepare it for storage.
3. **Load** – Insert the transformed data into PostgreSQL.

Apache Airflow schedules the pipeline and shows whether each run succeeds or fails.

## How the Project Works

1. Airflow starts the ETL task.
2. Python extracts the public safety records.
3. The pipeline cleans and transforms the records.
4. The processed data is loaded into PostgreSQL.
5. Airflow records the status and logs for the run.

Celery distributes Airflow tasks to a worker, while Redis acts as the message broker. Docker Compose starts each service in its own container.

## Technologies

- Python – ETL logic
- Apache Airflow – pipeline scheduling and monitoring
- PostgreSQL – data storage
- Docker and Docker Compose – containerized development environment
- Celery – task execution
- Redis – message broker

## Project Structure

```text
Chicago-Public-Safety-ETL/
├── dags/                  # Airflow DAG definitions
├── etl/                   # Extract, transform, and load code
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── etl.py
├── docker-compose.yaml    # Docker services and configuration
├── .env.example           # Example environment variables
├── .gitignore
└── README.md
```

## Requirements

Install the following before running the project:

- Git
- Docker Desktop
- Docker Compose

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/dobydev/Chicago-Public-Safety-ETL.git
cd Chicago-Public-Safety-ETL
```

### 2. Configure the environment

Create a `.env` file from `.env.example`, then update any required values for your local environment.

Do not commit the `.env` file because it may contain passwords or other sensitive settings.

### 3. Start the containers

```bash
docker compose up -d
```

### 4. Check the services

```bash
docker compose ps
```

Wait until the Airflow and PostgreSQL services report that they are healthy.

### 5. Open Airflow

Open the following address in a browser:

```text
http://localhost:8080
```

Find the `chicago_public_safety_etl` DAG, enable it if necessary, and trigger a new run.

## Viewing Logs

Airflow records a log for every task run. If a task fails, select the failed task in the Airflow interface and open its log to view the error.

You can also view the worker logs from the terminal:

```bash
docker compose logs --tail 150 airflow-worker
```

## Stopping the Project

```bash
docker compose down
```

## Project Goal

The goal of this project is to demonstrate a complete ETL workflow using tools commonly found in data engineering environments. It includes data extraction, transformation, database loading, workflow orchestration, containerization, task distribution, and pipeline monitoring.

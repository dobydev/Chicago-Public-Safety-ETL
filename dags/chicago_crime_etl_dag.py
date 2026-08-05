from datetime import datetime

from airflow.sdk import dag, task


@dag(
    dag_id="chicago_public_safety_etl",
    schedule=None,
    start_date=datetime(2026, 8, 1),
    catchup=False,
    tags=["etl", "chicago"],
)
def chicago_public_safety_etl():

    @task
    def run_chicago_etl():
        from etl.etl import ETLPipeline

        pipeline = ETLPipeline(limit=1000)
        processed_count = pipeline.run_pipeline()

        print(
            f"Airflow processed {processed_count} Chicago crime records."
        )

    run_chicago_etl()


chicago_public_safety_etl()
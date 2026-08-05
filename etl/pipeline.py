from etl.extract import extract_crime_data
from etl.transform import transform_crime_data
from etl.load import load_crime_data


class ETLPipeline:
    def __init__(self, limit=1000):
        self.limit = limit

    def run_pipeline(self):
        raw_records = extract_crime_data(limit=self.limit)
        cleaned_records = transform_crime_data(raw_records)
        load_crime_data(cleaned_records)

        print(
            f"ETL pipeline completed. "
            f"Processed {len(cleaned_records)} records."
        )

        return len(cleaned_records)


if __name__ == "__main__":
    pipeline = ETLPipeline(limit=1000)
    processed_records = pipeline.run_pipeline()
    processed_count = pipeline.run_pipeline()










import os
import psycopg
from dotenv import load_dotenv



# Load environment variables from .env file
load_dotenv()

# Method to load data into the PostgreSQL database
def load_crime_data(records):
    connection = psycopg.connect(
    host=os.getenv("CHICAGO_DB_HOST", "localhost"),
    port=os.getenv("CHICAGO_DB_PORT", "5432"),
    dbname=os.getenv("CHICAGO_DB_NAME"),
    user=os.getenv("CHICAGO_DB_USER"),
    password=os.getenv("CHICAGO_DB_PASSWORD"),
    )


# Query to insert records into the crime_incidents table with conflict handling
    insert_query = """
        INSERT INTO crime_incidents (
            incident_id,
            case_number,
            description,
            location_description,
            arrest_made,
            block,
            source_updated_at
        )
        VALUES (
            %(incident_id)s,
            %(case_number)s,
            %(description)s,
            %(location_description)s,
            %(arrest_made)s,
            %(block)s,
            %(updated_on)s
        )
        ON CONFLICT (incident_id) DO NOTHING;
    """

    with connection:
        with connection.cursor() as cursor:
            cursor.executemany(insert_query, records)

    connection.close()
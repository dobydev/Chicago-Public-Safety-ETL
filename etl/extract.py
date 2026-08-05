import requests

import json

API_URL = "https://data.cityofchicago.org/resource/ijzp-q8t2.json"

# Method to extract data from the API
def extract_crime_data(limit=1000):
    """
    Extracts crime data from the Chicago Data Portal API.

    Parameters:
        limit (int): The number of records to retrieve. Default is 1000.

    Returns:
        list: A list of crime records.
    """

    #Request parameters

    query_params = {
        "$select": (
            "id,"
            "case_number,"
            "date,"
            "block,"
            "description,"
            "location_description,"
            "arrest,"
            "updated_on"
        ),
        "$order": "updated_on DESC",
        "$limit": limit,
    }

    # Make the actual API request
    response = requests.get(API_URL, params=query_params, timeout=30)

    if not response.ok:
        print(response.text)
        response.raise_for_status()


    # Parse the JSON response as a Python list of dictionaries
    records = response.json()

   # Validate the response to ensure it is a list of records
    if not isinstance(records, list):
        raise ValueError("Expected a list of records, but got a different type.")

    print(f"\nExtracting {len(records)} records from the Chicago Data Portal API.....")

    print(f"\n{len(records)} have been successfully extracted from the Chicago Data Portal API.\n")

    return records
    
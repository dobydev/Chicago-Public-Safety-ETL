from datetime import datetime


def _parse_datetime(value):
    if not value:
        return None
    
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"

    return datetime.fromisoformat(value)


def transform_crime_data(records):
    transformed_records = []

    for record in records:
        transformed_record = {
            "incident_id": int(record["id"]),
            "case_number": record.get("case_number"),
            "date": _parse_datetime(record.get("date")),
            "description": record.get("description"),
            "location_description": record.get("location_description"),
            "arrest_made": bool(record.get("arrest", False)),
            "block": record.get("block"),
            "updated_on": _parse_datetime(record.get("updated_on")),
        }
        transformed_records.append(transformed_record)

    return transformed_records


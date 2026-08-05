CREATE TABLE IF NOT EXISTS crime_incidents(
	incident_id BIGINT PRIMARY KEY,
    case_number VARCHAR(20),
    block VARCHAR(150),
    description VARCHAR(255),
    location_description VARCHAR(150),
    arrest_made BOOLEAN NOT NULL DEFAULT FALSE,
    source_updated_at TIMESTAMP,
    loaded_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)
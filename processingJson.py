import sqlite3
import json
from datetime import datetime

# Database path
db_path = 'database/jsonStore.db'

def get_unprocessed_json():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, responseJson FROM rawJson WHERE processed_at IS NULL")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_processed_at(id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    current_time = datetime.now().isoformat()
    cursor.execute("UPDATE rawJson SET processed_at = ? WHERE id = ?", (current_time, id))
    conn.commit()
    conn.close()

def insert_json_into_FlightInfo(json_data):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Parse the JSON data and ignore the initial "data" key
    data = json.loads(json_data)["data"]

    # Flatten JSON and generate columns and values
    columns = []
    values = []

    def flatten_json(prefix, obj):
        for key, value in obj.items():
            if key == "additionalFlightInfo":       # Skip additionalFlightInfo to save space
                break
            if key == "flightState":
                columns.append(f"{prefix}{key}")
                values.append(value)
                continue
            if isinstance(value, dict):
                flatten_json(f"{prefix}{key}_", value)
            elif value is not None:  # Skip columns with null values
                columns.append(f"{prefix}{key}")
                values.append(value)

    flatten_json('', data)

    # Generate SQL query
    columns_str = ', '.join(columns)
    placeholders_str = ', '.join(['?'] * len(values))
    sql = f"INSERT INTO FlightInfo ({columns_str}) VALUES ({placeholders_str})"

    # Execute SQL query
    cursor.execute(sql, values)
    conn.commit()
    conn.close()

def main():
    try:
        rows = get_unprocessed_json()
        if rows:
            for row in rows:
                id, json_data = row
                insert_json_into_FlightInfo(json_data)
                update_processed_at(id)
                print(f"Data with id {id} inserted into FlightInfo table.")
        else:
            print("No unprocessed JSON data found in rawJson table.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

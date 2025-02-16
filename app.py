from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from validateEndPoint import validate_api_endpoint

import requests
import sqlite3

app = FastAPI()


# Function to create the database and table if they don't exist
def initialize_db():
    conn = sqlite3.connect('database/jsonStore.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rawJson (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            responseJson TEXT
        )
    ''')
    conn.commit()
    conn.close()


# Function to insert JSON response into the database
def insert_response_into_db(response_json):
    conn = sqlite3.connect('database/jsonStore.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO rawJson (responseJson) VALUES (?)
    ''', (response_json,))
    conn.commit()
    conn.close()


@app.on_event("startup")
async def startup_event():
    initialize_db()


@app.get("/flights")
async def get_flight_info(
        airline_code: str = Query(..., description="The IATA code for the airline"),
        flight_number: str = Query(..., description="The flight number"),
        date: str = Query(..., description="The date of the flight")
):
    url = f"https://www.flightstats.com/v2/api-next/flight-tracker/{airline_code}/{flight_number}/{date}"
    print(url)

    # Call the validation function
    is_valid = validate_api_endpoint(url)

    if is_valid:
        print("API endpoint is valid.")
    else:
        print("API endpoint is not valid.")

    response = requests.get(url)

    # Ensure the response is in JSON format
    try:
        flight_data = response.json()
    except ValueError:
        return JSONResponse(content={"error": "Invalid response format"}, status_code=500)

    # Insert response into the database
    insert_response_into_db(response.text)

    return JSONResponse(content=flight_data)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

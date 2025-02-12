from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

@app.get("/flights")
async def get_flight_info(
        airline_code: str = Query(..., description="The IATA code for the airline"),
        flight_number: str = Query(..., description="The flight number"),
        year: int = Query(..., description="The year of the flight"),
        month: int = Query(..., description="The month of the flight"),
        date: int = Query(..., description="The date of the flight")
):
    url = f"https://www.flightstats.com/v2/api-next/flight-tracker/{airline_code}/{flight_number}/{year}/{month}/{date}"
    print(url)
    response = requests.get(url)

    # Ensure the response is in JSON format
    try:
        flight_data = response.json()
    except ValueError:
        return JSONResponse(content={"error": "Invalid response format"}, status_code=500)

    return JSONResponse(content=flight_data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

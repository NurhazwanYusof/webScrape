# WebScrape - Quick manual
```commandline
 Required - Python 3.6.5
```
```commandline
This README contains 2 section
1) Web Scraping with FastAPI
2) processingJson.py
```

URL sample for request

`https://www.flightstats.com/v2/api-next/flight-tracker/{airline_code}/{flight_number}/{year}/{month}/{date}` \

Example: `https://www.flightstats.com/v2/api-next/flight-tracker/IB/351/2025/2/12`

-----------------------------------------------
Internal API GET request \
`http://127.0.0.1:8000/flights?airline_code={airline_code}&flight_number={flight_number}&date={date}` \
Example: `http://127.0.0.1:8000/flights?airline_code=IB&flight_number=351&date=2025/2/12`

---------------------------------------
# 1) Web Scraping with FastAPI - Overview
This Python script uses FastAPI to create an API endpoint for performing web scraping. The endpoint accepts GET parameters: airline code, airline number, and departure date. The script retrieves flight information based on these parameters and returns the scraped data.

Requirements
```python
Python 3.6.5

Required Python libraries:
fastapi
uvicorn
requests
```

You can install the required libraries using the following command:

```bash
pip install fastapi uvicorn requests
````
Script Description
1. Configuration
   The script starts by configuring the FastAPI app and importing the necessary libraries.

2. API Endpoint
   The script defines an API endpoint /scrape_flight_info that accepts the following GET parameters:

airline_code: The code of the airline (e.g., "AA" for American Airlines).

flight_number: The flight number (e.g., "100").

departure_date: The departure date in YYYY/MM/DD format (e.g., "2025/02/16").

3. Web Scraping
   The script uses the requests library to fetch the JSON content to parse and extract relevant flight information.
```commandline
DB location & location: database/jsonStore.db

Table Name:
rawJson - storing raw Json file for temporary storage
FlightInfo - strorin the file in a DB table format
```

4Response
   The script returns the scraped flight information in JSON format.

Usage
Ensure that you have the required libraries installed.

Run the FastAPI app using the following command:

bash
```commandline
uvicorn main:app --reload
```
Access the API endpoint by navigating to the following URL in your web browser or using a tool like Postman:

```commandline
http://127.0.0.1:8000/scrape_flight_info?airline_code=AA&flight_number=100&departure_date=2025/02/16
```

```commandline
Notes
- Ensure that the URL used for scraping (https://example.com/flights) is replaced with the actual URL of the website you want to scrape.
- Modify the script as needed to handle different structures or additional fields in the scraped data.
```



------

# 2) processingJson.py - Overview
The processingJson.py script retrieves JSON data from the rawJson table, flattens the JSON structure, and inserts the processed data into the FlightInfo table. This script automates the extraction, transformation, and loading (ETL) process for JSON data handling in our SQLite database.

# Requirements
Python 3.6.5

Required Python libraries:
```python
sqlite3
json
```


You can install any missing libraries using the following command:

bash
```commandline
pip install sqlite3 json
```
Script Description
1. Configuration -
   The script starts by configuring the database connection details and importing the necessary libraries.

2. Fetching JSON Data - 
   The script connects to the SQLite database and retrieves the JSON data from the rawJson table.

3. Flattening JSON Data - 
   Using the json library, the script flattens the JSON structure to transform nested JSON objects into a tabular format.

4. Inserting Data into FlightInfo Table - 
   The flattened data is then inserted into the FlightInfo table in the SQLite database.

Usage - 
Ensure that you have the required libraries installed.

Update the database connection details in the script to match your database configuration.


Run the script using the following command:
```commandline
python processingJson.py
```
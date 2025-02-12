# webScrape
# Python 3.6.5

URL sample for request 

`https://www.flightstats.com/v2/api-next/flight-tracker/{airline_code}/{flight_number}/{year}/{month}/{date}` \

Example: `https://www.flightstats.com/v2/api-next/flight-tracker/IB/351/2025/2/12`

-----------------------------------------------
Internal API GET request \
`http://127.0.0.1:8000/flights?airline_code={airline_code}&flight_number={flight_number}&year={year}&month={month}&date={date}` \
Example: `http://127.0.0.1:8000/flights?airline_code=IB&flight_number=351&year=2025&month=2&date=12`

---------------------------------------
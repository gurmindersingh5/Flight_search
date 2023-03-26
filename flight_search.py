import requests
from flight_data import FlightData
import time

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = "Dyzt9T2jAFd6d4EidfkejW8H1qtyOkK5"


class FlightSearch:

    # def get_destination_code(self, city_name):
    #     location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
    #     headers = {"apikey": TEQUILA_API_KEY}
    #     query = {"term": city_name, "location_types": "city"}
    #     response = requests.get(url=location_endpoint, headers=headers, params=query)
    #     results = response.json()["locations"]
    #     code = results[0]["code"]
    #     print( code)

    def check_flights(self, from_time, to_time, origin_city_code="DEL", destination_city_code="YYZ"):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "flight_type": "oneway",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "CAD",
            "sort": "price",
            "limit": 3

        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            out_time=data["route"][0]["local_departure"].split("T")[1].split(".")[0],
            arival_date=data["route"][0]["local_arrival"].split("T")[0],
            arival_time=data["route"][0]["local_arrival"].split("T")[1].split(".")[0],
            link=data["deep_link"]

        )
        print(f"{flight_data.destination_city}: CAD: {flight_data.price} \n {flight_data.out_date} , {flight_data.out_time}")
        print(flight_data.link)
        return flight_data

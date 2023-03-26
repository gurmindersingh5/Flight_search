from data_manager import DataManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

# if sheet_data[0]["iataCode"] == "":
#     from flight_search import FlightSearch
#     flight_search = FlightSearch()
#     for row in sheet_data:
#         row["iataCode"] = flight_search.get_destination_code(row["city"])
#     print(f"sheet_data:\n {sheet_data}")
#     data_manager.destination_data = sheet_data
#     data_manager.update_destination_codes()

from flight_search import FlightSearch
flight_search = FlightSearch()
from datetime import datetime, timedelta
from notification_manager import NotificationManager
notification_manager = NotificationManager()

tomorrow = datetime.now() + timedelta(days=1)
lastday = datetime.now() + timedelta(days=40)


for destination in sheet_data:
    flight = flight_search.check_flights(
        from_time=tomorrow,
        to_time=lastday,
    )
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.arival_date}."
        )
        # users = data_manager.get_customer_emails()
        # emails = [row["email"] for row in users]
        # names = [row["firstName"] for row in users]
        message = f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.arival_date}."
        link = "link here"

        notification_manager.send_emails(message, link)
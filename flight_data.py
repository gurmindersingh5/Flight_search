class FlightData:

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, out_time, arival_date, arival_time, link):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.out_time = out_time
        self.arival_date = arival_date
        self.arival_time = arival_time
        self.link = link
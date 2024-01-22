import pandas as pd

filepath = "hotels.csv"
df = pd.read_csv(filepath, dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id_local):
        self.hotel_id = hotel_id_local
        self.name = df.loc[df["id"] == self.hotel_id, "name"]

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv(filepath, index=False)
        print("Hotel Booked!")

    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name_local, hotel_object):
        self.customer_name = customer_name_local
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for booking with us!
        Customer Name: {self.customer_name}
        Hotel: {self.hotel.name}
"""
        return content


print(df)
hotel_id = input("Enter hotel ID: ")
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(customer_name_local=name, hotel_object=hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is unavailable.")

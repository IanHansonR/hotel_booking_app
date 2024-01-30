import pandas as pd

filepath = "hotels.csv"
df = pd.read_csv(filepath, dtype={"id": str})
df_card = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_secure_card = pd.read_csv("card_security.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_id_local):
        self.hotel_id = hotel_id_local
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv(filepath, index=False)
        print("Hotel Reserved.")

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
        Hotel: {self.hotel.name}"""
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration, "holder": holder, "cvc": cvc}
        if card_data in df_card:
            print("Payment Pending")
            return True
        else:
            print("Invalid Payment. Please try another.")
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_secure_card.loc[df_secure_card["number"] == "1234567890123456", "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False





print(df)
hotel_id = input("Enter hotel ID: ")
hotel = Hotel(hotel_id)

if hotel.available():
    credit_card = SecureCreditCard(number="1234567890123456")
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        given_password = input("Enter authentication password: ")
        if credit_card.authenticate(given_password=given_password):
            name = input("Enter your name: ")
            print("Card Authenticated.")
            hotel.book()
            reservation_ticket = ReservationTicket(customer_name_local=name, hotel_object=hotel)
            print(reservation_ticket.generate())
        else:
            print("Card Authentication Failed.")
    else:
        print("Card Verification Failed.")
else:
    print("Hotel is unavailable.")

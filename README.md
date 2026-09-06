```python
class MovieBookingSystem:
    def __init__(self):
        self.data = {}

    def create_booking(self, booking_id, customer_name, movie_name, tickets):
        if booking_id in self.data:
            raise ValueError("Booking already exists")

        self.data[booking_id] = {
            "customer_name": customer_name,
            "movie_name": movie_name,
            "tickets": tickets,
            "status": "Booked"
        }

        return self.data

    def update_tickets(self, booking_id, new_ticket_count):
        if booking_id not in self.data:
            raise KeyError("Booking not found")

        self.data[booking_id]["tickets"] = new_ticket_count

        return self.data

    def get_booking_details(self, booking_id):
        if booking_id not in self.data:
            raise KeyError("Booking not found")

        return self.data[booking_id]

    def get_group_bookings(self, minimum_tickets):
        return [
            bid for bid, info in self.data.items()
            if info["tickets"] >= minimum_tickets
        ]
```

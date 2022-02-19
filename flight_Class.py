class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_pass(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


F = Flight(3)
people = ["Harry", "John", "Justin", "Pran"]
for cust in people:
    success = F.add_pass(cust)
    if success:
        print(f"Added {cust} in the flight successfully.")
    else:
        print(f"Flight is totally booked, No seats available for {cust}")


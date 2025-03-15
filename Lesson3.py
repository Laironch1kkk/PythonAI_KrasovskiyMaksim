class Human:
    def __init__(self, name="Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers is {self.brand}")

nick = Human("Nick")
kate = Human("Kate")
car = Auto("Mercedes")

car.add_passenger(nick)
car.add_passenger(kate)
car.print_passengers_names()



Vlod = Human("Vlod")
Second_Mops = Human("Second Mops")
Mops = Human("Mops")
Maksim = Human("Maksim")
Fedya = Human("Fedya")
car = Auto("Audio")
car.add_passenger(Vlod)
car.add_passenger(Second_Mops)
car.add_passenger(Mops)
car.add_passenger(Maksim)
car.add_passenger(Fedya)
car.print_passengers_names()



class Vehicle:
    def __init__(self, name):
        self.name = name


class Car(Vehicle):
    def move(self):
        return f"{self.name} is Driving 🚗"


class Plane(Vehicle):
    def move(self):
        return f"{self.name} is Flying ✈️"


class Boat(Vehicle):
    def move(self):
        return f"{self.name} is Sailing 🚤"


# Example usage
if __name__ == "__main__":
    car = Car("Toyota")
    plane = Plane("Boeing 747")
    boat = Boat("Yacht")

    print(car.move())
    print(plane.move())
    print(boat.move()) 
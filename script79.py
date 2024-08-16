class Car:
    def __init__(self, make, model, year, speed=0):
        self._make = make
        self._model = model
        self._year = year
        self._speed = speed

    # Getter method for 'make'
    @property
    def make(self):
        return self._make

    # Setter method for 'make'
    @make.setter
    def make(self, value):
        if isinstance(value, str):
            self._make = value
        else:
            raise ValueError("Make must be a string")

    # Getter method for 'model'
    @property
    def model(self):
        return self._model

    # Setter method for 'model'
    @model.setter
    def model(self, value):
        if isinstance(value, str):
            self._model = value
        else:
            raise ValueError("Model must be a string")

    # Getter method for 'year'
    @property
    def year(self):
        return self._year

    # Setter method for 'year'
    @year.setter
    def year(self, value):
        if isinstance(value, int) and 1886 <= value <= 2024:
            self._year = value
        else:
            raise ValueError("Year must be an integer between 1886 and 2024")

    # Getter method for 'speed'
    @property
    def speed(self):
        return self._speed

    # Setter method for 'speed'
    @speed.setter
    def speed(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._speed = value
        else:
            raise ValueError("Speed must be a non-negative number")

    # Method to accelerate the car
    def accelerate(self, amount):
        self.speed += amount

    # Method to brake the car
    def brake(self, amount):
        if self.speed - amount >= 0:
            self.speed -= amount
        else:
            self.speed = 0

# Example usage
car = Car(make="Toyota", model="Camry", year=2020)

print(car.make)   # Output: Toyota
print(car.model)  # Output: Camry
print(car.year)   # Output: 2020
print(car.speed)  # Output: 0

car.accelerate(50)
print(car.speed)  # Output: 50

car.brake(20)
print(car.speed)  # Output: 30

car.year = 2023  # Update the year
print(car.year)   # Output: 2023

# Trying to set an invalid year
try:
    car.year = 1800
except ValueError as e:
    print(e)  # Output: Year must be an integer between 1886 and 2024

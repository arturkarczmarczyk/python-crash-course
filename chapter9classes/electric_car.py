from car import Car

class ElectricCar(Car):
    """Represents an electric car"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)

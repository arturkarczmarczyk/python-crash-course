from car import Car
from electric_car import ElectricCar

tesla = ElectricCar('tesla', 'model s', 2019)
tesla.increase_odometer(50)
print(tesla.get_descriptive_name())

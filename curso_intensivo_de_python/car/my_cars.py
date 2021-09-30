from car import Car
from eletric_car import EletricCar

my_beetle = Car('volkswagen', 'bettle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = EletricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

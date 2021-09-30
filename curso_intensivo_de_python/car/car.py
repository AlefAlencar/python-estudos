class Car:
    """Uma tentativa simples de representar um carro."""
    def __init__(self, make, model, year):
        """Inicializa os atributos que descrevem um carro."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Devolve um nome descritivo, formatado de modo elegante."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem o carro."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Define o valor de leitura do hodômetro ccom o valor especificado."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def incremet_odometer(self, miles):
        """Soma a quantidade específica ao valor de leitura do hodômetro."""
        self.odometer_reading += miles


'''class Battery:
    """Uma tentativa simples de modelar uma bateria para um carro elétrico."""

    def __init__(self, battery_size=70):
        """Inicializa os atributos da bateria."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria."""
        print(f"This car has a {self.battery_size}kWh battery.")

    def get_range(self):
        """Exibe uma frase sobre a distância que o carro é capaz de percorrer com essa bateria."""
        battery_range = 0
        if self.battery_size == 70:
            battery_range = 240
        elif self.battery_size == 85:
            battery_range = 270

        message = f'This car can go aproximately {battery_range} miles on a full charge.'
        print(message)


class EletricCar(Car):
    """Representa aspectos específicos de veículos elétricos"""
    def __init__(self, make, model, year):
        """Inicializa os atributos da classe-pai"""
        super().__init__(make, model, year)
        self.battery = Battery()
'''

'''print('#Carros')
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.incremet_odometer(100)
my_used_car.read_odometer()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23  # modificando diretamente o atributo por meio de uma instância
my_new_car.update_odometer(59)  # modificando através de um método que trata a atualização internamente
my_new_car.read_odometer()

print('#Carros elétricos')
my_tesla = EletricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
'''

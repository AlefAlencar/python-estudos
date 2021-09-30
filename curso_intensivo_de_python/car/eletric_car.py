from car import Car


class Battery:
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

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class EletricCar(Car):
    """Representa aspectos específicos de veículos elétricos"""
    def __init__(self, make, model, year):
        """Inicializa os atributos da classe-pai"""
        super().__init__(make, model, year)
        self.battery = Battery()


'''EXERCÍCIO ANTERIOR
my_gurgel = EletricCar('brazil', 'itaipu', 1970)
my_gurgel.get_descriptive_name()
my_gurgel.battery.get_range()
my_gurgel.battery.upgrade_battery()
my_gurgel.battery.get_range()
'''
# RESTAURANTE
# criando uma classe (é como um "bloco modelo")
class Restaurant:
    # método inicialização
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The {self.restaurant_name.title()}'s cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The {self.restaurant_name.title()} is OPEN.")

    def set_number_served(self, set_number):
        self.number_served = set_number

    def increment_number_served(self, increment):
        self.number_served += increment
        print(f"In this day, we served {increment} persons.")

    def show_number_served(self):
        print(f"This restaurant has served a total of {self.number_served} persons.")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):  # representa aspectos específicos
        super().__init__(restaurant_name, cuisine_type)  # inicializa os atributos da classe-pai
        self.flavors = ['vanilla', 'chocolate', 'matcha', 'coconut', 'strawberry']

    def show_flavors(self):
        for n, flavor in enumerate(self.flavors):
            print(f'{n+1}º flavor: {flavor}')


# PROGRAMA
# criando uma instância [a partir da classe ("bloco modelo") 'Restaurant']
# 9.1 Restaurantes
print('\n#9.1 Restaurante')
restaurant = Restaurant('alefood', 'brazilian')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
# 9.2 Três restaurantes
print('\n#9.3 Três restaurantes')
restaurant_01 = Restaurant('penny', 'american')
restaurant_02 = Restaurant('scarlett', 'russian')
restaurant_03 = Restaurant('gadot', 'israeli')
restaurant_01.describe_restaurant()
restaurant_02.describe_restaurant()
restaurant_03.describe_restaurant()

# 9.4 Pessoas atendidas
print('\n#9.4 Pessoas atendidas')
restaurant94 = Restaurant('zecao', 'caipira')
restaurant94.describe_restaurant()
restaurant94.open_restaurant()
restaurant94.show_number_served()
restaurant94.set_number_served(5)
restaurant94.show_number_served()
restaurant94.increment_number_served(3)
restaurant94.show_number_served()

# 9.6 Sorveteria
print('#9.6 Sorveteria')
# criar instância
icecream_stand = IceCreamStand('IceCreampie', 'icecream')
# mostrar a "sorveteria"
icecream_stand.describe_restaurant()
# chamar método da instância
icecream_stand.show_flavors()

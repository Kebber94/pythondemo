##### Imports #####
from Kaffemaskinen.drink import Drink, DrinkSizes

##### Classes ######
class CoffeMachine:
    def __init__(self):
        self.__drink_list = []

    def create_drink(self, drinkName, drinkSize, with_cream):
        self.__drink_list.append(Drink(drinkName, drinkSize, with_cream))

        return Drink(drink_name, drink_size, with_cream)


drink1 = Drink("Latte", DrinkSize.MEDIUM, True)

print(f'{latte.get_drink()}')


def ShowDrinks():

def EditDrink():

def DeleteDrink():




print('\n==== Kaffemaskinen ====\n'
      '1. Opret drink\n'
      '2. Vis drikke\n'
      '3. Rediger drik\n'
      '4. Slet drik\n'
      '5. Afslut')
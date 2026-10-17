from enum import Enum
from xmlrpc.client import boolean


"##### Variables: #####"
class Drink(Enum):
all_drinks = []


"##### Classes: #####"
class DrinkSize(Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"

class Drink:

    def __init__(self, DrinkName, DrinkSize, WithCream):
        self.__DrinkName = DrinkName
        self.__DrinkSize = DrinkSize
        self.__WithCream = WithCream

    def

    @property
    def get_drink(self):
        return self.__DrinkName + self.__DrinkSize + self.__WithCream



"##### Definitions: #####"
def CreateDrink():
    drink_name = input("Hvad hedder denne drik?: ")
    drink_size = input("Hvilken størrelse? (small, medium, large): ")
    with_cream = boolean(input("Skal den være med flødeskum (J)a/(N)ej: "))

    return Drink(drink_name, drink_size, with_cream)

CreateDrink()

##### Imports #####
from enum import Enum

##### Classes: #####
class DrinkSizes(Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"


class Drink:
    def __init__(self, drinkName, drinkSize, with_cream):
        if not isinstance(drinkName, str) or len(drinkName) < 3:
            raise ValueError(f'{drinkName} er ikke en gyldig DrinkName-værdi')
        else:
            self.__DrinkName = drinkName

        if isinstance(drinkSize, DrinkSizes):
            self.__DrinkSize = drinkSize
        else:
            raise ValueError(f'{drinkSize} er ikke en gyldig DrinkSizes-værdi')

        if isinstance(with_cream, bool):
            self.__WithCream = with_cream
        else:
            raise ValueError(f'{with_cream} er ikke en gyldig værdi. Brug True eller False')

    def get_drink(self):
        if self.__WithCream:
            cream = "Ja"
        else:
            cream = "Nej"

        return self.__DrinkName, self.__DrinkSize.value, cream

    def set_name(self, new_name):
        if not isinstance(new_name, str) or len(new_name) < 3:
            raise ValueError(f'{new_name} er ikke en gyldig DrinkName-værdi')
        else:
            self.__DrinkName = new_name

    def set_size(self, new_size):
        if isinstance(new_size, DrinkSizes):
            self.__DrinkSize = new_size
        else:
            raise ValueError(f'{new_size} er ikke en gyldig DrinkSizes-værdi')

    def set_cream(self, new_cream):
        if isinstance(new_cream, bool):
            self.__WithCream = new_cream
        else:
            raise ValueError(f'{new_cream} er ikke en gyldig værdi. Brug True eller False')
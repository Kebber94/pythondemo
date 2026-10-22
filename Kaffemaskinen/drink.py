##### Imports #####
from enum import Enum

##### Classes: #####
class DrinkSizes(str, Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"


class Drink:
    def __init__(self, drink_name, drink_size, with_cream):
        if not isinstance(drink_name, str) or len(drink_name) < 3:
            raise ValueError(f'{drink_name} er ikke en gyldig DrinkName-værdi')
        else:
            self.__drink_name = drink_name

        if isinstance(drink_size, DrinkSizes):
            self.__drink_size = drink_size
        else:
            raise ValueError(f'{drink_size} er ikke en gyldig DrinkSizes-værdi')

        if isinstance(with_cream, bool):
            self.__with_cream = with_cream
        else:
            raise ValueError(f'{with_cream} er ikke en gyldig værdi. Brug True eller False')

    def get_drink(self):
        if self.__with_cream:
            cream = "Ja"
        else:
            cream = "Nej"

        return self.__drink_name, self.__drink_size.value, cream

    def set_name(self, new_name):
        if not isinstance(new_name, str) or len(new_name) < 3:
            raise ValueError(f'{new_name} er ikke en gyldig DrinkName-værdi')
        else:
            self.__drink_name = new_name

    def set_size(self, new_size):
        if isinstance(new_size, DrinkSizes):
            self.__drink_size = new_size
        else:
            raise ValueError(f'{new_size} er ikke en gyldig DrinkSizes-værdi')

    def set_cream(self, new_cream):
        if isinstance(new_cream, bool):
            self.__with_cream = new_cream
        else:
            raise ValueError(f'{new_cream} er ikke en gyldig værdi. Brug True eller False')
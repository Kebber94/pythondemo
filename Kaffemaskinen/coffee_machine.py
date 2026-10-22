##### Imports #####
from Kaffemaskinen.drink import Drink

##### Classes ######
class CoffeeMachine:
    def __init__(self):
        self.__drink_list = []

    def create_drink(self, drink_name, drink_size, with_cream):
        self.__drink_list.append(Drink(drink_name, drink_size, with_cream))

    def get_drinks(self):
        return self.__drink_list.copy()

    def is_valid_index(self, drink_number):
        # Returnerer True eller False, afhængigt af om index findes i maskinens liste
        return isinstance(drink_number, int) and 0 <= drink_number < len(self.__drink_list)

    def update_drink_name(self, drink_number, new_drink_name):
        if self.is_valid_index(drink_number):
            self.__drink_list[drink_number].set_name(new_drink_name)
        else:
            raise ValueError(f'{drink_number} is an invalid drink')

    def update_drink_size(self, drink_number, new_drink_size):
        if self.is_valid_index(drink_number):
            self.__drink_list[drink_number].set_size(new_drink_size)
        else:
            raise ValueError(f'{drink_number} is an invalid drink')

    def update_drink_cream(self, drink_number, new_drink_cream):
        if self.is_valid_index(drink_number):
            self.__drink_list[drink_number].set_cream(new_drink_cream)
        else:
            raise ValueError(f'{drink_number} is an invalid drink')

    def delete_drink(self, drink_number):
        if self.is_valid_index(drink_number):
            return self.__drink_list.pop(drink_number)
        else:
            raise ValueError(f'{drink_number} is an invalid drink')

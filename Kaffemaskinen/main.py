##### Imports #####
from Kaffemaskinen.coffee_machine import CoffeeMachine
from Kaffemaskinen.drink import DrinkSizes

##### Definitions #####
#** Input validations **#
def validate_drink_name(drink_name):
      return len(drink_name) >= 3

def validate_drink_size(drink_size):
      match drink_size.upper():
            case "S" | "SMALL":
                  return DrinkSizes.SMALL
            case "M" | "MEDIUM":
                  return DrinkSizes.MEDIUM
            case "L" | "LARGE":
                  return DrinkSizes.LARGE
            case _:
                  return None

def validate_drink_cream(drink_cream):
      match drink_cream.upper():
            case "J" | "JA":
                  return True
            case "N" | "NEJ":
                  return False
            case _:
                  return None

#** Other **#
def get_drink_name():
    while True:
        drink_name = input('Hvilken drink ønsker du?: ')

        if validate_drink_name(drink_name):
            return drink_name
        else:
            print('Ugyldigt navn. Prøv igen...')

def get_drink_size():
    while True:
          drink_size = input('Hvilken størrelse ønsker du? (S/M/L): ')

          drink_size = validate_drink_size(drink_size)

          if drink_size is not None:
                return drink_size
          else:
                print('Ugyldig størrelse. Angiv S, L eller M. Prøv igen...')

def get_drink_cream():
      while True:
            drink_cream = input('Ønsker du flødeskum? J/N: ')

            drink_cream = validate_drink_cream(drink_cream)

            if drink_cream is not None:
                  return drink_cream
            else:
                  print(f'Ugyldig indtastning. Skriv (J)a eller (N)ej. Prøv igen...')

def get_drink_number():
    while True:
        try:
            drink_number = int(input('\nVælg nummeret på en drink: ')) - 1
            return drink_number
        except ValueError:
            print('Du skal indtaste et gyldigt tal! Prøv igen...')

def create_drink(machine):
      drink_name = (get_drink_name()).capitalize()
      drink_size = get_drink_size()
      drink_cream = get_drink_cream()

      try:
            machine.create_drink(drink_name, drink_size, drink_cream)

            if drink_cream:
                  cream = "Ja"
            else:
                  cream = "Nej"

            print(f'\n{drink_name} | {drink_size.value} | Flødeskum: {cream} - blev oprettet.')

      except ValueError:
            print('Der opstod en fejl under oprettelsen. Prøv igen...')

def show_drinks(machine):
      drinks = machine.get_drinks()

      if drinks:
            for index, drink in enumerate(drinks, start=1):
                  name, size, cream = drink.get_drink()
                  print(f'[{index}]  Navn: {name} | Størrelse: {size} | Flødeskum: {cream}')
      else:
            print('Maskinen har ikke oprettet nogle drikke endnu.')


def edit_drink(machine):
      drinks = machine.get_drinks()

      if drinks:
            print('Du er ved at ændre en drik.\n')
            show_drinks(machine)

            drink_number = get_drink_number()

            if machine.is_valid_index(drink_number):
                  drink_name = get_drink_name()
                  drink_size = get_drink_size()
                  drink_cream = get_drink_cream()

                  machine.update_drink_name(drink_number, drink_name)
                  machine.update_drink_size(drink_number, drink_size)
                  machine.update_drink_cream(drink_number, drink_cream)

                  print('\nDrikken blev ændret succesfuldt.')
            else:
                  print('Ugyldig indtastning. Afslutter...')


def delete_drink(machine):
      show_drinks(machine)
      drink_number = get_drink_number()

      if machine.is_valid_index(drink_number):
            deleted_drink = machine.delete_drink(drink_number)

            name, size, cream = deleted_drink.get_drink()

            print(f'Følgende drik er blevet slettet: {name} | {size} | Flødeskum: {cream}')
      else:
            print('Ugyldig indtastning. Afslutter...')


def main():
      machine = CoffeeMachine()

      while True:
            print('\n==== Kaffemaskinen ====\n'
                           '1. Opret drink\n'
                           '2. Vis drikke\n'
                           '3. Rediger drik\n'
                           '4. Slet drik\n'
                           '5. Afslut\n')
            try:
                  choice = int(input('Vælg et nummer: '))
                  #print('\n')
            except ValueError:
                  print('Du skal indtaste et tal fra menuen!')
                  continue

            if 0 < choice < 6:
                  match choice:
                        case 1:
                              create_drink(machine)
                        case 2:
                              show_drinks(machine)
                        case 3:
                              edit_drink(machine)
                        case 4:
                              delete_drink(machine)
                        case 5:
                              break
            else:
                  print('Ugyldig indtastning. Prøv igen...')


##### Start #####
if __name__ == "__main__":
    main()
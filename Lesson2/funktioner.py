
def def_greeting(name):
    print("Hej", name)
    print("I dag lærer vi om funktioner!")
    print("På det her kursus skal man være over 18 år")

    alder = int(input("Hvor gammel er du?: "))

    if alder >= 18:
        print("Du er voksen og må gerne være her\n")
    elif alder < 18:
        print("Du er ikke voksen!\n")


def def_height(height):
    if height >= 190:
        print("Shit du er høj mand!")
    elif height >= 150:
        print("Din højde er normal")
    else:
        print("Hvad så bette skid")


def_greeting("Louise")
def_height(100)


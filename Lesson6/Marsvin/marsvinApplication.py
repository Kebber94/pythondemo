from Lesson6.Marsvin.model import bur
from Lesson6.Marsvin.model.Race import Race
from Lesson6.Marsvin.model.bur import Bur
from Lesson6.Marsvin.model.marsvin import Marsvin
from Lesson6.Marsvin.service.FileHaandtering import FilHaandtering

bur1 = Bur(1)
bur2 = Bur(2)
bur3 = Bur(3)



def vaelg_bur():

    print("Vælg bur:")
    print("1. Bur 1")
    print("2. Bur 2")
    print("3. Bur 3")

    bur_nummer = int(input("Bur nummer: "))

    if bur_nummer == 1:
        return bur1

    elif bur_nummer == 2:
        return bur2

    elif bur_nummer == 3:
        return bur3

    return None



def main():

    while True:

        print("\n----- Marsvin Menu -----")
        print("1. Opret marsvin")
        print("2. Vis alle marsvin")
        print("3. Opdater marsvin")
        print("4. Slet marsvin")
        print("5. Sorter marsvin")
        print("6. Gem til fil")
        print("7. Læs fra fil")
        print("0. Afslut")

        valg = input("Vælg menu: ")

        match valg:

            case "1":
                try:
                    navn = input("Navn: ")
                    alder = int(input("Alder: "))
                    vaegt = float(input("Vægt: "))
                    print("Vælg race:")
                    print("1. TEDDY")
                    print("2. SHELTIE")
                    print("3. ABYSSINIER")

                    race = Race(int(input("Race: ")))

                    marsvin = Marsvin(navn, alder, vaegt, race)


                    bur = vaelg_bur()

                    if bur is None:
                        print("Ugyldigt bur")
                    else:
                        bur.tilfoej_marsvin(marsvin)

                    print("Marsvin oprettet")
                except ValueError:
                    print("Forkert input")

            case "2":
                bur = vaelg_bur()

                if bur is None:
                    print("Ugyldigt bur")
                else:
                    bur.vis_alle_marsvin()

                print("Vi alle marsvin i bur")


            case "3":
                navn = input("Hvilket marsvin vil du opdatere? ")
                ny_alder = int(input("Ny alder: "))

                bur = vaelg_bur()
                if bur is None:
                    print("Ugyldigt bur")
                else:
                    bur.opdater_marsvin_navn(navn)

                print("Marsvin opdateret")

            case "4":
                navn = input("Hvilket marsvin vil du slette? ")
                bur = vaelg_bur()
                if bur is None:
                    print("Ugyldigt bur")
                else:
                    bur.slet_marsvin(navn)


                print("Marsvin slettet")

            case "5":
                bur = vaelg_bur()
                if bur is None:
                    print("Ugyldigt bur")
                else:
                    bur.sorter_efter_navn()


                print("Marsvin sorteret efter navn")

            case "6":

                alle_marsvin = []

                for bur in [bur1, bur2, bur3]:
                    alle_marsvin.extend(
                        bur.get_marsvin_liste()
                    )

                FilHaandtering.gem_til_fil(alle_marsvin)

                print("Alle marsvin gemt til fil")

            case "7":

                marsvin_liste = FilHaandtering.laes_fra_fil()

                for marsvin in marsvin_liste:
                    print(marsvin)

            case "0":
                print("Program afsluttes...")
                break

            case _:
                print("Ugyldigt valg")

if __name__ == "__main__":
        main()

"""
#Trin 2: Test getters marsvin class
m1 = Marsvin("Plet", 2, 1.1)

print(m1.get_navn())
print(m1.get_alder())
print(m1.get_vaegt())

print("---")

#Test setters marsvin class
m2 = Marsvin("Pjuske", 3, 2.3)

m2.set_navn("Poul")
m2.set_alder(5)
m2.set_vaegt(3)

print(m2.get_navn())
print(m2.get_alder())
print(m2.get_vaegt())

print("---")

#Test ugyldige data
m1.set_alder(-10)

print(m1.get_alder())
print("---")
"""
"""
#Test Enum Race
m1 = Marsvin("Plet", 2, 1.1, Race.TEDDY)
print(m1)
print("---")

#Test Bur class
bur1 = Bur(1)
print(bur1)

#Test CRUD CREATE
print("---")

m2 = Marsvin("Plet", 2, 1.1, Race.ABYSSINIER)
m3 = Marsvin("Nuttet", 3, 1.4, Race.SHELTIE)
# Test CREATE
print("Test CREATE")
bur1.tilfoej_marsvin(m1)
bur1.tilfoej_marsvin(m2)
bur1.tilfoej_marsvin(m3)
#Test READ
print("Test READ")
bur1.vis_alle_marsvin()
#Test UPDATE
print("Test UPDATE")
bur1.opdater_marsvin_navn("Plet", "SuperPlet")
bur1.vis_alle_marsvin()
#Test DELETE
print("Test DELETE")
bur1.slet_marsvin("Nuttet")
bur1.vis_alle_marsvin()

print("sortering efter navn")
bur1.sorter_efter_navn()
bur1.vis_alle_marsvin()
print("sortering efter alder")
bur1.sorter_efter_alder()
bur1.vis_alle_marsvin()
print("sortering efter vægt")
bur1.sorter_efter_vaegt()
bur1.vis_alle_marsvin()
print("sortering efter race")
bur1.sorter_efter_race()
bur1.vis_alle_marsvin()
"""

"""
#Byg listen
marsvin_liste = []

marsvin_liste.append(m1)

for marsvin in marsvin_liste:
    print(marsvin)

"""



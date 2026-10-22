from Lesson6.Marsvin.model.marsvin import Marsvin
from Lesson6.Marsvin.model.Race import Race


class FilHaandtering:

    @staticmethod
    def gem_til_fil(marsvin_liste):

        with open("data/marsvin.txt", "w") as fil:


                fil.write("=== Marsvin Register ===\n\n")

                for marsvin in marsvin_liste:
                    fil.write(f"Navn  : {marsvin.get_navn()}\n")
                    fil.write(f"Alder : {marsvin.get_alder()} aar\n")
                    fil.write(f"Vægt  : {marsvin.get_vaegt()} kg\n")
                    fil.write(f"Race  : {marsvin.get_race().name}\n")
                    fil.write("-" * 30 + "\n")




    @staticmethod
    def laes_fra_fil():

        marsvin_liste = []

        with open("data/marsvin.txt", "r") as fil:

            linjer = fil.readlines()

        i = 0

        while i < len(linjer):

            if linjer[i].startswith("Navn"):
                navn = linjer[i].split(":")[1].strip()

                alder = int(
                    linjer[i + 1]
                    .split(":")[1]
                    .replace("aar", "")
                    .strip()
                )

                vaegt = float(
                    linjer[i + 2]
                    .split(":")[1]
                    .replace("kg", "")
                    .strip()
                )

                race_navn = (
                    linjer[i + 3]
                    .split(":")[1]
                    .strip()
                )

                race = Race[race_navn]

                marsvin = Marsvin(
                    navn,
                    alder,
                    vaegt,
                    race
                )

                marsvin_liste.append(marsvin)

            i += 1

        return marsvin_liste



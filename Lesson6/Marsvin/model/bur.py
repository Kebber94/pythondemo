class Bur:

    def __init__(self, nummer):
        self.__nummer = nummer
        self.__marsvin_liste = []

    def get_marsvin_liste(self):
        return self.__marsvin_liste

    def __str__(self):
        return f"{self.__nummer} nummer {self.__marsvin_liste} marsvin"


    # CREATE
    def tilfoej_marsvin(self, marsvin):
        self.__marsvin_liste.append(marsvin)

    # READ
    def vis_alle_marsvin(self):
        for marsvin in self.__marsvin_liste:
            print(marsvin)

    # UPDATE
    def opdater_marsvin_navn(self, gammel_navn, nyt_navn):

        for marsvin in self.__marsvin_liste:

            if marsvin.get_navn() == gammel_navn:
                marsvin.set_navn(nyt_navn)
                return True

        return False

    # DELETE
    def slet_marsvin(self, navn):

        for marsvin in self.__marsvin_liste:

            if marsvin.get_navn() == navn:
                self.__marsvin_liste.remove(marsvin)
                return True

            return False



    # Sortering efter navn
    def sorter_efter_navn(self):
        self.__marsvin_liste.sort(
            key=lambda marsvin: marsvin.get_navn()
        )

    # Sortering efter alder
    def sorter_efter_alder(self):
        self.__marsvin_liste.sort(
            key=lambda marsvin: marsvin.get_alder()
        )

    # Sortering efter vægt
    def sorter_efter_vaegt(self):
        self.__marsvin_liste.sort(
            key=lambda marsvin: marsvin.get_vaegt()
        )

    # Sortering efter race
    def sorter_efter_race(self):
        self.__marsvin_liste.sort(
            key=lambda marsvin: marsvin.get_race().value
        )

    # Sortering efter køn
    def sorter_efter_koen(self):
        self.__marsvin_liste.sort(
            key=lambda marsvin: marsvin.get_koen().name
        )








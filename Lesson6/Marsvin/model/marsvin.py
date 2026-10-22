from Lesson6.Marsvin.model.Race import Race


class Marsvin:

    def __init__(self, navn, alder, vaegt, race):
        self.set_navn(navn)
        self.set_alder(alder)
        self.set_vaegt(vaegt)
        self.__race = race

    # Getter
    def get_race(self):
        return self.__race

    # Setter
    def set_race(self, race):

        if isinstance(race, Race):
            self.__race = race
        else:
            print("Ugyldig race")

    def get_navn(self):
            return self.__navn

    def get_alder(self):
            return self.__alder

    def get_vaegt(self):
            return self.__vaegt

    def set_navn(self, navn):
        if navn != "":
            self.__navn = navn

    def set_alder(self, alder):
        if alder > 0:
            self.__alder = alder

    def set_vaegt(self, vaegt):
        if vaegt > 0:
            self.__vaegt = vaegt

    def __str__(self):
        return f"{self.__navn} ({self.__alder} år, {self.__vaegt} kg {self.__race} race)"



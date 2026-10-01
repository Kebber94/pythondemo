"""
Opgave : Forstå koden

Studér koden for klassen Movie og objekterne movie1 og movie2.
Besvar følgende spørgsmål:

1. Hvad er formålet med de private attributter (__titel, __skuespillere, __instruktor, __year)?
    Datavalidering af input til oprettelse af objekt.
2. Hvorfor bruger vi getters og setters?
    For at kunne se skjulte attributter uden for class'en.
    Setters bruges til at sætte værdien.
3. Hvad sker der, hvis man forsøger at oprette en film med et ugyldigt årstal?
    Man får af vide "Ugyldigt årstal"
4. Hvad er et objekt?
    Det er et objekt dannet ud fra class'en.
    I det her tilfælde en film.
5. Hvilke objekter bliver oprettet i programmet?
    Film objekter
6. Hvilke værdier indeholder objekterne movie1 og movie2?
    titel, skuespillere, instruktor, year
7. Hvad vil følgende kode udskrive på skærmen?

"""

class Movie:
    def __init__(self, titel, skuespillere, instruktor, year):
        self.set_titel(titel)
        self.set_skuespillere(skuespillere)
        self.set_instruktor(instruktor)
        self.set_year(year)

    # Private attributter
    __titel = ""
    __skuespillere = []
    __instruktor = ""
    __year = 0

    # Getters
    def get_titel(self):
        return self.__titel

    def get_skuespillere(self):
        return self.__skuespillere

    def get_instruktor(self):
        return self.__instruktor

    def get_year(self):
        return self.__year

    # Setters med validering
    def set_titel(self, titel):
        if len(titel) >= 2:
            self.__titel = titel
        else:
            print("Titel skal være mindst 2 tegn.")

    def set_skuespillere(self, skuespillere):
        if isinstance(skuespillere, list) and len(skuespillere) > 0:
            self.__skuespillere = skuespillere
        else:
            print("Der skal være mindst én skuespiller.")

    def set_instruktor(self, instruktor):
        if len(instruktor) >= 2:
            self.__instruktor = instruktor
        else:
            print("Instruktørens navn er ugyldigt.")

    def set_year(self, year):
        if 1888 <= year <= 2030:
            self.__year = year
        else:
            print("Ugyldigt årstal.")

    def vis_info(self):
        print(f"Titel: {self.__titel}")
        print(f"Skuespillere: {', '.join(self.__skuespillere)}")
        print(f"Instruktør: {self.__instruktor}")
        print(f"År: {self.__year}")


movie1 = Movie(
    "Inception",
    ["Leonardo DiCaprio", "Tom Hardy"],
    "Christopher Nolan",
    2010
)

movie2 = Movie(
    "The Matrix",
    ["Keanu Reeves", "Carrie-Anne Moss"],
    "Lana Wachowski",
    1999
)


print(movie1.get_titel())
print(movie2.get_year())

movie1.set_year(2012)
movie1.set_titel("Inception: Updated")

print(movie1.get_titel())
print(movie1.get_year())

print()

movie1.vis_info()

print()

movie2.vis_info()



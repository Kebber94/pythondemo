class Bil:
    def __init__(self, brand, model, year):

        print("Constructor kaldes")

        self.brand = brand
        self.model = model
        self.year = year
        self.__hastighed = 0

    def set_hastighed(self, ny_hastighed):
        if ny_hastighed >= 0:
            self.__hastighed = ny_hastighed
            print("Hastigheden opdateret")
        else:
            print("Fejl - negativ hastighed")

print("Før objektet oprettes")

bil1 = Bil("Audi", "A4", 2026)

print("Efter objektet oprettes")

bil1.set_hastighed(100)
bil1.set_hastighed(-100)



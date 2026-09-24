"""
Opgave: Find dit stjernetegn ♈♉♊
I denne opgave skal du lave et program, der spørger brugeren om fødselsmåned og viser det
tilhørende stjernetegn.
Formål
Du skal øve:
• input()
• def
• if, elif og else
• return
Krav
1. Brugeren indtaster et månedstal (1-12).
2. Opret en funktion, der finder stjernetegnet.
3. Brug if/elif/else til at vælge det rigtige stjernetegn.
4. Udskriv resultatet.
"""



def def_starsign():
    month = int(input("Hvad er din fødselsmåned?"))
    day = int(input("Hvilken dag er du født?"))

    if birthday == 1:
        print("Stenbuk")
    elif birthday == 2:
        print("Vandmand")
    elif birthday == 3:
       print("Fisk")
    elif birthday == 4:
      print("Vædder")
    elif birthday == 5:
      print("Tyr")
    elif birthday == 6:
       print("Tvilling")
    elif birthday == 7:
       print("Krebs")
    elif birthday == 8:
       print("Løve")
    elif birthday == 9:
       print("Jomfru")
    elif birthday == 10:
        print("Vægt")
    elif birthday == 11:
        print("Skorpion")
    elif birthday == 12:
        print("Skytte")
    else:
        print("Ugyldigt input. Prøv igen")





def def_starsign_short():
    birthday = int(input("Hvad er din fødselsmåned?"))

    match birthday:
        case 1:
            print("Stenbuk")
        case 2:
            print("Vandmand")
        case 3:
            print("Fisk")
        case 4:
            print("Vædder")
        case 5:
          print("Tyr")
        case 6:
           print("Tvilling")
        case 7:
           print("Krebs")
        case 8:
           print("Løve")
        case 9:
           print("Jomfru")
        case 10:
            print("Vægt")
        case 11:
            print("Skorpion")
        case 12:
            print("Skytte")
        case _:
            print("Ugyldigt input. Prøv igen")





def def_starsign():
    month = int(input("Hvad er din fødselsmåned? "))
    day = int(input("Hvilken dag er du født? "))

    if month == 1:
        if day <= 19:
            return "Stenbuk"
        else:
            return "Vandmand"

    elif month == 2:
        if day <= 18:
            return "Vandmand"
        else:
            return "Fisk"

    elif month == 3:
        if day <= 20:
            return "Fisk"
        else:
            return "Vædder"

    elif month == 4:
        if day <= 19:
            return "Vædder"
        else:
            return "Tyr"

    elif month == 5:
        if day <= 20:
            return "Tyr"
        else:
            return "Tvilling"

    elif month == 6:
        if day <= 20:
            return "Tvilling"
        else:
            return "Krebs"

    elif month == 7:
        if day <= 22:
            return "Krebs"
        else:
            return "Løve"

    elif month == 8:
        if day <= 22:
            return "Løve"
        else:
            return "Jomfru"

    elif month == 9:
        if day <= 22:
            return "Jomfru"
        else:
            return "Vægt"

    elif month == 10:
        if day <= 22:
            return "Vægt"
        else:
            return "Skorpion"

    elif month == 11:
        if day <= 21:
            return "Skorpion"
        else:
            return "Skytte"

    elif month == 12:
        if day <= 21:
            return "Skytte"
        else:
            return "Stenbuk"

    else:
        return "Ugyldig måned"


starsign = def_starsign()
print("Dit stjernetegn er:", starsign)


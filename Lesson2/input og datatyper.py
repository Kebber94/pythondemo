from os.path import sep

navn = str(input("Hvad hedder du?"))
alder = int(input("Hvor gammel er du?"))


print ("\nHej ", str.capitalize(navn), ", ", "Du er ", alder, " år gammel.", sep="")



if alder >= 18:
    print("Ey! Du er jo myndig ;-)\n")
else:
    print("Du er for ung :-(\n")


tal = int(input("Giv mig et tal"))

if tal > 0:
    print("Dit tal er et positivt tal")
if tal < -1:
    print("Dit tal er et negativt tal")
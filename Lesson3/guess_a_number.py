

# Variabler
# min_number = 1
# max_number = 20
users_guess = 0



# Metoder
def get_number_to_be_guessed():
    return int(input("Hvilket tal skal gættes?...:"))

def get_users_guess():
    return int(input("Hvad er dit gæt?...:"))

def compare_numbers(users_guess, number_to_be_guessed):
    if number_to_be_guessed == users_guess:
        print(f"Du har gættet tallet! Det var {number_to_be_guessed}")
    else:
        print(f"Desværre, taller var ikke {users_guess}")
        if  users_guess < number_to_be_guessed:
            print(f"Tallet er højere end {users_guess}")
        else:
            print(f"Tallet er lavere {users_guess}")



# Kode
print("Velkommen til Gæt et tal.\n"
      "Her skal du forsøge at gætte mit hemmelige tal.\n"
      "Du får alle de gæt du har brug for")

number_to_be_guessed = get_number_to_be_guessed()


while users_guess != number_to_be_guessed:
    users_guess = get_users_guess()
    compare_numbers(users_guess, number_to_be_guessed)

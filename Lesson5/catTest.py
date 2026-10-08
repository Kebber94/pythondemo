from Lesson5.cat import Cat

class CatTest:

    @staticmethod
    def main():
        # Create a list of cats
        cats = [
            Cat("Luna"),
            Cat("Simba"),
            Cat("Milo")
        ]

        # Use a for loop to call methods
        for cat in cats:
            cat.eat()
            cat.chase_mouse()
            cat.sleep()
            print()  # Empty line between cats

        total_cats = int(input("How many cats would you like to register?"))
        cat_list = []

        for number in range(1, total_cats + 1):
            get_catname = input(f"What is cat number {number} name? ")
            cat_list.append(get_catname)



        print(cat_list)

# Run the program
if __name__ == "__main__":
    CatTest.main()


"""3: Use input

Ask the user how many cats they want to register.
Ask the names of the cats.

4: Use for and print
After all cats have been registered, display each cat performing its activities:

Eating
Chasing a mouse
Sleeping"""
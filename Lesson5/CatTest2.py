from Lesson5.cat import Cat

class CatTest:

    @staticmethod
    def main():

        total_cats = int(input("How many cats would you like to register?"))
        cat_list = []

        for number in range(1, total_cats + 1):
            cat_list.append(Cat(str(input(f"What is cat number {number} name? "))))

        # Use a for loop to call methods
        for cat in cat_list:
            cat.eat()
            cat.chase_mouse()
            cat.sleep()
            print()  # Empty line between cats

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
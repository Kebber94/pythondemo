class Cat:
    def __init__(self, name):
        # Attribute
        self.name = name

    def eat(self):
        """Cat eats burrito."""
        print(f"{self.name} eats a burrito 🌯")

    def chase_mouse(self):
        """Cat chase mouse."""
        print(f"{self.name} chases Jerry 🐭")

    def sleep(self):
        """Cat sleeps again."""
        print(f"{self.name} sleeps again 😴")

class Chicken:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hunger = 50
        self.happiness = 50
        self.location = "coop"

    def feed(self):
        self.hunger += 10
        self.happiness -= 20

    def play(self):
        self.happiness += 20
        self.hunger -= 10

    def move(self, location):
        self.location = location

    def display_status(self):
        print(f"{self.name} is {self.age} years old.")
        print(f"Hunger: {self.hunger}%")
        print(f"Happiness: {self.happiness}%")
        print(f"Location: {self.location}")

def main():
    chicken = Chicken("Cluck", 1)
    while True:
        chicken.display_status()
        user_input = input("What would you like to do? (feed, play, move, exit): ")
        if user_input == "feed":
            chicken.feed()
        elif user_input == "play":
            chicken.play()
        elif user_input == "move":
            location = input("Enter new location: ")
            chicken.move(location)
        elif user_input == "exit":
            break
        else:
            print("Invalid input. Try again!")

if __name__ == "__main__":
    main()

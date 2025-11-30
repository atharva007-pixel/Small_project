from random import randint

class Player:
    def __init__(self, name):
        self.name = name
        self.guesses = []

    def guess(self, target):
        num = int(input("Enter your number (1-10): "))
        self.guesses.append(num)

        if num == target:
            print("🎉 You guessed right!")
            return True
        elif num < target:
            print("Higher number please 🔼")
        else:
            print("Lower number please 🔽")
        return False

    def summary(self):
        print(f"\n{self.name}, you took {len(self.guesses)} chances.")
        print("Your guesses were:", self.guesses)


# Game starts here
print("🎯 Welcome to the Guess the Number Game!")
user = input("Enter your name: ")
target = randint(1, 10)
player = Player(user)

while True:
    if player.guess(target):
        player.summary()
        break



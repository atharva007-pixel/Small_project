word=["pain","paris","alpine","plane","apple","grape","grapefruit"]
    # print("Welcome to the word guessing game!")

class Hangman():
    def __init__(self,name):
        self.name=name
    
    def game(self):
        import random
        self.chosen_word=random.choice(word)
        
        self.lintial_w=self.chosen_word[0]
        self.llast_w=self.chosen_word[-1]

        self.letrs=[]

        for letters in self.chosen_word:
            self.letrs.append(letters)

        
    def guess(self):
           print(f"{self.chosen_word}") 
            
           while True:
            guess=input("Whats your guess man: ")
            if guess in self.letrs:
                 print("You guessed right")
                 print(f"The word starts with {self.lintial_w}")


            # print(chosen_word)
            # print(lintial_w)
            # print(llast_w)

# game()
Hangman("Atharva")

Hangman.game(self=Hangman)
Hangman.guess(self=Hangman)



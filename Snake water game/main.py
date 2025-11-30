# Same like stone paper scissor game
''' 
Snake drinks water
Water drowns gum
Gun shoot snake
s=1
w=-1
g=0
'''

import time
import os

# Clear screen for clean look
os.system('cls' if os.name == 'nt' else 'clear')

# Fancy intro

print("        💖 WELCOME TO THE SWG GAME 💖")

time.sleep(1)
print("\nLet's find out what fate has in store for you 💫\n")
time.sleep(1)

# Taking random numbers
import random
computer=random.choice([1,-1,0])
user_choice=input("Enter Your Choice: ").lower()
user_dict={"snake":1,"water":-1,"gun":0}
chose=user_dict[user_choice]


# Animation
print("\n✨ Be prepared, the game is about to begin! ✨")
for i in range(5):
    print("❤️", end=" ", flush=True)
    time.sleep(0.5)
print("\n")



if(computer==1 and chose==-1):
    print("You win!")
elif(computer==1 and chose==0):
    print("You loose!")


elif(computer==-1 and chose==1):
    print("You loose!")
elif(computer==-1 and chose==0):
    print("You win!")


elif(computer==0 and chose==1):
    print("You loose!")
elif(computer==0 and chose==-1):
    print("You win!")

else:
    print("Its draw")

# print(f"Computer choose ,meawnhile you  choose {user_choice}")
print("Well played,thanks for playing")


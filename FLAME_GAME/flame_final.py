
import time
import os

# Clear screen for clean look
os.system('cls' if os.name == 'nt' else 'clear')

# Fancy intro
print("🔥" * 40)
print("        💖 WELCOME TO THE F.L.A.M.E GAME 💖")
print("🔥" * 40)
time.sleep(1)
print("\nLet's find out what fate has in store for you 💫\n")
time.sleep(1)

# User input
flame_name1 = input("💌 Enter Your sweet name: ").strip().capitalize()
flame_name2 = input("💌 Enter your partner's lovely name: ").strip().capitalize()

# Handle names with or without spaces
gap1 = flame_name1.find(" ")
gap2 = flame_name2.find(" ")

user_name1 = flame_name1[:gap1] if gap1 != -1 else flame_name1
user_name2 = flame_name2[:gap2] if gap2 != -1 else flame_name2

# Create sets
set_1 = set(user_name1)
set_2 = set(user_name2)

# Logic
intersect = set_1.intersection(set_2)
union = set_1.union(set_2)
diff = union - intersect

# Animation
print("\n✨ Calculating your destiny ✨")
for i in range(5):
    print("❤️", end=" ", flush=True)
    time.sleep(0.5)
print("\n")

# FLAME Logic
f = range(1, 1000, 5)
l = range(2, 1000, 5)
a = range(3, 1000, 5)
m = range(4, 1000, 5)
e = range(5, 1000, 5)

# Stylish results
print("💫 RESULT 💫")
print("🔥" * 20)
if len(diff) in f:
    print("💞 You both are just **FRIENDS** 💞")
elif len(diff) in l:
    print("❤️ OMG! You guys are **LOVERS** ❤️")
elif len(diff) in a:
    print("🔥 Damn! You have an **AFFAIR** 🔥")
elif len(diff) in m:
    print("💍 You both will **MARRY** someday 💍")
elif len(diff) in e:
    print("💔 Unfortunately, you’re **ENEMIES** 💔")
else:
    print("💗 You share a **SPECIAL BOND** 💗")

print("🔥" * 20)
time.sleep(1)
print("\nThanks for playing the FLAME game! 💖\n")
time.sleep(1)
print("Made with 💕 by", user_name1)



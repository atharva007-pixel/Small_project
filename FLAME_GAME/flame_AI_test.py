import os
import time

def display_result(diff_len):
    results = {
        1: "💞 You both are just **FRIENDS** 💞",
        2: "❤️ OMG! You guys are **LOVERS** ❤️",
        3: "🔥 Damn! You have an **AFFAIR** 🔥", 
        4: "💍 You both will **MARRY** someday 💍",
        0: "💔 Unfortunately, you're **ENEMIES** 💔"
    }
    return results.get(diff_len % 5, "💗 You share a **SPECIAL BOND** 💗")

# Clear screen and show intro
os.system('cls' if os.name == 'nt' else 'clear')
print("🔥" * 40, "\n        💖 WELCOME TO THE F.L.A.M.E GAME 💖\n", "🔥" * 40)

# Get names and create sets
name1 = input("\n💌 Enter Your sweet name: ").strip().split()[0].capitalize()
name2 = input("💌 Enter your partner's lovely name: ").strip().split()[0].capitalize()

# Calculate result
diff_length = len(set(name1).union(set(name2)) - set(name1).intersection(set(name2)))

# Animation and result display
print("\n✨ Calculating your destiny ✨")
print("❤️ " * 5, flush=True)
time.sleep(1)

print("\n💫 RESULT 💫\n", "🔥" * 20)
print(display_result(diff_length))
print("🔥" * 20, f"\n\nMade with 💕 by {name1}")
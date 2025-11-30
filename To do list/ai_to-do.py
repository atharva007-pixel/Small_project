import os

# Clear screen and initialize
os.system('cls' if os.name == 'nt' else 'clear')
tasks = []

def add_task():
    tasks.append(input("Enter your task: "))
    with open("Task_record.txt", "a") as f:
        f.write(tasks[-1] + "\n")
    print("Your task has been added\n")

def remove_task():
    tasks.pop(int(input("Enter which task to remove : ")) - 1)
    print("The task has been removed\n")

def view_task():
    print("Nothing is in the to-do" if not tasks else f"Your tasks are:\n{chr(10).join(tasks)}\n")

# Main program
print("TAKE YOUR NOTES IN MOTION\n")
user_name = input("Whats your name buddy: ").capitalize().strip()
options = f"""What would like to do today {user_name}:
    1).Add a task
    2).View a task
    3).Remove a task
    4).Exit\n"""

actions = {
    '1': add_task,
    '2': view_task,
    '3': remove_task,
    '4': lambda: print("Goodbye! 👋") or True
}

while True:
    print(options)
    choice = input("Enter your choice:\n")
    if choice not in actions:
        print("Invalid input, please enter a number corresponding to your choice.\n")
        continue
    if actions[choice]():
        break
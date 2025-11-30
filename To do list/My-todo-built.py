import os

# Clear screen for clean look
os.system('cls' if os.name == 'nt' else 'clear')

task=[]


# adding the task
def add_task():
    write_task=input("Enter your task: ")
    task.append(write_task)
    print("Your task has been added\n")
    # extract_string="\n".join(task) # Joining the list items with newline character ,but this is unneccesary as we dont need to take everything from the list nd print it
    with open("Task_record.txt","a") as f: #Append mode to keep previous tasks
     f.write(write_task+"\n") 


# Removing the task
def remove_task():
    task.pop(int(input("Enter which task to remove : "))-1)
    print("The task has been removed\n")


# Viewing the task
def view_task():
    if not task:
        print("Nothing is in the to-do\n")
    else:
        print("\nYour tasks are:")
        for i, t in enumerate(task, 1):
            print(f"{i}. {t}")
        print()

# Exiting THE program
def exit_program():
    print("Goodbye! 👋")
    return True


# Starting the program

print("TAKE YOUR NOTES IN MOTION\n\t")
user_name=input("Whats your name  buddy: ").capitalize().strip()
user_task=(f'''What would like to do today {user_name}:
    1).Add a task
    2).View a task
    3).Remove a task
    4).Exit       \n''')


# Best way is to create a dictionary to map choices to functions
actions={
    '1':add_task,
    '2':view_task,
    '3':remove_task,
    '4':exit_program
}

#    print(user_task)
while True:
   print(user_task)
   choice=(input("Enter your choice:\n"))
   if choice not in actions:
     print("Invalid input, please enter a number corresponding to your choice.\n")
     continue
   if actions[choice]():
      break

        

#MY WAY OF DOING IT BELOW:  

# while True:
#  print(user_task)
#  if choice not in ['1','2','3','4']:
#     print("Invalid input, please enter a number corresponding to your choice.\n")
#     pass
 
#  if choice=="1":
#     add_task()

#  elif choice=="3":
#     remove_task()
 
#  elif choice=='2':
#     view_task()

#  elif choice=='4':
#     print("Goodbye! 👋")
#     break

    

    

# user=input("Type your msg: ")
# l.append(user)
# print(l)
import os

# Clear screen for clean look
os.system('cls' if os.name == 'nt' else 'clear')

print("TAKE YOUR NOTES IN MOTION\n\t")
user_name=input("Whats your name  fella: ").capitalize().strip()
user_task=(f'''What would like to do today {user_name}:
    1).Add a task
    2).Flag a task
    3).Remove a task\n''')
print(user_task)

task_list=[]
while True:

 choice=int(input("Enter your choice: "))

    
 if (choice==1):
        add_task=input("Add your task: ")
        task_list.append(add_task)
        print("Task is added")
        
 elif(choice==0):
        flag_task=input("Type your status: ")
        task_list.append(flag_task)
        print("Task status updated")

 elif choice==-1:
        remove_task=int(input("Remove task: "))
        task_list.pop(remove_task-1)
        print("Task removed")
 
 
 print(task_list)


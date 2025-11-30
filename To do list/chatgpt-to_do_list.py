tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("\nEnter choice: ")
    
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("✅ Task added!")
    
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    
    elif choice == "3":
        if tasks:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"✅ Removed: {removed}")
            else:
                print("❌ Invalid number!")
        else:
            print("No tasks to remove!")
    
    elif choice == "4":
        print("Goodbye! 👋")
        break
    
    else:
        print("❌ Invalid choice!")

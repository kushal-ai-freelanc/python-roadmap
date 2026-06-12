tasks=[]
while True:
    print("\n1. Add text")
    print("2. view text")
    print("3. Exit")
    choice=int(input("Enter choice:"))

    if choice==1:
        task=input("task: ")
        tasks.append(task)
        print("Task added!")

    elif choice==2:
        print("\nTasks:")
        for i, task in enumerate(tasks,1):
            print(f"{i}.{task}")

    elif choice==3:
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
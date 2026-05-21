def load_tasks():
    try:
        file = open("tasks.txt", "r")
        tasks = file.read().splitlines()
        file.close()
        return tasks
    except:
        return[]

def save_tasks(tasks):
        file = open("tasks.txt", "w")
        for task in tasks:
            file.write(task + "\n")
        file.close()

tasks = load_tasks()
while True:
    print("----To do list----")
    print("1. Add a task")
    print("2. View task")
    print("3. Remove task")
    print("4. Quit")

    choice = input("Enter your choice:")

    if choice == "1":
        task = input("Enter a task:")
        tasks.append(task)
        save_tasks(tasks)
        print("Task successfuly added")

    elif choice == "2":
        print("Tasks")

        for task in tasks:
            print("-", task)

    elif choice == "3":

       try: 
        task = input("Enter a task you want to remove:")
        tasks.remove(task)
        save_tasks(tasks)
        print("Task successfully removed:")

       except:
           print("Task not found!")

    elif choice == "4":
        print("GOODBYE!")

    else:
        print("Invalid choice")

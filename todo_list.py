tasks = []

def addTask():
    while True:
        task = input("Enter the Task:(If u finish adding type stopAppend) ")
        tasks.append(task)
        print(f"Task '{task}' is added to the List.")
        if task == "stopAppend":
            break

def viewTask():
    if not tasks:
        print("There is no task enter!")
    else:
        print("Current task")
        for index, task in enumerate(tasks):
            print(f"Task #'{index}'. '{task}'")

def deleteTask():
    viewTask()
    try:
        taskToDelete = int(input("Enter # to delete: "))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task #{taskToDelete} is deleted :)")
        else:
            print(f"Task #{taskToDelete} was not found.")

    except:
        print("Invalid input")

if __name__ == "__main__":
    print("Welcome to ToDo List App:)")

    while True:
        print("/n")
        print("Select the operation")
        print("---------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. View the tasks")
        print("4. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            addTask()
        elif choice == 2:
            deleteTask()
        elif choice == 3:
            viewTask()
        elif choice == 4:
            break
        else:
            print("You've enter the wront input!")
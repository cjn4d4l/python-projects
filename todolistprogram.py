#To-DO List Program
#with local storage txt for tasks
#basic file handling read and append text

tasks = []

run_todo = True
initialize = True

print("To-Do List Program")
while run_todo:
    if initialize:
        with open("todos.txt", "r") as f:
            for i in f:
                tasks.append(i)
        initialize = False

    file = open("todos.txt", "a")
    print("---Menu---")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Update Task")
    print("4. View Tasks")
    print("5. Exit")
    try:
        choice = int(input("Enter Action: "))
    except:
        print("\n---Invalid input. Try again---\n")
        continue
    if choice == 1:
        print("\n---Add Task---")
        add_task = input("Enter a Task: ")
        print("Task Appended Successfully")
        #tasks.append(add_task) appended to tasks list
        file.write(add_task + "\n") #appends to text file where it is  stored
        initialize = True
        tasks = []
    elif choice == 2:
        while True:
            try:
                print("\n---Delete Task---")
                delete_task = int(input("Enter Task Number to Delete: ")) #working in progress with the local storage feature
                tasks.pop(delete_task - 1)
                break
            except:
                print("Input Should be a number")
        print("Task Deleted")
    elif choice == 3:
        while True:
            try:
                print("\n---Update Task---")
                index = int(input("Enter Task Number to Update: "))
                print(f"Task: {tasks[index - 1]}")
                Updated_task = input("Enter Edited Task: ") #working in progress with the local storage feature
                tasks[index - 1] = Updated_task
                break
            except:
                print("Input Should be a number")
        print("Task Edited Successfully")
    elif choice == 4:
        with open("todos.txt", "r") as f:
            if f.read() == "":
                print("No Tasks Available")
            else:
                n = 1
                print("\n---View Tasks---")
                for i in tasks:
                    print(f"{n}. {i}", end="")
                    n += 1
        print()
    elif (choice == 5):
        run_todo = False
    file.close()
    print()
    
print("Program Exited")
close = input()
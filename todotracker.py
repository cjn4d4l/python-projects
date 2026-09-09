#todotracker program
import json
import os

run_op = True

tasks = []

try:
    with open("tasks.json", "r") as file:
        data = json.load(file)

        for i in data:
            tasks.append({
                "content": i['content'],
                "is_done": i['is_done']
            })
except json.JSONDecodeError:
    tasks = []

def add_task():
    print("Add a Task")
    task = input("> ")
    return task

while run_op:
    print("---Command Line To-Do Tracker---\n")
    print("Options:")
    print("[1] View Tasks")
    print("[2] Add a Task")
    print("[3] Exit")
    choice = int(input("> "))

    if choice == 1:
        os.system("cls")
        print("---ToDos---")
        if tasks:
            n = 1
            for i in tasks:
                if i['is_done']:
                    print(f"[{n}] {i['content']}    [Done]")
                else:
                    print(f"[{n}] {i['content']}    [Pending]")
                n += 1
        else:
            print("No Tasks Yet")

        print()
    elif choice == 2:
        os.system("cls")
        taskInput = add_task()
        todo = {
            "content": taskInput,
            "is_done": False
        }
        tasks.append(todo)
        os.system("cls")
    elif choice == 3:
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)
        run_op = False
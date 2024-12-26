tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added.")

def view_tasks():
    for i, t in enumerate(tasks, start=1):
        status = "Done" if t["done"] else "Pending"
        print(f"{i}. {t['task']} - {status}")

def mark_done(index):
    if 0 < index <= len(tasks):
        tasks[index - 1]["done"] = True
        print(f"Task '{tasks[index - 1]['task']}' marked as done.")
    else:
        print("Invalid task number.")

# Menu for testing
if __name__ == "__main__":
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Done\n4. Exit")
        choice = int(input("Choose an option: "))
        if choice == 1:
            task = input("Enter the task: ")
            add_task(task)
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            num = int(input("Enter task number to mark as done: "))
            mark_done(num)
        elif choice == 4:
            break
        else:
            print("Invalid choice.")
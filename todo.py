tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added")

def display_tasks():
    if len(tasks) == 0:
        print("No tasks available")
    else:
        for i in range(len(tasks)):
            print(i+1, tasks[i])

def delete_task():
    display_tasks()
    num = int(input("Enter task number to delete: "))
    if num <= len(tasks):
        tasks.pop(num-1)
        print("Task deleted")
    else:
        print("Invalid number")

def main():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            display_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
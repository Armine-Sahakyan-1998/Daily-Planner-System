tasks = {}
def add_task():
    task_name = input("Enter the task name: ")
    priority = input("How important is it:(a lot,not a lot,a little?): ")
    tasks[task_name] = priority
    print(f"Task '{task_name}' added with priority {priority}.")




def view_task():
    if not tasks:
        print("No tasks available")
    else:
        print("Current Tasks:")
        for key,value in tasks.items():
            print(f"- {key} (Priority: {value})")




def delete_task():
    if not tasks:
        print("No tasks available to remove: ")
        return
    
    del_name = input("What do you want to delete: ")
    if del_name in tasks:
        del tasks[del_name]
        print(f"Task '{del_name}' removed.")
    else:
        print(f"Task '{del_name}' not found.")


while True:
    print("\nTask Managmant System: ")
    print("1. Add Task")
    print("2. View Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1,2,3 or 4): ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice.Please enter 1,2,3 or 4.")



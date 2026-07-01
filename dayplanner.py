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












#1,2,3,4,5
# tiv = 1
# while tiv <= 5:
#     print("Current Count:", tiv)
#     tiv += 1
# print("Loop finished!")




# #5,4,3,2,1
# tiv_1 = 5
# while tiv_1 >= 1:
#     print("Current count:", tiv_1)
#     tiv_1 -= 1
# print("Loop finished!")




# #Passwors arnvazn 8 simvol
# password = input("Enter a password (at least 8 characters): ")

# while len(password) < 8:
#     print("Password is too short. Please enter at least 8 characters.")
#     password = input("Enter a password (at least 8 characters): ")
# print("Password accepted!")





#factorial
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# result = factorial(5)
# print(f"The factorial of 5 is {result}")

#fibonacci
# def fibonacchi(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacchi(n - 1) + fibonacchi(n - 2)
    
# result = fibonacchi(6)
# print(f"Fibonacchi of 6 is {result}")
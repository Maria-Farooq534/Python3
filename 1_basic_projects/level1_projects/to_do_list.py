"""
Simple To-Do List (Console Based)
Store tasks in a list.
Add, remove, and display tasks.
(Practice with list mutation, append, remove).
"""

tasks = []

while True:

    print("\nChoose one option:")
    print("1. Add Tasks")
    print("2. Remove Tasks")
    print("3. View Tasks")
    print("4. Exit")


    user_query = input("Select 1,2,3 or 4 : ")
    
    # Add Tasks
    if user_query == "1":
        add_task = input("Add task : ")
        tasks.append(add_task)
        print(f"\n'{add_task}' added successfully!")
    
    #Remove Tasks
    elif user_query == "2":
        remove_task = input("Enter task to remove : ")
        if remove_task in tasks:
            tasks.remove(remove_task)
            print(f"'{remove_task}' removed!\n")
        else:
            print(f"\n'{remove_task}' task is not available in the list.")

    # View Tasks
    elif user_query == "3":
        if not tasks:
            print("\nNo tasks yet! Add dome tasks first.")
        else:
            print("\nAvailable Tasks to do:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    # Exit
    elif user_query == "4":
        print("Exit Successfully!")
        break

    # Exit
    else:
        print("Please enter number between 1-4.")
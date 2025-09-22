
from to_do_list import ToDoList


# ui
flag = True
while flag:
    print("\n \n TO DO LIST")
    print("----------------------------")
    user_tlist = ToDoList()
    choice = input(
        " 1. Add new task \n 2. remove task \n 3. Save task to storage \n 4. Load task from storage \n 5. Show list of tasks \n 6. exit \n ---------------------------- \n \n"
    )

    if choice == "1":
        try:
            name, description, priority = input("Enter informaiton of ypur task (three value) \n").split()
            user_tlist.add_task(name, description, priority)
        except Exception as e:
            print(f"Error : {e}")
    elif choice == "2":
        name = input("Enter name of task you want delete :\n")
        user_tlist.remove_task(name)
        
    elif choice == "3":
        user_tlist.save_task()
        print("task saved successfully")
        
    elif choice == "4":
        user_tlist.load_tasks()
        print("task loaded successfully")
        
    elif choice == "5":
        user_tlist.show_list()
        
    elif choice == "6":
        res = input("Do you want save yout task ? (y/n) \n")
        if res.lower() == "y":
            user_tlist.load_tasks()
        flag = False

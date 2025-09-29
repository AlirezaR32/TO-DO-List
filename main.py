from src.services.todo_list import ToDoList

def print_header():
    print("\n" + "="*40)
    print("         📝  TO DO LIST MANAGER  📝")
    print("="*40)

def print_menu():
    print("""
    [1] ➕  Add new task
    [2] ➖  Remove task
    [3] �  Update task
    [4] �💾  Save tasks to storage
    [5] 📂  Load tasks from storage
    [6] 📋  Show all tasks
    [7] 📊  Show tasks by priority
    [8] 🧹  Clear all tasks
    [9] 🚪  Exit
    """)

def print_tasks(tasks):
    if not tasks:
        print("⚠️  No tasks available.")
    else:
        print("\nYour Tasks:")
        print("-"*40)
        for idx, item in enumerate(tasks, 1):
            name, desc, prio = item.details()
            print(f"{idx}. 🏷️ {name} | 📝 {desc} | 🔥 Priority: {prio}")
        print("-"*40)

def main():
    user_tlist = ToDoList()
    flag = True
    while flag:
        print_header()
        print_menu()
        choice = input("Select an option [1-6]: ").strip()

        if choice == "1":
            print("\n➕ Add New Task")
            name = input("Enter task name: ").strip()
            description = input("Enter task description: ").strip()
            priority = input("Enter task priority: ").strip()
            user_tlist.add_task(name, description, priority)
            print("✅ Task added successfully!")

        elif choice == "2":
            print("\n➖ Remove Task")
            name = input("Enter the name of the task to remove: ").strip()
            user_tlist.remove_task(name)
            print("🗑️ Task removed (if it existed).")

        elif choice == "3":
            user_tlist.save_task()
            print("💾 Tasks saved successfully!")

        elif choice == "4":
            user_tlist.load_tasks()
            print("📂 Tasks loaded successfully!")

        elif choice == "5":
            print_tasks(user_tlist.tasks)

        elif choice == "6":
            res = input("Do you want to save your tasks before exit? (y/n): ").strip()
            if res.lower() == "y":
                user_tlist.save_task()
                print("💾 Tasks saved. Goodbye!")
            print("👋 Exiting To Do List Manager. Have a productive day!")
            flag = False

        else:
            print("❌ Invalid option. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()

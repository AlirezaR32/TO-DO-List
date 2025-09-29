from src.services.todo_list import ToDoList
from src.utils.constants import PRIORITY_LOW, PRIORITY_MEDIUM, PRIORITY_HIGH

def print_header():
    print("\n" + "="*50)
    print("            📝  TO DO LIST MANAGER  📝")
    print("="*50)

def print_menu():
    print("""
    [1] ➕  Add new task
    [2] ➖  Remove task
    [3] 📝  Update task
    [4] 💾  Save tasks to storage
    [5] 📂  Load tasks from storage
    [6] 📋  Show all tasks
    [7] 📊  Show tasks by priority
    [8] 🧹  Clear all tasks
    [9] 🚪  Exit
    """)

def print_tasks(tasks):
    if not tasks:
        print("\n⚠️  No tasks available.")
        print("-"*50)
    else:
        print("\n📋 Your Tasks:")
        print("-"*50)
        for idx, item in enumerate(tasks, 1):
            name, desc, prio = item.details()
            print(f"{idx}. 🏷️ {name} | 📝 {desc} | 🔥 Priority: {prio}")
        print("-"*50)

def get_priority():
    while True:
        print("\n📊 Priority Levels:")
        print(f"1. 🟢 {PRIORITY_LOW}")
        print(f"2. 🟡 {PRIORITY_MEDIUM}")
        print(f"3. 🔴 {PRIORITY_HIGH}")
        choice = input("\nSelect priority level [1-3]: ").strip()
        
        if choice == "1":
            return PRIORITY_LOW
        elif choice == "2":
            return PRIORITY_MEDIUM
        elif choice == "3":
            return PRIORITY_HIGH
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")

def main():
    user_tlist = ToDoList()
    
    # Try to load existing tasks at startup
    try:
        user_tlist.load_tasks()
        if not user_tlist.is_empty():
            print("\n📂 Existing tasks loaded successfully!")
    except:
        print("\n⚠️ No existing tasks found. Starting with empty list.")

    while True:
        print_header()
        print_menu()
        print(f"\n📌 Current tasks count: {user_tlist.count_tasks()}")
        choice = input("\nSelect an option [1-9]: ").strip()

        if choice == "1":
            print("\n➕ Add New Task")
            print("-"*50)
            try:
                name = input("Enter task name: ").strip()
                description = input("Enter task description: ").strip()
                priority = get_priority()
                task = user_tlist.add_task(name, description, priority)
                print(f"\n✅ Task '{task.name}' added successfully!")
            except ValueError as e:
                print(f"\n❌ Error: {str(e)}")

        elif choice == "2":
            if user_tlist.is_empty():
                print("\n⚠️ No tasks to remove!")
            else:
                print("\n➖ Remove Task")
                print("-"*50)
                print_tasks(user_tlist.tasks)
                name = input("\nEnter the name of the task to remove: ").strip()
                removed = user_tlist.remove_task(name)
                if removed:
                    print(f"\n🗑️ Task '{removed.name}' removed successfully!")
                else:
                    print(f"\n❌ Task '{name}' not found!")

        elif choice == "3":
            if user_tlist.is_empty():
                print("\n⚠️ No tasks to update!")
            else:
                print("\n📝 Update Task")
                print("-"*50)
                print_tasks(user_tlist.tasks)
                name = input("\nEnter the name of the task to update: ").strip()
                task = user_tlist.get_task(name)
                if task:
                    print(f"\nCurrent details for '{task.name}':")
                    print(f"Description: {task.description}")
                    print(f"Priority: {task.priority}")
                    
                    update_desc = input("\nEnter new description (or press Enter to keep current): ").strip()
                    if not update_desc:
                        update_desc = None
                    
                    update_prio = input("Update priority? (y/n): ").strip().lower()
                    new_priority = None
                    if update_prio == 'y':
                        new_priority = get_priority()
                    
                    updated = user_tlist.update_task(name, update_desc, new_priority)
                    print(f"\n✅ Task '{updated.name}' updated successfully!")
                else:
                    print(f"\n❌ Task '{name}' not found!")

        elif choice == "4":
            user_tlist.save_task()
            print(f"\n💾 {user_tlist.count_tasks()} tasks saved successfully!")

        elif choice == "5":
            user_tlist.load_tasks()
            print(f"\n📂 {user_tlist.count_tasks()} tasks loaded successfully!")

        elif choice == "6":
            if user_tlist.is_empty():
                print("\n⚠️ No tasks to display!")
            else:
                print_tasks(user_tlist.tasks)

        elif choice == "7":
            if user_tlist.is_empty():
                print("\n⚠️ No tasks to display!")
            else:
                priority = get_priority()
                tasks = user_tlist.get_tasks_by_priority(priority)
                if tasks:
                    print(f"\n📊 Tasks with {priority} priority:")
                    print("-"*50)
                    for idx, task in enumerate(tasks, 1):
                        print(f"{idx}. 🏷️ {task.name} | 📝 {task.description}")
                    print("-"*50)
                else:
                    print(f"\n⚠️ No tasks found with {priority} priority!")

        elif choice == "8":
            if user_tlist.is_empty():
                print("\n⚠️ No tasks to clear!")
            else:
                confirm = input("\n⚠️ Are you sure you want to clear all tasks? (y/n): ").strip().lower()
                if confirm == 'y':
                    count = user_tlist.count_tasks()
                    user_tlist.clear_tasks()
                    print(f"\n🧹 {count} tasks cleared successfully!")
                else:
                    print("\n❌ Operation cancelled.")

        elif choice == "9":
            if not user_tlist.is_empty():
                save = input("\nDo you want to save your tasks before exit? (y/n): ").strip().lower()
                if save == "y":
                    user_tlist.save_task()
                    print("\n💾 Tasks saved successfully!")
            print("\n👋 Exiting To Do List Manager. Have a productive day!")
            break

        else:
            print("\n❌ Invalid option. Please choose a number between 1-9.")
        
        if choice != "9":
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
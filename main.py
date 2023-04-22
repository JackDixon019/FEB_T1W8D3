from todo_functions import add_todo, mark_todo, remove_todo, view_todo

from colored import fg, bg, attr

print(f"{fg('blue')} {bg('yellow')} Welcome to your TODO list {attr('reset')}")

file_name = "list.csv"
# CSV structure:
# Title,completed
# Todo 1,False
# Todo 2. True

# Check if file exists
try:
    todo_file = open(file_name, "r")
    todo_file.close()
    print("In try block")
# If it does not exist, create file
except FileNotFoundError as e:
    todo_file = open(file_name, "w")
    todo_file.write("title,completed\n")
    todo_file.close()
    print("In except block")

def create_menu():
    print("1. Enter 1 to add a new item to your list")
    print("1. Enter 2 to remove an item from your list")
    print("1. Enter 3 to mark an item as completed")
    print("1. Enter 4 to view your todo list")
    print("1. Enter 5 to exit")
    choice = input("Enter your selection: ")
    return choice

user_choice = ""

while user_choice != "5":
    user_choice = create_menu()

    if user_choice == "1":
        add_todo(file_name)
    elif user_choice == "2":
        remove_todo(file_name)
    elif user_choice == "3":
        mark_todo(file_name)
    elif user_choice == "4":
        view_todo(file_name)
    elif user_choice == "5":
        continue
    else:
        print("Invalid input")
    input("Press Enter to continue")

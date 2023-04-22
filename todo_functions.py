import csv
from fileinput import filename
from lib2to3.pgen2.grammar import opmap_raw

def add_todo(file_name):
    print("Add todo")
    todo_title = input("Enter your todo title: ")
    with open(file_name, "a") as todo_file:
        writer = csv.writer(todo_file)
        writer.writerow([todo_title, "False"])

def remove_todo(file_name):
    print("Remove todo")
    # We will read and save all data as a list, EXCEPT for the one we want to remove
    # Then, write this list back in the file
    todo_title = input("Enter the todo title that you want to remove: ")
    todo_lists = []
    with open(file_name, "r") as todo_file:
        reader = csv.reader(todo_file)
        for row in reader:
            if todo_title != row[0]:
                todo_lists.append(row)
    print(todo_lists)
    with open(file_name, "w") as todo_file:
        writer = csv.writer(todo_file)
        writer.writerows(todo_lists)
    print(f"Your new todo list is: ")
    view_todo(file_name)


def mark_todo(file_name):
    print("Mark todo")
    view_todo(file_name)
    todo_title = input("Enter the todo title that you want to mark as complete: ")
    todo_lists = []
    with open(file_name, "r") as todo_file:
        reader = csv.reader(todo_file)
        for row in reader:
            if todo_title == row[0]:
                todo_lists.append([todo_title, "True"])
            else:
                todo_lists.append(row)
    with open(file_name, "w") as todo_file:
        writer = csv.writer(todo_file)
        writer.writerows(todo_lists)


def view_todo(file_name):
    with open(file_name, "r") as todo_file:
        reader = csv.reader(todo_file)
        reader.__next__()
        for row in reader:
            if row[1] == "True":
                print(f"Todo {row[0]} is completed")
            else:
                print(f"Todo {row[0]} is not completed")

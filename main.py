from logic import add_tasks, complete_tasks, remove_task, list_tasks
from storage import save_tasks, load_tasks
import os

tasks = load_tasks()

def main():
    print_menu()
    menu_read()

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    print("----Welcome the task tracker----")
    print("to continue choose any function")
    print("1- Add tasks")
    print("2- Complete tasks")
    print("3- Remove tasks")
    print("4- List tasks")
    print("5- Clean console")
    print("6- Exit")

def menu_read():
    while(True):
        choose = int(input('Type a number: '))
        if choose >= 1 and choose <= 6:
            if choose == 1:
                title = str(input("Title of the task: "))
                date = str(input("Date of the task: "))
                priority = int(input("Please type the priority of the task (1/2/3): "))
                add_tasks(tasks, title, date, priority)
                save_tasks(tasks)
                print_menu()
            elif choose == 2:
                id = int(input('Please type the ID of the task that you want classify as complete: '))
                tf = complete_tasks(tasks, id)
                if tf == True:
                    save_tasks()
                    clean()
                    print("Task completed")
                elif tf == False:
                    clean()
                    print("ID NOT FOUND")
                print_menu()
            elif choose == 3:
                id = int(input("Please type the ID of the task that you want remove: "))
                tf = remove_task(tasks, id)
                if tf == True:
                    save_tasks(tasks)
                    clean()
                    print("Task removed")
                elif tf == False:
                    clean()
                    print("ID NOT FOUND")
                print_menu()
            elif choose == 4:
                priority = int(input("Please type the priority of the tasks that you want to list (1/2/3 and 4 for list done tasks): "))
                list_tasks(tasks, priority)
            elif choose == 5:
                clean()
                print_menu()
            elif choose == 6:
                break
        else:
            print('Please type a valid number!!')
            print_menu()
if __name__ == "__main__":
    main()


def add_tasks(tasks, title, date, priority):
    if not tasks:
        new_id = 1
    else:
        ids = []
        for task in tasks:
            ids.append(task["id"])
        new_id = max(ids) + 1
    task = {
        "id": new_id,
        "title": title,
        "date": date,
        "priority": priority,
        "done": False
        
    }
    tasks.append(task)

def  list_tasks(tasks, priority): 
    def print_tasks(task):
            print(f'ID: {task["id"]}')
            print(f'Title: {task["title"]}')
            print(f'Date: {task["date"]}')
            if task["done"] == False:
                status = "Pending"
            elif task["done"] == True:
                status = "Done"
            print(f'Status: {status}')
    if not tasks:
        print("None tasks found")
    else:
        priority1 = []
        priority2 = []
        priority3 = []
        done = [] # done will show all tasks that already've been done, without consider its priority
        for task in tasks:
            if task["priority"] == 1:
                priority1.append(task)
            elif task["priority"] == 2:
                priority2.append(task)
            elif task["priority"] == 3:
                priority3.append(task)
            if task["done"]:
                done.append(task)
        if priority == 1:
            for task in priority1:
                if task["done"]: 
                    continue
                else:
                    print_tasks(task)
        elif priority == 2:
            for task in priority2:
                if task["done"]: 
                    continue
                else:
                    print_tasks(task)
        elif priority == 3:
            for task in priority3:
                if task["done"]: 
                    continue
                else:
                    print_tasks(task)
        elif priority == 4: #that will show all done tasks
            for task in done:
                    print_tasks(task)
def complete_tasks(tasks, id):
    for task in tasks:
        if task["id"] == id:
            task["done"] = True
            return True
    return False

    
def remove_task(tasks, id):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return True
    return False
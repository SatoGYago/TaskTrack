import json

def load_tasks():
    try:
        with open('tasks.json', 'r', encoding='utf-8') as file:
            tasks = json.load(file)
            return tasks
    except (FileNotFoundError, EOFError, json.JSONDecodeError):
        tasks = []
        return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)
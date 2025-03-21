import json
import os
from task_manager.logger import setup_logger

logger = setup_logger()
TASKS_FILE = os.getenv("TASKS_FILE_PATH", "tasks.json")

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            tasks = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description, priority):
    tasks = load_tasks()
    task_id = max([task["id"] for task in tasks], default=0) + 1
    task = {"id": task_id, "description": description, "priority": priority}
    tasks.append(task)
    save_tasks(tasks)
    return task

def list_tasks():
    return load_tasks()

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(new_tasks) == len(tasks):
        return False  # Aucune tâche supprimée
    save_tasks(new_tasks)
    return True

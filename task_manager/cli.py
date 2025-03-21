import argparse
from task_manager.core import add_task, list_tasks, delete_task
from task_manager.logger import setup_logger

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Sous-commande pour ajouter une tâche
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Task description")
    add_parser.add_argument("--priority", type=int, default=1, help="Task priority")

    # Sous-commande pour lister les tâches
    list_parser = subparsers.add_parser("list", help="List all tasks")

    # Sous-commande pour supprimer une tâche
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("task_id", type=int, help="ID of the task to delete")

    args = parser.parse_args()

    if args.command == "add":
        task = add_task(args.description, args.priority)
        logger.info(f"Added task: {task}")
        print(f"Task added: {task}")
    elif args.command == "list":
        tasks = list_tasks()
        if tasks:
            print("Tasks:")
            for task in tasks:
                print(task)
        else:
            print("No tasks found.")
    elif args.command == "delete":
        result = delete_task(args.task_id)
        if result:
            logger.info(f"Deleted task with ID: {args.task_id}")
            print(f"Task with ID {args.task_id} deleted.")
        else:
            logger.error(f"Task with ID {args.task_id} not found.")
            print(f"Task with ID {args.task_id} not found.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

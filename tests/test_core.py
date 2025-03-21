import os
import json
import unittest
from task_manager.core import add_task, load_tasks, delete_task

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        # Utiliser un fichier de test pour les tâches
        self.test_file = "test_tasks.json"
        os.environ["TASKS_FILE_PATH"] = self.test_file
        # Créer un fichier vide
        with open(self.test_file, "w") as f:
            json.dump([], f)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_task(self):
        task = add_task("Test Task", 2)
        self.assertEqual(task["description"], "Test Task")
        self.assertEqual(task["priority"], 2)
        tasks = load_tasks()
        self.assertIn(task, tasks)

    def test_delete_task(self):
        task = add_task("Task to Delete", 1)
        tasks = load_tasks()
        self.assertIn(task, tasks)
        result = delete_task(task["id"])
        self.assertTrue(result)
        tasks_after = load_tasks()
        self.assertNotIn(task, tasks_after)

if __name__ == "__main__":
    unittest.main()

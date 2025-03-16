# tests/test_task.py
import unittest
from models.task import Task
from controllers.task_controller import TaskController

class TestTask(unittest.TestCase):
    def test_add_task(self):
        controller = TaskController()
        task = controller.add_task("Estudar Python")
        self.assertEqual(task.description, "Estudar Python")
        self.assertFalse(task.completed)

    def test_complete_task(self):
        controller = TaskController()
        controller.add_task("Estudar Python")
        self.assertTrue(controller.complete_task(1))
        self.assertFalse(controller.complete_task(99))  # ID inválido

if __name__ == "__main__":
    unittest.main()
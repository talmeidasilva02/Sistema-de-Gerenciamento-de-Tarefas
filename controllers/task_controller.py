# controllers/task_controller.py
from typing import List
from models.task import Task

class TaskController:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, description: str) -> Task:
        task_id = len(self.tasks) + 1
        task = Task(task_id, description)
        self.tasks.append(task)
        return task

    def complete_task(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.task_id == task_id:
                task.completed = True
                return True
        return False

    def remove_task(self, task_id: int) -> bool:
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        return True

    def list_tasks(self) -> List[Task]:
        return self.tasks
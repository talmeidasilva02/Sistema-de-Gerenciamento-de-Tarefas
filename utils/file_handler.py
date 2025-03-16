# utils/file_handler.py
import json
from typing import List, Dict
from models.task import Task

class FileHandler:
    @staticmethod
    def save_tasks(file_path: str, tasks: List[Task]):
        with open(file_path, "w") as file:
            json.dump([task.__dict__ for task in tasks], file)

    @staticmethod
    def load_tasks(file_path: str) -> List[Task]:
        try:
            with open(file_path, "r") as file:
                tasks_data = json.load(file)
                return [Task(**data) for data in tasks_data]
        except FileNotFoundError:
            return []
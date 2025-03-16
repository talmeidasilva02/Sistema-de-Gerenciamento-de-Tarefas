# models/task.py
class Task:
    def __init__(self, task_id: int, description: str, completed: bool = False):
        self.task_id = task_id
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "Concluída" if self.completed else "Pendente"
        return f"Tarefa #{self.task_id}: {self.description} [{status}]"
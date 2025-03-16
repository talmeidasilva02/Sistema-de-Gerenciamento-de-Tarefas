# main.py
from controllers.task_controller import TaskController
from views.task_view import TaskView
from utils.file_handler import FileHandler

def main():
    file_path = "tasks.json"
    tasks = FileHandler.load_tasks(file_path)

    controller = TaskController()
    controller.tasks = tasks

    view = TaskView(controller)
    view.run()

    FileHandler.save_tasks(file_path, controller.tasks)

if __name__ == "__main__":
    main()
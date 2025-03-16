# views/task_view.py
from controllers.task_controller import TaskController

class TaskView:
    def __init__(self, controller: TaskController):
        self.controller = controller

    def show_menu(self):
        print("\n--- To-Do List ---")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Concluir Tarefa")
        print("4. Remover Tarefa")
        print("5. Sair")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Escolha uma opção: ")

            if choice == "1":
                description = input("Descrição da tarefa: ")
                self.controller.add_task(description)
                print("Tarefa adicionada!")

            elif choice == "2":
                tasks = self.controller.list_tasks()
                for task in tasks:
                    print(task)

            elif choice == "3":
                task_id = int(input("ID da tarefa para concluir: "))
                if self.controller.complete_task(task_id):
                    print("Tarefa concluída!")
                else:
                    print("Tarefa não encontrada.")

            elif choice == "4":
                task_id = int(input("ID da tarefa para remover: "))
                if self.controller.remove_task(task_id):
                    print("Tarefa removida!")
                else:
                    print("Tarefa não encontrada.")

            elif choice == "5":
                break

            else:
                print("Opção inválida. Tente novamente.")
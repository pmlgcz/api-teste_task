# Criação da classe Task
class Task:
    def __init__(self, description):
        self.description = description

# Criação da classe TaskList
class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print("Tarefa adicionada com sucesso.")

    def list_tasks(self):
        if len(self.tasks) == 0:
            print("Não há tarefas na lista.")
        else:
            print("Tarefas na lista:")
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task.description}")

    def remove_task(self, task_number):
        try:
            task = self.tasks.pop(task_number-1)
            print(f"Tarefa '{task.description}' removida com sucesso.")
        except IndexError:
            print("Não foi possível remover a tarefa. Número inválido.")

# Criação da função main para interação com o usuário
def main():
    task_list = TaskList()
    while True:
        print("\nO que deseja fazer?")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Remover tarefa")
        print("4. Sair")

        choice = input("Digite o número da opção desejada: ")
        if choice == "1":
            description = input("Digite a descrição da tarefa: ")
            task_list.add_task(description)
        elif choice == "2":
            task_list.list_tasks()
        elif choice == "3":
            task_number = int(input("Digite o número da tarefa que deseja remover: "))
            task_list.remove_task(task_number)
        elif choice == "4":
            break
        else:
            print("Opção inválida. Por favor, digite um número de 1 a 4.")

if __name__ == "__main__":
    main()

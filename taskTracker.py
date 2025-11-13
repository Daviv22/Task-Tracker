import json
from datetime import datetime

def add_task():

    tasksList = get_json_file()

    task = {
        "id": "",
        "description": "",
        "status": "",
        "createdAt": "",
        "updatedAt": ""
    }

    task["id"] = len(tasksList)
    description = input("Adicione uma descrição da tarefa: ")
    task["description"] = description
    task["status"] = "A fazer"
    task["createdAt"] = get_data()

    tasksList.append(task)

    send_json_file(tasksList)

def update_task():
    tasksList = get_json_file()

    tarefa = int(input("Digite o id da tarefa: "))
    tasksList[tarefa]["description"] = input("Digite a nova descrição: ")
    tasksList[tarefa]["updatedAt"] = get_data()

    send_json_file(tasksList)


def delete_task():
    tasksList = get_json_file()

    id = int(input("Que tarefa você quer remover? "))
    tasksList[:] = [item for item in tasksList if item["id"] != id]

    send_json_file(tasksList)

def list_tasks():
    tasksList = get_json_file()
    status = input("Listas marcadas como ... ")
    for task in tasksList:
        for x, y in task.items():
            if task["status"] == status:
                print(x, y)
            elif status == "Todas":
                print(x, y)
        print("\n========== // ==========\n")

def mark_task():
    tasksList = get_json_file()

    id = int(input("Que tarefa você quer marcar? "))
    print("Quer marcar como...")
    print("\t1 - A fazer")
    print("\t2 - Fazendo")
    print("\t3 - Feito")
    status = int(input("Digite: "))
    if status == 1:
        tasksList[id]["status"] = "A fazer"
    if status == 2:
        tasksList[id]["status"] = "Fazendo"
    if status == 3:
        tasksList[id]["status"] = "Feito"

    send_json_file(tasksList)

def get_json_file():
    with open("tasks.json", "r") as f:
        data = json.load(f)

    return data

def send_json_file(tasksList):
    with open("tasks.json", "w") as f:
        json.dump(tasksList, f, indent=4)

def check_decision(decisao):

    if decisao == 1:
        return add_task()
    if decisao == 2:
        return update_task()
    if decisao == 3:
        return delete_task()
    if decisao == 4:
        return mark_task()
    if decisao == 5:
        return list_tasks()
    
    return None

def get_data():
    data = datetime.now()
    data = f"{data.year}-{data.month}-{data.day} {data.hour}:{data.minute}"

    return data

def run_app():

    while True:

        print("O que você gostaria de fazer: ")
        print("\t1 - Adicionar tarefa")
        print("\t2 - Atualizar tarefa")
        print("\t3 - Deletar tarefa")
        print("\t4 - Marcar tarefa como ...")
        print("\t5 - Listar tarefas ...")

        decisao = int(input("Digite: "))
        check_decision(decisao)

run_app()


import json
from datetime import datetime

tasksList = []

def add_task():

    task = {
        "id": "",
        "description": "",
        "status": "",
        "createdAt": "",
        "updatedAt": ""
    }

    description = input("Adicione uma descrição da tarefa: ")
    task["description"] = description
    status = input("Adicione o status da tarefa: ")
    task["status"] = status
    data = datetime.now()
    task["createdAt"] = f"{data.year}-{data.month}-{data.day} {data.hour}:{data.minute}"

    tasksList.append(task)

def update_task():
    tarefa = int(input("Digite o id da tarefa: "))
    print("O que você gostaria de mudar:")
    print("\t1 - Descrição da tarefa")
    print("\t2 - Status da tarefa")
    escolha = int(input("Digite: "))

    if escolha == 1:
        tasksList[tarefa]["description"] = input("Digite a nova descrição: ")
        data = datetime.now()
        tasksList[tarefa]["updateAt"] = f"{data.year}-{data.month}-{data.day} {data.hour}:{data.minute}"
    if escolha == 2:
        data = datetime.now()
        tasksList[tarefa]["status"] = input("Digite o novo status: ")
        tasksList[tarefa]["updateAt"] = f"{data.year}-{data.month}-{data.day} {data.hour}:{data.minute}"


def delete_task():
    pass

def list_tasks():
    pass

def mark_task():
    pass

def json_file():
    pass

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

"""
    tasksLists = []

    taskStructure = {
        "id": "",
        "description": "",
        "status": "",
        "createdAt": "",
        "updatedAt": ""
    }
    with open("teste.json", "a") as f:
        json.dump(tasksLists, f)
"""


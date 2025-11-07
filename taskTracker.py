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

    task["id"] = len(tasksList)
    description = input("Adicione uma descrição da tarefa: ")
    task["description"] = description
    task["status"] = "A fazer"
    task["createdAt"] = get_data()

    tasksList.append(task)

def update_task():
    tarefa = int(input("Digite o id da tarefa: "))
    tasksList[tarefa]["description"] = input("Digite a nova descrição: ")
    tasksList[tarefa]["updatedAt"] = get_data()


def delete_task():
    id = int(input("Que tarefa você quer remover? "))
    tasksList[:] = [item for item in tasksList if item["id"] != id]
    for i, task in enumerate(tasksList):
        task["id"] = i

def list_tasks():
    for task in tasksList:
        print(task)

def mark_task():
    id = int(input("Que tarefa você quer marcar? "))
    print("Quer marcar como...")
    print("\t1 - A fazer")
    print("\t2 - Fazendo")
    print("\t3 - Feito")

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


import json
import datetime

def add_task():
    pass

def update_task():
    pass

def delete_task():
    pass

def list_tasks():
    pass

def mark_task():
    pass

def json_file():
    tasksList = []

    taskStructure = {
        "id": "",
        "description": "",
        "status": "",
        "createdAt": "",
        "updatedAt": ""
    }

def check_decision(decisao):

    if decisao == 1:
        return add_task()
    if decisao == 2:
        return update_task()
    if decisao == 3:
        return delete_task()
    if decisao == 4():
        return mark_task()
    if decisao == 5:
        return list_tasks()

def run_app():
    while True:
        print("O que você gostaria de fazer: ")
        print("\t1 - Adicionar tarefa")
        print("\t2 - Atualizar tarefa")
        print("\t3 - Deletar tarefa")
        print("\t4 - Marcar tarefa como ...")
        print("\t5 - Listar tarefas ...")
        decisao = input("Digite: ")
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


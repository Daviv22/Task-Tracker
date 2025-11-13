import json
from datetime import datetime

def add_task(task_name):

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

def update_task(task_id, task_name):
    tasksList = get_json_file()

    tasksList[task_id]["description"] = task_name
    tasksList[task_id]["updatedAt"] = get_data()

    send_json_file(tasksList)


def delete_task(task_id):
    tasksList = get_json_file()

    tasksList[:] = [item for item in tasksList if item["id"] != task_id]

    send_json_file(tasksList)

def list_tasks():
    tasksList = get_json_file()
    for task in tasksList:
        for x, y in task.items():
            print(x, y)
        print("\n========== // ==========\n")

def mark_task(task_id, status):
    tasksList = get_json_file()
    
    tasksList[task_id]["status"] = status

    send_json_file(tasksList)

def get_json_file():
    with open("teste.json", "r") as f:
        data = json.load(f)

    return data

def send_json_file(tasksList):
    with open("teste.json", "w") as f:
        json.dump(tasksList, f, indent=4)

def get_data():
    data = datetime.now()
    data = f"{data.year}-{data.month}-{data.day} {data.hour}:{data.minute}"

    return data
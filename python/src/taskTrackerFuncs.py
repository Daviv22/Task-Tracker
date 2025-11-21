import json
from datetime import datetime
import os

json_path = os.path.join(os.path.dirname(__file__), "tasks.json")

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
    task["description"] = task_name
    task["status"] = "A Fazer"
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

def list_tasks(status):
    tasksList = get_json_file()
    for task in tasksList:
        print("\n========== // ==========\n")
        print(f"ID: {task["id"]}")
        print(f"Description: {task["description"]}")
        print(f"Status: {task["status"]}")
        print(f"Created at: {task["createdAt"]}")
        if task["updatedAt"]:
            print(f"Updated at: {task["updatedAt"]}")
    
    print("\n========== // ==========\n")

def mark_task(task_id, status):
    tasksList = get_json_file()
    
    tasksList[task_id]["status"] = status
    tasksList[task_id]["updatedAt"] = get_data()

    send_json_file(tasksList)

def get_json_file():
    with open(json_path, "r") as f:
        data = json.load(f)

    return data

def send_json_file(tasksList):
    with open(json_path, "w") as f:
        json.dump(tasksList, f, indent=4)

def get_data():
    data = datetime.now()
    data = f"{data.year}-{data.month}-{data.day} {data.hour}:{data.minute}"

    return data
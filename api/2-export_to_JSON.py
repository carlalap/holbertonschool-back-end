#!/usr/bin/python3
""" Export to JSON """
import json
import requests
import sys


def export_user_to_json():
    """export user id data to json format"""

    USER_ID = sys.argv[1]

    user_data = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(USER_ID)).json()
    todo_data = requests.get('https://jsonplaceholder.typicode.com/todos',
                             params={"userId": USER_ID}).json()
    EMPLOYEE_UN = user_data.get("username")
    EMPLOYEE_NAME = user_data.get("name")

    counter = 0
    task_list = []
    complete_status_list = []
    for thing in todo_data:
        counter += 1
        task_list.append(thing.get("title"))
        complete_status_list.append(thing.get("completed"))

    json_list = []
    for i in range(counter):
        new_dict = {
            "task": task_list[i],
            "completed": complete_status_list[i],
            "username": EMPLOYEE_UN
        }
        json_list.append(new_dict)

    json_dict = {
        f"{USER_ID}": json_list
    }


if __name__ == "__main__":
    export_user_to_json()

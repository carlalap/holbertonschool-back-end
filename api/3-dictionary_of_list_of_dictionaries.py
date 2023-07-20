#!/usr/bin/python3
"""
Python script that uses a REST API
(https://jsonplaceholder.typicode.com/),
to export data in the JSON format.
"""
import json
import requests
import sys
from sys import argv

if __name__ == "__main__":
    get_id = set()
    request = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = request.json()

    for user in data:
        get_id.add(user.get("userId"))
    file_export = {}
    url_u = "https://jsonplaceholder.typicode.com/users/{}"
    url_todos = "https://jsonplaceholder.typicode.com/todos?userId={}"

    for user in get_id:
        url_users = request.get(url_u.format(user))
        url_name = url_users.json().get("username")
        url_users = request.get(url_todos.format(user))
        data_request = url_users.json()
        file_export['{}'.format(user)] = []

        for task in data_request:
            file_export['{}'.format(user)].append()

    for task in data:
        file_export["{}".format(argv[1])].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": url_name
        })

    with open('todo_all_employees.json', mode='w') as file:
        json.dump({int(x): file_export[x] for x in file_export.keys()},
                   file, sort_keys=True)

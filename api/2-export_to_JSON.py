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
        url_users = "https://jsonplaceholder.typicode.com/users/{}"
        url_todos = "https://jsonplaceholder.typicode.com/todos?userId={}"
        url = requests.get(url_users.format(argv[1]))
        data_name = url.json().get('username')
        url = requests.get(url_todos.format(argv[1]))
        data = url.json()
        file_export = {}
        file_export["{}".format(argv[1])] = []
        for task in data:
                file_export["{}".format(argv[1])].append({
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": data_name})

        with open("{}.json".format(argv[1]), mode="w") as file_json:
                json.dump(file_export, file_json)

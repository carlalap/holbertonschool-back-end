#!/usr/bin/python3
"""
Python script that uses a REST API
(https://jsonplaceholder.typicode.com/), for a given
employee ID, returns information about his/her TODO list progress
"""
import json
import requests
import sys
from sys import argv

if __name__ == "__main__":
        url_users = "https://jsonplaceholder.typicode.com/users/{}"
        url_todos = "https://jsonplaceholder.typicode.com/todos?userId={}"
        url = requests.get(url_users.format(argv[1]))
        data_name = url.json().get('name')
        url = requests.get(url_todos.format(argv[1]))
        data = url.json()
        done = 0
        total = 0
        for task in data:
                total += 1
                if task.get("completed"):
                        done += 1
        first_line = "Employee {} is done with tasks({}/{}):"
        print(first_line.format(data_name, done, total))
        for task in data:
                if task.get("completed"):
                        print("\t {}".format(task.get("title")))

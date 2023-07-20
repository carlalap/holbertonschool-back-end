#!/usr/bin/python3
"""
Python script that uses a REST API
(https://jsonplaceholder.typicode.com/),
to export data in the CSV format.
"""
import csv
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
        with open("{}.csv".format(argv[1]), mode="w") as file_csv:
                file_write = csv.writer(file_csv, delimiter=',', quotechar='"',
                                        quoting=csv.QUOTE_ALL)
                for task in data:
                        file_write.writerow([argv[1], data_name,
                                            task.get("completed"),
                                            task.get("title")]
                                            )

#!/usr/bin/python3
"""
Python script that uses a REST API
(https://jsonplaceholder.typicode.com/),
to export data in the JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"
    todos_url = f"{base_url}/todos"

    try:
        users_response = requests.get(users_url)
        users_response.raise_for_status()
        users_data = users_response.json()

        all_employees_tasks = {}

        for user in users_data:
            user_id = user["id"]
            username = user["username"]

            todos_response = requests.get(todos_url,
                                          params={"userId": user_id})
            todos_response.raise_for_status()
            todos_data = todos_response.json()

            user_tasks = []
            for task in todos_data:
                task_title = task["title"]
                task_completed = task["completed"]

                user_tasks.append({
                    "username": username,
                    "task": task_title,
                    "completed": task_completed
                })

            all_employees_tasks[user_id] = user_tasks

        with open("todo_all_employees.json", mode="w") as file_json:
            json.dump(all_employees_tasks, file_json)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
    except ValueError:
        print("Error: Invalid JSON response.")
        sys.exit(1)

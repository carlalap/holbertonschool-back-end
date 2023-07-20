#!/usr/bin/python3
"""
Python script that uses a REST API
(https://jsonplaceholder.typicode.com/), for a given
employee ID, returns information about his/her TODO list progress
"""
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # define the base URL of the REST API
        employee_response = requests.get(employee_url)
        todo_response = requests.get(todo_url)

        employee_response.raise_for_status()
        todo_response.raise_for_status()

        employee_data = employee_response.json()
        todo_data = todo_response.json()

        employee_name = employee_data["name"]
        done_tasks = [task for task in todo_data if task["completed"]]
        total_tasks = len(todo_data)

        print(f"Employee {employee_name} is done with tasks
              ({len(done_tasks)}/{total_tasks}): ")

        for task in done_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
    except KeyError:
        print("Error: Employee not found.")
        sys.exit(1)
    except ValueError:
        print("Error: Invalid JSON response.")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

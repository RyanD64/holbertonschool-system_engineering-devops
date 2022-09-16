#!/usr/bin/python3
"""script that returns information about a given employee"""
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    user = f"https://jsonplaceholder.typicode.com/users/{id}"
    todo = f"https://jsonplaceholder.typicode.com/users/{id}/todos"

    users = requests.get(user).json()
    TODO = requests.get(todo).json()

    num_task_done = 0
    all = 0
    done = []

    for task in TODO:
        all += 1
        if task.get("completed") is True:
            num_task_done += 1
            done.append(task.get("title"))

    response = "Employee {} is done with tasks({}/{}):"
    print(response.format(users.get("name"), num_task_done, all))
    for task in done:
        print("\t {}".format(task))
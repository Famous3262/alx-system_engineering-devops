#!/usr/bin/python3
"""A script using REST API for to-do lists of an  employee"""

import requests
import sys


if __name__ == '__main__':
    employee_Id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employee_Id

    response = requests.get(url)
    employee_Name = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    num_tasks = response.json()
    done = 0
    done_tasks = []

    for task in num_tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_Name, done, len(num_tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))

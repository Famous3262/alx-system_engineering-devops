#!/usr/bin/python3
"""A script using  REST API for to_do lists of an employee
and export data in JSON format
"""

import json
import requests
import sys


if __name__ == '__main__':
    employee_Id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employee_Id

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    num_tasks = response.json()

    dictionary = {employee_Id: []}
    for task in num_tasks:
        dictionary[employee_Id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(employee_Id), 'w') as filename:
        json.dump(dictionary, filename)

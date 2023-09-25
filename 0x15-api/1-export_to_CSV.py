#!/usr/bin/python3
"""A script using REST API for to_do lists of an employee
and export data in the CSV format
"""

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

    with open('{}.csv'.format(employee_Id), 'w') as file:
        for task in num_tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employee_Id, username, task.get('completed'),
                               task.get('title')))

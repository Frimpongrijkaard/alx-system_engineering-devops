#!/usr/bin/python3
"""Python script that returns information about employees"""

import json
import requests
import sys


if __name__ == '__main__':
    employee_Id = sys.argv[1]
    base_Url = "https://jsonplaceholder.typicode.com/users"
    url = base_Url + "/" + employee_Id

    response = requests.get(url)
    username = response.json().get('username')

    to_do_Url = url + "/todos"
    response = requests.get(to_do_Url)
    tasks = response.json()

    dic = {employee_Id: []}
    for tsk in tasks:
        dic[employee_Id].append({
            "task": tsk.get('title'),
            "completed": tsk.get('completed'),
            "username": username
        })
    with open('{}.json'.format(employee_Id), 'w') as filename:
        json.dump(dic, filename)

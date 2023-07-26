#!/usr/bin/python3
"""Python script that returns information about employees"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    users = response.json()

    dic = {}
    for user in users:
        userid = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        response = requests.get(url)
        tasks = response.json()
        dic[user_id] = []
        for tsk in tasks:
            dic[user_id].append({
                "task": tsk.get('title'),
                "completed": tsk.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dic, file)

#!/usr/bin/python3
"""Python script that returns information about employees"""

import requests
import sys


if __name__ == '__main__':
    employee_Id = sys.argv[1]
    base_Url = "https://jsonplaceholder.typicode.com/users"
    url = base_Url + "/" + employee_Id

    response = requests.get(url)
    employee_Name = response.json().get('name')

    to_do_Url = url + "/todos"
    response = requests.get(to_do_Url)
    tasks = response.json()
    work_done = 0
    tasks_done = []

    for tsk in tasks:
        if tsk.get('completed'):
            tasks_done.append(tsk)
            work_done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_Name, work_done, len(tasks)))

    for tsk in tasks_done:
        print("\t {}".format(tsk.get('title')))

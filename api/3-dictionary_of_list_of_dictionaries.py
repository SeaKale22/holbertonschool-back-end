#!/usr/bin/python3
"""
Uses API to return info on all employees' progress
"""


if __name__ == "__main__":
    import requests
    import json

    def all_employees_tasks():
        """
        method for getting exporting to a cvs data from api
        """
        # define api url
        api_url = 'https://jsonplaceholder.typicode.com/'

        # use get to get employee data
        employee_request = requests.get(f'{api_url}users/')
        # jsonise to get data
        employee_data = employee_request.json()
        # create dict for organized data
        organized_data = {}
        # get each employee and their task info
        for employee in employee_data:
            user_id = employee['id']
            username = employee['username']
            # fetch each task for employee
            tasks_request = requests.get(f'{api_url}todos?userId={user_id}')
            tasks_data = tasks_request.json()
            # create task list
            tasks_list = []
            for task in tasks_data:
                tasks_list.append({"username": username, "task": task['title'], "completed": task['completed']})
            # Add the tasks list to the organized data
            organized_data[user_id] = tasks_list

        json_file = 'todo_all_employees.json'
        # open and dump data
        with open(json_file, 'w') as file:
            json.dump(organized_data, file)

    # Call the function to get and display employees progress
    all_employees_tasks()

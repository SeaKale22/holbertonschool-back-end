#!/usr/bin/python3
"""
Uses API to return info on given employee's progress
"""


if __name__ == "__main__":
    import requests
    import json
    import sys

    def employee_to_do_progress_cvs_export(employee_id):
        """
        method for getting exporting to a cvs data from api
        """
        # define api url
        api_url = 'https://jsonplaceholder.typicode.com/'

        # use get to get employee data
        employee_request = requests.get(f'{api_url}users/{employee_id}')
        # jsonise to get data
        employee_data = employee_request.json()
        # get emplyee info
        employee_name = employee_data.get('username')

        # get todo list
        todo_request = requests.get(f'{api_url}todos?userId={employee_id}')
        # get data
        todo_data = todo_request.json()
        total_tasks = len(todo_data)
        completed_tasks = sum(task['completed'] for task in todo_data)
        # create json dict for data to export
        json_data = {}
        task_list = []
        # create task dictionary for list
        for task in todo_data:
            task_dict = {}
            task_dict["task"] = task.get('title')
            task_dict["completed"] = task.get('completed')
            task_dict["username"] = employee_name
            task_list.append(task_dict)
        # add task list to json_data
        json_data[employee_id] = task_list
        json_file = f'{employee_id}.json'

        # open and dump data
        with open(json_file, 'w') as file:
            json.dump(json_data, file)

    # Get the employee ID from the command-line arguments
    employee_id = sys.argv[1]
    # Call the function to get and display employee TODO list progress
    employee_to_do_progress_cvs_export(employee_id)

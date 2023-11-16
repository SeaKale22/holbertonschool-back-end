#!/usr/bin/python3
"""
Uses API to return info on given employee's progress
"""


if __name__ == "__main__":
    import requests
    import sys

    def employee_to_do_progress(employee_id):
        """
        method for getting data from api
        """
        # define api url
        api_url = 'https://jsonplaceholder.typicode.com/'

        # use get to get employee data
        employee_request = requests.get(f'{api_url}users/{employee_id}')
        # jsonise to get data
        employee_data = employee_request.json()
        # get emplyee info
        employee_name = employee_data.get('name')

        # get todo list
        todo_request = requests.get(f'{api_url}todos?userId={employee_id}')
        # get data
        todo_data = todo_request.json()
        total_tasks = len(todo_data)
        completed_tasks = sum(task['completed'] for task in todo_data)

        # print todo list progress
        print("Employee {} is done with tasks({}/{}):"
              .format(employee_name, completed_tasks, total_tasks))
        # Print the titles of completed tasks
        for task in todo_data:
            if task['completed']:
                print(f"\t{task['title']}")

    # Get the employee ID from the command-line arguments
    employee_id = sys.argv[1]
    # Call the function to get and display employee TODO list progress
    employee_to_do_progress(employee_id)

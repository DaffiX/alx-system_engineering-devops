#!/usr/bin/python3
"""API Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an employee ID as an argument.")
        sys.exit()

    url = "https://jsonplaceholder.typicode.com/"
    try:
        user = requests.get(url + "users/{}".format(sys.argv[1])).json()
        todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        sys.exit()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t{}".format(c)) for c in completed]

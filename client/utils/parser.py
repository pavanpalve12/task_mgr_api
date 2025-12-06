import sys

# ------------- Menus -------------------------------------------------
def show_signup_login_menu():
    print(f"{'=' * 20} TO DO CLI {'=' * 20}")
    print("Choose one of the following action,")
    print("    Enter 1 for Signup")
    print("    Enter 2 for Login")
    print("    Enter 0 for Exit")
    print(f"{'=' * (42 + len("TO DO CLI"))}")

def show_task_menu():
    print(f"{'=' * 20} TO DO CLI {'=' * 20}")
    print("Choose one of the following task action,")
    print("    Enter 1 for Add")
    print("    Enter 2 for Replace")
    print("    Enter 3 for Delete")
    print("    Enter 4 for List")
    print("    Enter 5 for Update Task Status")
    print("    Enter 0 for Exit")
    print(f"{'=' * (42 + len("TO DO CLI"))}")

# ------------- user auth  ------------------------------------------------
def take_signup_login_input() -> dict:

    action = input("Choose Action: ")
    if action in ["1", "2", "0"]:
        if int(action) == 1:
            print("You chose signup")
            user_input = _record_signup_input("signup")
        elif int(action) == 2:
            print("You chose Login")
            user_input = _record_login_input("login")
        elif int(action) == 0:
            print("You Chose Exit")
            sys.exit(0)
    else:
        print("Please enter valid choice from 0, 1, 2")
    return user_input

def _record_signup_input(action) -> dict:
    user_name = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    ui_input = {
        "action": action,
        "user_name": user_name,
        "email": email,
        "password": password
    }

    return ui_input

def _record_login_input(action) -> dict:
    user_name = input("Enter username: ")
    password = input("Enter password: ")

    ui_input = {
        "action": action,
        "user_name": user_name,
        "password": password
    }
    return ui_input

# ------------- tasks -------------------------------------------------
def take_task_action_input() -> dict:
    action = input("Choose Action: ")
    if action in ["1", "2", "3", "4", "5", "0"]:
        if int(action) == 1:
            task_input = _record_add_task_input("add_task")
        elif int(action) == 2:
            task_input = _record_update_task_input("replace_task")
        elif int(action) == 3:
            task_input = _record_delete_task_input("delete_task")
        elif int(action) == 4:
            task_input = _record_list_tasks_input("list_tasks")
        elif int(action) == 5:
            task_input = _record_update_task_status_input("update_task_status")
        elif int(action) == 0:
            print("You Chose Exit")
            sys.exit(0)
    else:
        print("Please enter valid choice.")
    return task_input


def _record_add_task_input(action) -> dict:
    title = input("Enter task title: ")
    description = input("Enter task description: ")

    ui_input = {
        "action": action,
        "title": title.title(),
        "description": description.title()
    }
    return ui_input

def _record_replace_task_input(action) -> dict:
    task_id = input("Enter task id: ")
    title = input("Enter task title: ")
    description = input("Enter task description: ")

    ui_input = {
        "action": action,
        "task_id": task_id,
        "title": title.title(),
        "description": description.title()
    }
    return ui_input


def _record_update_task_input(action) -> dict:
    task_id = input("Enter task id: ")
    title = input("Enter task title: ")
    description = input("Enter task description: ")

    ui_input = {
        "action": action,
        "task_id": task_id,
        "title": title.title(),
        "description": description.title()
    }
    return ui_input

def _record_delete_task_input(action) -> dict:
    task_id = input("Enter task id: ")

    ui_input = {
        "action": action,
        "task_id": task_id
    }
    return ui_input

def _record_update_task_status_input(action) -> dict:
    task_id = input("Enter task id: ")
    status = input("Enter task status: ")

    ui_input = {
        "action": action,
        "task_id": task_id,
        "status": status
    }
    return ui_input

def _record_list_tasks_input(action) -> dict:
    status = input("Enter task status: ")
    ui_input = {
        "action": action,
        "status": status
    }
    return ui_input


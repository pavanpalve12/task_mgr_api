# Controller and routing for api calls
from server.services import auth_services as auth_serv
from server.services import token_services as token_serv
from server.services import task_services as task_serv
from server.models import users_models as um
from server.models import tokens_models as tm

from client.utils import tabulate_data as td

from datetime import datetime

db_file = "/Users/pavan/Workspace/00-Tech-Workspace/github/task_mgr_api/server/db/to_do_db.sqlite"
# new uer signup

# email = "steve_jobs@apple.com"
# username = "jobs_apple_founder"
# password = "jobs_apple_founder"
# login_key = "jobs_apple_founder"

email = "pvn1291@gmail.com"
username = "pvn1291"
password = "pvn1291"
login_key = "pvn1291"

end_point_action = "GET/todo"
# test Task details
task_id = 4
title = "attend gym session"
description = "attend gym class at 6 am"
status = ""

# Patch parameters
update_details = {"title": "study python", "description": "Complete python project"}

# sign up user
if end_point_action == "POST/register":
    signup_flag = auth_serv.signup_user(username=username, email=email, password=password)
    if signup_flag:
        print(f"User Registered with -> {username}, {email}")
    else:
        print("User registration failed")

# generate and store token if login is successful
if end_point_action == "POST/login":
    login_flag = auth_serv.login_user(login_key=login_key, password=password)
    if login_flag:
        print(f"User logged in as -> {username}, {email}")

        # check if user have active token
        user_id = um.get_user_id_by_email(email=email)
        token = tm.get_token_by_user_id(user_id=user_id)

        if token:
            print(f"Active token found -> {token}")
        else:
            # store token in tokens table against user
            if token_serv.store_token(user_id=user_id):
                print(f"Token is generated and stored for user -> {user_id}, {email}")
                token = tm.get_token_by_user_id(user_id=user_id)
                print(f"Token for user {email} is -> {token}")
            else:
                print("Token generation failed")
    else:
        print("Login failed")

# POST - add task to to_do_list
if end_point_action == "POST/todo":
    task_details = {
        "user_id": um.get_user_id_by_email(email=email),
        "title": title,
        "description": description,
        "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    if task_serv.add_task(task_details = task_details):
        print(f"Task added successfully -> {task_details}")
    else:
        print("Task creation failed")

# PUT - replace / update entire task with new task
if end_point_action == "PUT/todo":
    task_details = {
        "user_id": um.get_user_id_by_email(email=email),
        "task_id": 4,
        "title": title.title(),
        "description": description.title(),
        "status": "to-do",
        "update_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    flag = task_serv.replace_task(
        user_id=task_details["user_id"],
        task_id=task_details["task_id"],
        title=task_details["title"],
        description=task_details["description"],
        status=task_details["status"],
        update_timestamp=task_details["update_timestamp"]
    )
    if flag:
        print(f"Task is replaced -> {task_details}")
    else:
        print("Task replace failed")

# PATCH - update specific attributes - (title / description / status) -> ensure to update updated_At
if end_point_action == "PATCH/todo":
    flag = task_serv.update_task(
        user_id =um.get_user_id_by_email(email=email),
        task_id= task_id,
        #update_details= update_details,
        update_details={"status": "done"},
        update_timestamp= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    if flag:
        print("Task updated successfully -> ", update_details)
    else:
        print("Task update failed")

# DELETE - delete task -> deactivate task by changing active_status -> update deactivatedAt
if end_point_action == "DELETE/todo":
    flag = task_serv.delete_task(
        user_id=um.get_user_id_by_email(email=email),
        #task_id=task_id,
        task_id=5,
        delete_timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    if flag:
        print("Task deleted successfully")
    else:
        print("Task delete failed")

# GET - list tasks - status (display tasks based on status or full table)
if end_point_action == "GET/todo":
    user_id = um.get_user_id_by_email(email=email)
    result_data = task_serv.list_tasks(user_id=user_id, status=status)

    td.display_data_table(data=result_data)
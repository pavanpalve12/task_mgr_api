# Controller and routing for api calls
from http.client import responses

from server.services import auth_services as auth_serv
from server.services import token_services as token_serv
from server.services import task_services as task_serv
from server.models import users_models as user_model
from server.models import tokens_models as token_model
from server.models import tasks_models as task_model
from server.utils import response_formatting as rf
from server.constants import constant_values as cv

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
task_id = 5
title = "attend cricket session"
description = "attend cricket class at 6 am"
status = ""

# Patch parameters
update_details = {"title": "study python", "description": "Complete python project"}

# sign up user
if end_point_action == "POST/register":
    signup_flag, code = auth_serv.signup_user(email=email, username=username, password=password)
    if signup_flag:
        response = rf.format_response(
            code = code,
            data = [{"username": username, "email": email}]
        )
        print(f"User Registered with -> {response}")
    else:
        response = rf.format_response(code=code)
        print("user registration failed -> ", response)

# generate and store token if login is successful
if end_point_action == "POST/login":
    login_flag, code = auth_serv.login_user(login_key=login_key, password=password)
    if login_flag:
        response = rf.format_response(code = code, data = [{"login_key": login_key}])
        print("User logged in ->", response)
        # check if user have active token
        user_id = user_model.get_user_id_by_email(email=email)
        token = token_model.get_token_by_user_id(user_id=user_id)

        if token:
            print(f"Active token found -> {token}")
        else:
            # store token in tokens table against user
            if token_serv.store_token(user_id=user_id):
                print(f"Token is generated and stored for user -> {user_id}, {email}")
                token = token_model.get_token_by_user_id(user_id=user_id)
                print(f"Token for user {email} is -> {token}")
            else:
                response = rf.format_response(code = "missing_token")
                print("Token generation failed ", response)

    else:
        response = rf.format_response(code=code)
        print("Login failed ", response)

# POST - add task to to_do_list
if end_point_action == "POST/todo":
    task_details = {
        "user_id": user_model.get_user_id_by_email(email=email),
        "title": title,
        "description": description,
        "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    add_flag, code = task_serv.add_task(task_details = task_details)
    if add_flag:
        added_task, _ = task_serv.get_latest_task(user_id=user_model.get_user_id_by_email(email=email))
        response = rf.format_response(code=code, data = added_task)
        print(f"Task added successfully ->", response)
    else:
        response = rf.format_response(code = code)
        print("Task creation failed ", response)

# PUT - replace / update entire task with new task
if end_point_action == "PUT/todo":
    task_details = {
        "user_id": user_model.get_user_id_by_email(email=email),
        "task_id": 9,
        "title": title.title(),
        "description": description.title(),
        "status": "to-do",
        "update_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    replace_flag, code = task_serv.replace_task(
        user_id=task_details["user_id"],
        task_id=task_details["task_id"],
        title=task_details["title"],
        description=task_details["description"],
        status=task_details["status"],
        update_timestamp=task_details["update_timestamp"]
    )
    if replace_flag:
        replaced_task, _ = task_serv.get_task_by_task_id(task_id=task_details["task_id"])
        response = rf.format_response(code=code, data=replaced_task)
        print(f"Task is replaced -> {response}")
    else:
        response = rf.format_response(code=code)
        print("Task replace failed ", response)

# PATCH - update specific attributes - (title / description / status) -> ensure to update updated_At
if end_point_action == "PATCH/todo":
    update_flag, code = task_serv.update_task(
        user_id =user_model.get_user_id_by_email(email=email),
        task_id= task_id,
        #update_details= update_details,
        update_details={"status": "in-progress"},
        update_timestamp= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    if update_flag:
        updated_task, _ = task_serv.get_latest_updated_task(user_id=user_model.get_user_id_by_email(email=email))
        response = rf.format_response(code=code, data=updated_task)
        print(f"Task is updated -> {response}")
    else:
        response = rf.format_response(code=code)
        print("Task update failed ", response)

# DELETE - delete task -> deactivate task by changing active_status -> update deactivatedAt
if end_point_action == "DELETE/todo":
    delete_flag, code = task_serv.delete_task(
        user_id=user_model.get_user_id_by_email(email=email),
        #task_id=task_id,
        task_id=task_id,
        delete_timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    if delete_flag:
        response = rf.format_response(code=code)
        print(f"Task is deleted -> {response}")
    else:
        response = rf.format_response(code=code)
        print("Task delete failed ", response)

# GET - list tasks - status (display tasks based on status or full table)
if end_point_action == "GET/todo":
    user_id = user_model.get_user_id_by_email(email=email)
    result_data, code = task_serv.list_tasks(user_id=user_id)

    if result_data:
        response = rf.format_response(code=code, data = result_data)
        print(f"List task successful -> {response}")
    else:
        response = rf.format_response(code=code)
        print("List task failed ", response)
    td.display_data_table(data=result_data)
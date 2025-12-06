from server.models import tasks_models as tm

# GET actions - LIST Tasks
def list_tasks(user_id: int, status: str = None) -> (list, str):
    result_set, result_set_metadata = [], []
    if not status:
        result_set, result_set_metadata = tm.select_all_tasks(user_id=user_id)
    if status in ["to-do", "in-progress", "done"]:
        result_set, result_set_metadata = tm.select_tasks_by_status(user_id=user_id, status=status)

    if result_set:
        result_data = resultset_to_dict_list(result_set=result_set, result_set_metadata=result_set_metadata)
        return result_data, "list_todos_success"
    else:
        print("No task records in db")
        return result_set, "server_error"


# POST actions - ADD Tasks
def add_task(task_details: dict) -> (bool, str):
    flag = tm.insert_task(task_details=task_details)
    if flag:
        return True, "create_todo_success"
    else:
        return False, "server_error"

# PUT actions - UPDATE Tasks
def replace_task(user_id: int, task_id: int, title: str, description: str, status: str, update_timestamp: str) -> (bool, str):
    flag = tm.replace_task(
        user_id=user_id, task_id=task_id,
        title=title, description=description, status = status,
        update_timestamp=update_timestamp
    )
    if flag:
        return True, "update_todo_success"
    else:
        return False, "server_error"

# PATCH actions - UPDATE Task Attributes
def update_task(user_id: int, task_id: int, update_details: dict, update_timestamp: str) -> (bool, str):
    flag = tm.update_task(
        user_id=user_id, task_id=task_id,
        update_details=update_details,
        update_timestamp=update_timestamp
    )
    if flag:
        return True, "update_todo_success"
    else:
        return False, "server_error"


# DELETE actions - DELETE Task
def delete_task(user_id: int, task_id: int, delete_timestamp: str) -> (bool, str):
    flag = tm.delete_task(user_id=user_id, task_id=task_id, delete_timestamp=delete_timestamp)
    if flag:
        return True, "delete_todo_success"
    else:
        return False, "server_error"

def resultset_to_dict_list(result_set: list, result_set_metadata: list) -> list:
    col_names = [col[0] for col in result_set_metadata]

    result_data = []
    for row in result_set:
        tmp = {}
        for idx, col in enumerate(col_names):
            tmp[col] = row[idx]
            #print(f"{idx} -> {col} -> {row[idx]} -> {result_data}")
        result_data.append(tmp)

    return result_data


def get_latest_updated_task(user_id: str) -> (list, str):
    result_set, result_set_metadata = tm.select_latest_task(user_id=user_id)
    if result_set:
        result_data = resultset_to_dict_list(result_set=result_set, result_set_metadata=result_set_metadata)
        return result_data, "success"
    else:
        print("No task records in db")
        return result_set, "server_error"

def get_latest_task(user_id: str) -> (list, str):
    result_set, result_set_metadata = tm.select_latest_task(user_id=user_id)
    if result_set:
        result_data = resultset_to_dict_list(result_set=result_set, result_set_metadata=result_set_metadata)
        return result_data, "success"
    else:
        print("No task records in db")
        return result_set, "server_error"

def get_task_by_task_id(task_id: str) -> (list, str):
    result_set, result_set_metadata = tm.select_task_by_task_id(task_id=task_id)
    if result_set:
        result_data = resultset_to_dict_list(result_set=result_set, result_set_metadata=result_set_metadata)
        return result_data, "success"
    else:
        print("No task records in db")
        return result_set, "server_error"
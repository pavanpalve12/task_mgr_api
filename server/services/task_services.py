from server.models import tasks_models as tm

# GET actions - LIST Tasks
def list_tasks(user_id: int, status: str) -> list:
    if not status:
        result_set, result_set_metadata = tm.select_all_tasks(user_id=user_id)
    elif status in ["to-do", "in-progress", "done"]:
        result_set, result_set_metadata = tm.select_tasks_by_status(user_id=user_id, status=status)

    if result_set:
        result_data = format_response(result_set=result_set, result_set_metadata=result_set_metadata)
        return result_data
    else:
        print("No task records in db")
        return result_set


# POST actions - ADD Tasks
def add_task(task_details: dict) -> bool:
    return tm.insert_task(task_details=task_details)


# PUT actions - UPDATE Tasks
def replace_task(user_id: int, task_id: int, title: str, description: str, status: str, update_timestamp: str):
    return tm.replace_task(
        user_id=user_id, task_id=task_id,
        title=title, description=description, status = status,
        update_timestamp=update_timestamp
    )


# PATCH actions - UDPATE Task Attributes
def update_task(user_id: int, task_id: int, update_details: dict, update_timestamp: str) -> bool:
    return tm.update_task(
        user_id=user_id, task_id=task_id,
        update_details=update_details,
        update_timestamp=update_timestamp
    )


# DELETE actions - DELETE Task
def delete_task(user_id: int, task_id: int, delete_timestamp: str) -> bool:
    return tm.delete_task(user_id=user_id, task_id=task_id, delete_timestamp=delete_timestamp)


# format response in json format
def format_response(result_set: list, result_set_metadata: list) -> list:
    col_names = [col[0] for col in result_set_metadata]
    print(col_names)
    [print(row) for row in result_set]

    result_data = []
    for row in result_set:
        tmp = {}
        for idx, col in enumerate(col_names):
            tmp[col] = row[idx]
            #print(f"{idx} -> {col} -> {row[idx]} -> {result_data}")
        result_data.append(tmp)

    return result_data

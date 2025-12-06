from server.db import db_utils as du


def insert_task(task_details: dict) -> bool:
    sql_str = f"INSERT INTO tasks (user_id, title, description, createdAt) VALUES ({task_details["user_id"]}, '{task_details["title"]}', '{task_details["description"]}', '{task_details["createdAt"]}')"
    _ = du.execute_insert_query(sql_str=sql_str)
    return True


def select_all_tasks(user_id: int) -> (list, list):
    sql_str = f"SELECT * FROM tasks WHERE active_status = 'active' AND user_id = {user_id} ORDER BY createdAt DESC, task_id"
    result_set, result_set_metadata = du.execute_select_query(sql_str=sql_str)
    return result_set, result_set_metadata

def select_latest_task(user_id: int) -> (list, list):
    sql_str = f"SELECT * FROM tasks WHERE active_status = 'active' AND user_id = {user_id} ORDER BY createdAt DESC, task_id LIMIT 1"
    result_set, result_set_metadata = du.execute_select_query(sql_str=sql_str)
    return result_set, result_set_metadata

def select_latest_updated_task(user_id: int) -> (list, list):
    sql_str = f"SELECT * FROM tasks WHERE active_status = 'active' AND user_id = {user_id} ORDER BY updatedAt DESC, task_id LIMIT 1"
    result_set, result_set_metadata = du.execute_select_query(sql_str=sql_str)
    return result_set, result_set_metadata

def select_tasks_by_status(user_id: int, status: str) -> (list, list):
    sql_str = f"SELECT * FROM tasks WHERE active_status = 'active' AND user_id = {user_id} AND status = '{status}' ORDER BY createdAt DESC, task_id"
    result_set, result_set_metadata = du.execute_select_query(sql_str=sql_str)
    return result_set, result_set_metadata

def select_task_by_task_id(task_id: int) -> (list, list):
    sql_str = f"SELECT * FROM tasks WHERE active_status = 'active' AND task_id = {task_id} LIMIT 1"
    result_set, result_set_metadata = du.execute_select_query(sql_str=sql_str)
    return result_set, result_set_metadata

def update_task(user_id: int, task_id: int, update_details: dict, update_timestamp: str) -> bool:
    update_clause_str = f"UPDATE tasks SET updatedAt = '{update_timestamp}', "
    set_clause_str = ', '.join([f"{key} = '{value}'" for key, value in update_details.items()])
    where_clause_str = f" WHERE active_status = 'active' AND user_id = {user_id} AND task_id = {task_id}"
    sql_str = update_clause_str + set_clause_str + where_clause_str

    updated_row_count = du.execute_update_query(sql_str)
    if updated_row_count:
        return True
    else:
        return False


def replace_task(user_id: int, task_id: int, title: str, description: str, status: str, update_timestamp: str):
    sql_str = f"UPDATE tasks SET user_id = {user_id}, title = '{title}', description = '{description}', status = '{status}', updatedAt = '{update_timestamp}' WHERE active_status = 'active' AND user_id = {user_id} AND task_id = {task_id}"
    updated_row_count = du.execute_update_query(sql_str=sql_str)

    if updated_row_count:
        return True
    else:
        return False


def delete_task(user_id: int, task_id: int, delete_timestamp: str) -> bool:
    sql_str = f"UPDATE tasks SET active_status = 'inactive', deactivatedAt = '{delete_timestamp}' WHERE active_status = 'active' AND user_id = {user_id} AND task_id = {task_id}"
    updated_row_count = du.execute_update_query(sql_str=sql_str)
    print(updated_row_count)
    if updated_row_count:
        return True
    else:
        return False

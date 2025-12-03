from server.db import db_utils as du

def insert_task(task_details: dict) -> list:
    sql_str = f"INSERT INTO tasks (user_id, title, description, createdAt) VALUES ({task_details["user_id"]}, '{task_details["title"]}', '{task_details["description"]}', '{task_details["createdAt"]}')"
    result_set , result_set_metadata = du.execute_query(sql_str=sql_str)
    return result_set

def select_all_tasks(user_id: int) -> list:
    sql_str = f"SELECT * FROM tasks WHERE user_id = {user_id} ORDER BY createdAt DESC, task_id"
    result_set , result_set_metadata = du.execute_query(sql_str=sql_str)
    return result_set, result_set_metadata

def select_tasks_by_status(user_id: int, status: str) -> list:
    sql_str = f"SELECT * FROM tasks WHERE user_id = {user_id} AND status = '{status}' ORDER BY createdAt DESC, task_id"
    result_set , result_set_metadata = du.execute_query(sql_str=sql_str)
    return result_set, result_set_metadata

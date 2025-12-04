from server.db import db_utils as du

def get_distinct_emails() -> list:
    sql_str = f"SELECT DISTINCT users.email FROM users"
    result_set = du.execute_select_query(sql_str = sql_str)
    distinct_emails = [row[0] for row in result_set]
    return distinct_emails

def get_distinct_username() -> list:
    sql_str = f"SELECT DISTINCT users.user_name FROM users"
    result_set = du.execute_select_query(sql_str = sql_str)
    distinct_usernames = [row[0] for row in result_set]
    return distinct_usernames

def insert_new_user(user_values: dict) -> list:
    sql_str = f"INSERT INTO users (user_name, email, password, createdAt) VALUES ('{user_values["username"]}', '{user_values["email"]}', '{user_values["password"]}', '{user_values["createdAt"]}')"
    result_set = du.execute_insert_query(sql_str = sql_str)
    return result_set

def get_user_by_login_key(login_key: str) -> list:
    sql_str = f"SELECT * FROM users WHERE users.user_name = '{login_key}' OR users.email = '{login_key}'"
    result_set = du.execute_select_query(sql_str = sql_str)
    if len(result_set) == 1:
        user_details = list(result_set[0])
        return user_details
    else:
        print("Duplicate row found")
        return []

def get_user_id_by_email(email: str) -> int:
    sql_str = f"SELECT user_id FROM users WHERE email = '{email}'"
    result_set , result_set_metadata = du.execute_select_query(sql_str=sql_str)
    if len(result_set) == 1:
        user_id = result_set[0][0]
        return user_id
    else:
        return 0


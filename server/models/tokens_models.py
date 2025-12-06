from server.db import db_utils as du

def insert_token(insert_token_details: dict) -> bool:
    sql_str = f"INSERT INTO tokens (user_id, token, createdAt) VALUES ({insert_token_details["user_id"]}, '{insert_token_details["token"]}', '{insert_token_details["createdAt"]}')"
    _ = du.execute_insert_query(sql_str=sql_str)
    return True

def get_token_by_user_id(user_id: int) -> str:
    sql_str = f"SELECT token FROM tokens WHERE user_id = {user_id} ORDER BY createdAt DESC LIMIT 1"
    result_set , _ = du.execute_select_query(sql_str=sql_str)
    if len(result_set) == 1:
        token = result_set[0][0]
        return token
    else:
        return ""
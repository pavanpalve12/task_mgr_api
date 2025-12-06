from server.utils import hashing as hashing
from server.utils import validators as validators
from server.models import users_models as um
from datetime import datetime as datetime

def signup_user(email: str, username: str, password: str) -> (bool, str):
    insert_user_values = {}
    password_hash = hashing.hash_password(password=password)

    if not password_hash:
        return False, "server_error"
    else:
        if not validators.is_valid_email(email = email):
            return False, "invalid_email"
        else:
            if not validators.is_email_unique( email = email):
                return False, "email_exists"
            else:
                if not validators.is_username_unique( username = username):
                    return False, "username_exists"
                else:
                    insert_user_values["email"] = email
                    insert_user_values["username"] = username
                    insert_user_values["password"] = password_hash
                    insert_user_values["createdAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(insert_user_values)
    if insert_user_values:
        print("Inserting values")
        um.insert_new_user(user_values = insert_user_values)

    return True, "signup_success"

def login_user(login_key: str, password: str) -> (bool, str):
    user_details = um.get_user_by_login_key(login_key=login_key)
    print(user_details)
    if not user_details:
        return False, "invalid_credentials"
    else:
        if (login_key == user_details[0] or login_key == user_details[1]) and hashing.validate_password(password=password, stored_hash_password=user_details[3]) == True:
            return True, "login_success"
        else:
            return False, "invalid_credentials"

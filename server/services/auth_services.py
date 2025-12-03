from server.utils import hashing as hashing
from server.utils import validators as validators
from server.models import users_models as um
from datetime import datetime as datetime

def signup_user(email: str, username: str, password: str) -> bool:
    insert_user_values = {}
    password_hash = hashing.hash_password(password=password)

    if not password_hash:
        print("Issue while hashing password")
        return False
    else:
        if not validators.is_valid_email(email = email):
            print(f"Email is invalid -> {email}. Please use another email.")
            return False
        else:
            if not validators.is_email_unique( email = email):
                print(f"Email address already exists -> {email}. Please use another email.")
                return False
            else:
                if not validators.is_username_unique( username = username):
                    print(f"Username is taken -> {username}. Please use another username.")
                    return False
                else:
                    insert_user_values["email"] = email
                    insert_user_values["username"] = username
                    insert_user_values["password"] = password_hash
                    insert_user_values["createdAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(insert_user_values)
    if insert_user_values:
        print("Inserting values")
        um.insert_new_user(user_values = insert_user_values)

    return True

def login_user(login_key: str, password: str):
    user_details = um.get_user_by_login_key(login_key=login_key)
    print(f"Username -> {user_details[1]}, email -> {user_details[2]}, password -> {user_details[3]}")
    print(f"login key -> {login_key}, password -> {password}")
    if not user_details:
        print(f"User not found in database -> {login_key})")
        return False
    else:
        if (login_key == user_details[0] or login_key == user_details[1]) and hashing.validate_password(password=password, stored_hash_password=user_details[3]) == True:
            return True
        else:
            print("Login key or password is not matching")
            return False

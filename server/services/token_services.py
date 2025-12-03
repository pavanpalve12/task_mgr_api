from server.models import tokens_models as tm
import os
import base64
from datetime import datetime

def generate_user_token() -> str:
    os_random = os.urandom(32)
    token = base64.urlsafe_b64encode(os_random).decode('utf-8')
    return token

def store_token(user_id: int) -> bool:
    token = generate_user_token()
    if token:
        print(f"Token is generated -> {token}")
        insert_token_details = {
            "user_id": user_id,
            "token": token,
            "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        tm.insert_token(insert_token_details=insert_token_details)
    else:
        print("Token generation failed")

    return True

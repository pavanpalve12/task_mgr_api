import hashlib
import os
import base64

def hash_password(password: str) -> str:
    # Step 1: generate a random salt
    salt = os.urandom(16)

    # Step 2: Derive a secure hash using pbkdf2_hmac
    hash_bytes = hashlib.pbkdf2_hmac(
        hash_name = "sha256",
        password = password.encode('utf-8'),
        salt = salt,
        iterations = 100
    )

    # Step 3: Encode salt : hash for storage
    salt_b64 = base64.b64encode(salt).decode('utf-8')
    hash_b64 = base64.b64encode(hash_bytes).decode('utf-8')

    return f"{salt_b64}:{hash_b64}"

def validate_password(password:str, stored_hash_password: str) -> bool:
    salt_b64, hash_b64 = stored_hash_password.split(":")

    stored_salt = base64.b64decode(salt_b64)
    stored_hash = base64.b64decode(hash_b64)

    new_hash = hashlib.pbkdf2_hmac(
        hash_name = "sha256",
        password = password.encode('utf-8'),
        salt = stored_salt,
        iterations = 100
    )

    return new_hash == stored_hash
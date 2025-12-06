from server.models import users_models as um
import re

def is_valid_email(email: str) -> bool:
    valid_email_regex = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}"
    if re.fullmatch(pattern = valid_email_regex, string = email):
        return True
    else:
        return False

def is_email_unique(email: str) -> bool:
    unique_emails = um.get_distinct_emails()
    if email not in unique_emails:
        return True
    else:
        return False


def is_username_unique(username: str) -> bool:
    unique_usernames = um.get_distinct_username()
    if username not in unique_usernames:
        return True
    else:
        return False


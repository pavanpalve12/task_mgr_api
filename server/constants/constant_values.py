from pathlib import Path as path

base_dir = path(__file__).resolve().parent.parent  # server/
db_file = base_dir / "db" / "to_do_db.sqlite"

success = {
    "http_code": "",
    "status": "success",
    "success":{
        "code": "",
        "message": ""
    },
    "data": [] # list of task dicts
}

error = {
    "http_code": "",
    "status": "error",
    "error": {
        "code": "", # short error - validation / unauthorized etc
        "message": "" # cause of error
    }
}

ERROR_MAP = {
    "missing_token": {
        "http_code": 401,
        "error_code": "missing_token",
        "error_msg": "Authentication token is required."
    },
    "invalid_token": {
        "http_code": 401,
        "error_code": "invalid_token",
        "error_msg": "The provided token is invalid."
    },
    "expired_token": {
        "http_code": 401,
        "error_code": "expired_token",
        "error_msg": "Your authentication token has expired."
    },
    "invalid_credentials": {
        "http_code": 401,
        "error_code": "invalid_credentials",
        "error_msg": "Email or password is incorrect."
    },
    "forbidden": {
        "http_code": 403,
        "error_code": "forbidden",
        "error_msg": "You do not have permission to perform this action."
    },
    "resource_not_found": {
        "http_code": 404,
        "error_code": "resource_not_found",
        "error_msg": "The requested resource was not found."
    },
    "email_exists": {
        "http_code": 409,
        "error_code": "email_exists",
        "error_msg": "This email is already registered."
    },
    "username_exists": {
        "http_code": 409,
        "error_code": "username_exists",
        "error_msg": "This username is already taken."
    },
    "bad_request": {
        "http_code": 400,
        "error_code": "bad_request",
        "error_msg": "The request cannot be processed due to invalid input."
    },
    "invalid_email": {
        "http_code": 400,
        "error_code": "invalid_email",
        "error_msg": "The provided email format is invalid."
    },
    "invalid_title": {
        "http_code": 400,
        "error_code": "invalid_title",
        "error_msg": "Title does not meet required validation rules."
    },
    "invalid_description": {
        "http_code": 400,
        "error_code": "invalid_description",
        "error_msg": "Description does not meet validation rules."
    },
    "invalid_status": {
        "http_code": 422,
        "error_code": "invalid_status",
        "error_msg": "The provided status value is not allowed."
    },
    "rate_limited": {
        "http_code": 429,
        "error_code": "rate_limited",
        "error_msg": "Too many requests. Please slow down."
    },
    "server_error": {
        "http_code": 500,
        "error_code": "server_error",
        "error_msg": "An internal server error occurred."
    },
    "service_unavailable": {
        "http_code": 503,
        "error_code": "service_unavailable",
        "error_msg": "The service is temporarily unavailable. Try again later."
    }
}

SUCCESS_MAP = {
    "signup_success": {
        "http_code": 201,
        "success_code": "signup_success",
        "success_msg": "User registered successfully."
    },
    "login_success": {
        "http_code": 200,
        "success_code": "login_success",
        "success_msg": "User authenticated successfully."
    },
    "create_todo_success": {
        "http_code": 201,
        "success_code": "create_todo_success",
        "success_msg": "Todo item created successfully."
    },
    "update_todo_success": {
        "http_code": 200,
        "success_code": "update_todo_success",
        "success_msg": "Todo item updated successfully."
    },
    "delete_todo_success": {
        "http_code": 204,
        "success_code": "delete_todo_success",
        "success_msg": "Todo item deleted."
    },
    "list_todos_success": {
        "http_code": 200,
        "success_code": "list_todos_success",
        "success_msg": "Todo items retrieved successfully."
    },
    "token_refreshed": {
        "http_code": 200,
        "success_code": "token_refreshed",
        "success_msg": "Token refreshed successfully."
    },
    "logout_success": {
        "http_code": 204,
        "success_code": "logout_success",
        "success_msg": "User logged out successfully."
    },
    "success": {
        "http_code": 200,
        "success_code": "success",
        "success_msg": "success"
    }
}



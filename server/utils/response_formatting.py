from server.constants import constant_values as cv
import copy

def format_response(code: str, data: list = None) -> dict:
    if "success" in code:
        http_code = cv.SUCCESS_MAP.get(code).get("http_code")
    else:
        http_code = cv.ERROR_MAP.get(code).get("http_code")

    if 200 <= http_code < 300:
        response = copy.deepcopy(cv.success)
        response["http_code"] = http_code
        response["data"] = data
        response["success"]["code"] = cv.SUCCESS_MAP.get(code).get("success_code")
        response["success"]["message"] = cv.SUCCESS_MAP.get(code).get("success_msg")
        return response
    elif 400 <= http_code < 600:
        response = copy.deepcopy(cv.error)
        response["http_code"] = http_code
        response["error"]["code"] = cv.ERROR_MAP.get(code).get("error_code")
        response["error"]["message"] = cv.ERROR_MAP.get(code).get("error_msg")
        return response
    else:
        return {
            "http_code": http_code,
            "status": "error",
            "error": {
                "code": "unknown",
                "message": "unrecognized status code"
            }
        }
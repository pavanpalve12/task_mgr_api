from client.utils import parser as parser
import os

def main():
    while True:
        parser.show_signup_login_menu()
        user_input = parser.take_signup_login_input()

        if user_input["action"] == "signup":
            api_request_str = "POST/register/"
            print("You want to signup -> ", str(user_input))
        if user_input["action"] == "login":
            print("You want to login -> ", str(user_input))

        login_flag = True
        while True:
            if login_flag:
                task_input = {}
                parser.show_task_menu()
                task_input = parser.take_task_action_input()
                if task_input["action"] == "add_task":
                    print("You want to add tasks", task_input)
                if task_input["action"] == "replace_task":
                    print("You want to replace tasks", task_input)
                if task_input["action"] == "delete_task":
                    print("You want to delete tasks", task_input)
                if task_input["action"] == "list_task":
                    print("You want to list tasks", task_input)
                if task_input["action"] == "update_task_status":
                    print("You want to update tasks status", task_input)

                print(user_input)
                print(task_input)
            else:
                continue
if __name__ == "__main__":
        main()

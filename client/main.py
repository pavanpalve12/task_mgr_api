from client.utils import parser as parser

def main():
    # Take Sign up / login input
    user_input = parser.take_signup_login_input()

    # Take task action input, add, update, delete, list
    if user_input["action"] == "login":
        task_input = parser.take_task_action_input()

        print("Login Info -> ", str(user_input))
        print("Task Info -> ", str(task_input))


if __name__ == "__main__":
        main()

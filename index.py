import main

session = ""  # 此处填写自己的laravel_session


def main_handler(event, context):
    main.run(session)

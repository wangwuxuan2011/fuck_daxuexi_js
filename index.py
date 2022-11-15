import main

session = "123123"  # 此处填写自己的laravel_session


def main_handler(event, context):
    main.run(session)

import main

session = ""  # 此处填写自己的laravel_session
bark_id = ""  # 此处填写自己的bark_id

def main_handler(event, context):
    main.run(session, bark_id)


main.run(session, bark_id)
import get_latest_lessonId
import report_learning
import web_header


def run(session=""):
    if session == "":
        raise Exception("需要session，请填充")

    web_header.set_cookie({"laravel_session": session})

    get_info = get_latest_lessonId.get_info()
    lesson_id = get_info.get("lesson_id")
    token = get_info.get("token")

    print(lesson_id, token)

    report = report_learning.report(token, lesson_id)
    print(report)
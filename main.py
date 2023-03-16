import get_latest_lessonId
import report_learning
import web_header
import push_bark


def run(session="", bark_id=""):
    try:
        if session == "":
            raise Exception("需要session，请填充")
        web_header.set_cookie({"laravel_session": session})
        get_info = get_latest_lessonId.get_info()
        lesson_id = get_info.get("lesson_id")
        report_status = report_learning.report(lesson_id)
        if report_status['status']== 1:
            push_bark.bark("第"+str(lesson_id)+"期已学习成功",bark_id)
    except Exception as e:
        print("error:" + str(e))
        push_bark.bark("错误:" + str(e),bark_id)


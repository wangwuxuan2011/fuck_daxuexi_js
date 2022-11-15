import requests

import web_header


def report(token, lesson_id):
    body = {"_token": token, "lesson_id": lesson_id}
    r = requests.post(url=web_header.get_url(), headers=web_header.get_header('post'), cookies=web_header.cookie, data=body)

    http_status_code = r.status_code  # 获取网页状态代码
    body_status_code = r.json().get("status")  # 获取返回的status
    if int(http_status_code) != 200 or int(body_status_code) != 1:
        print(r.status_code)
        print(r.text)
        print(r.json())
        raise Exception("\nhttp_status_code:" + str(http_status_code) + "\nbody_status_code:" + str(body_status_code))
    return {"http_status_code": http_status_code, "status": body_status_code}

import re

import requests

import web_header


def get_info():
    r = requests.get(url=web_header.get_url(), headers=web_header.get_header('get'), cookies=web_header.cookie)
    http_status_code = r.status_code  # 获取网页状态代码
    text = r.text
    lesson_id_array = re.findall(r"'lesson_id':(.+)\n", text, re.M | re.I)
    token_array = re.findall(r'var token = "(.+?)";', text, re.M | re.I)
    if int(http_status_code) != 200 or len(lesson_id_array) == 0 or len(token_array) == 0:
        print(http_status_code)
        print(text)
        raise Exception("\nhttp_status_code:" + str(http_status_code) + "\ntext:" + str(text))
    lesson_id = lesson_id_array[0]
    token = token_array[0]
    return {"lesson_id": lesson_id, "token": token}

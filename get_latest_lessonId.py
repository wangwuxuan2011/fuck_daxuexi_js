import re

import requests

import web_header


def get_info():
    body = {"page": 1, "limit": 5}
    r = requests.post(url=web_header.get_lessons_url(), headers=web_header.get_header(), cookies=web_header.cookie,
                     json=body)
    http_status_code = r.status_code
    if int(http_status_code) != 200:
        raise Exception("\nhttp_status_code:" + str(http_status_code) + "\n")
    json = r.json()
    lesson_id = json.get("data")[0].get("id")
    if int(http_status_code) != 200 or not lesson_id:
        raise Exception("text:" + str(json))
    return {"lesson_id": lesson_id}

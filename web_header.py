base_url = "https://service.jiangsugqt.org"
header = {
    "Host": "service.jiangsugqt.org",
    "Accept": "*/*",
    "withCredential": "true",
    "Accept-Language": "zh-CN,zh-Hans;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json",
    "Origin": "https://service.jiangsugqt.org",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.33(0x18002126) NetType/WIFI Language/zh_CN",
    "Connection": "keep-alive",
    "Referer": "https://service.jiangsugqt.org/youth-h5/",
}

cookie = {}


def get_lessons_url(confirm_url="/api/lessons"):
    return base_url + confirm_url

def get_do_url(confirm_url="/api/doLesson"):
    return base_url + confirm_url


def set_cookie(cookie_value):
    global cookie
    cookie = cookie_value

def get_header():
    return header

base_url = "https://service.jiangsugqt.org"
header_post = {"Host": "service.jiangsugqt.org",
               "Accept": "application/json, text/javascript, */*; q=0.01",
               "X-Requested-With": "XMLHttpRequest",
               "Accept-Language": "zh-CN,zh-Hans;q=0.9",
               "Accept-Encoding": "gzip, deflate, br",
               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
               "Origin": "https://service.jiangsugqt.org",
               "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, "
                             "like Gecko) MicroMessenger/6.8.0(0x16080000) MacWechat/3.6(0x13060010) Safari/605.1.15 "
                             "NetType/WIFI",
               "Connection": "keep-alive",
               "Referer": "https://service.jiangsugqt.org/youth/lesson/confirm",
               "Content-Length": "61"
               }
header_get = {"Host": "service.jiangsugqt.org",
              "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
              "Accept-Language": "zh-CN,zh-Hans;q=0.9",
              "Accept-Encoding": "gzip, deflate, br",
              "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                            "MicroMessenger/6.8.0(0x16080000) MacWechat/3.6(0x13060010) Safari/605.1.15 NetType/WIFI",
              "Connection": "keep-alive",
              }
cookie = {}


def get_url(confirm_url="/youth/lesson/confirm"):
    return base_url + confirm_url


def set_cookie(cookie_value):
    global cookie
    cookie = cookie_value


def get_header(method):
    if method == 'get':
        return header_get
    elif method == 'post':
        return header_post

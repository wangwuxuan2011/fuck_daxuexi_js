import requests


def bark(content,bark_id):
    if bark_id != "":
        r = requests.get(url="https://api.day.app/" + bark_id + "/江苏省青年大学习/" + content)


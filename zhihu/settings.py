# encoding: utf-8
import os.path
import random

# UserAgent list
user_agent_list = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
]

USER_AGENT = random.choice(user_agent_list)

HEADERS = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent': USER_AGENT
}

ZHUANLAN_HEADERS = {
    "Host": "zhuanlan.zhihu.com",
    "Referer": "https://zhuanlan.zhihu.com/",
    'User-Agent': USER_AGENT
}

COOKIES_FILE = os.path.join(os.path.expanduser('~'), "cookies.txt")

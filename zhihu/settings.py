# encoding: utf-8
import os.path

# UserAgent list
user_agent_list = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
]

USER_AGENT = user_agent_list[0]

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

# COOKIE 存储位置
COOKIES_FILE = os.path.join(os.path.expanduser('~'), "cookies.txt")

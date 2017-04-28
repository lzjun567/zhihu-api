# encoding: utf-8
import os.path

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87'

HEADERS = {"Host": "www.zhihu.com",
           "Referer": "https://www.zhihu.com/",
           'User-Agent': USER_AGENT
           }

ZHUANLAN_HEADERS = {"Host": "zhuanlan.zhihu.com",
                    "Referer": "https://zhuanlan.zhihu.com/",
                    'User-Agent': USER_AGENT
                    }

COOKIES_FILE = os.path.join(os.path.expanduser('~'), "cookies.txt")

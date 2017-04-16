# encoding: utf-8
__author__ = 'liuzhijun'
import time
from zhihu import Zhihu

if __name__ == '__main__':
    zhihu = Zhihu()
    profile = zhihu.user(profile_url="https://www.zhihu.com/people/xiaoxiaodouzi")
    time.sleep(1)
    profile = zhihu.user(user_slug="xiaoxiaodouzi")
    time.sleep(1)
    _id = profile.get("id")
    zhihu.send_message("你好,问候1", profile_url="https://www.zhihu.com/people/xiaoxiaodouzi")
    time.sleep(1)
    zhihu.send_message("你好,问候2", user_slug="xiaoxiaodouzi")
    time.sleep(1)
    zhihu.send_message("你好,问候3", user_id=_id)


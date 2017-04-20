# encoding: utf-8

import time

from zhihu import Zhihu

__author__ = 'liuzhijun'

if __name__ == '__main__':
    zhihu = Zhihu()
    profile = zhihu.user(profile_url="https://www.zhihu.com/people/zhijun-liu")
    print(profile)
    time.sleep(1)
    # profile = zhihu.user(user_slug="xiaoxiaodouzi")
    # time.sleep(1)
    #
    # _id = profile.get("id")
    # print(_id)
    # # 3a2be5588fefcbc13ba4459cd8f1b5bc
    # # 1da75b85900e00adb072e91c56fd9149
    # zhihu.send_message("你好,问候1", profile_url="https://www.zhihu.com/people/xiaoxiaodouzi")
    # time.sleep(1)
    # zhihu.send_message("你好,问候2", user_slug="xiaoxiaodouzi")
    # time.sleep(1)
    # zhihu.send_message("你好,问候3", user_id=_id)

    # zhihu.follow(profile_url="https://www.zhihu.com/people/gao-yu-dong-41")

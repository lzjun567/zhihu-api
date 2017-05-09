# encoding: utf-8

import os

from zhihu.models import account
from zhihu.settings import COOKIES_FILE

try:
    input = raw_input  # py2
except:
    pass


def need_login(func):
    """
    用户认证装饰器(判断用户是否已经登录)
    """

    def wrapper(self, *args, **kwargs):
        success = True
        # TODO 1. 不能这样简单粗暴判断cookie文件存不存在,因为有可能文件里面的cookie信息已经过期,也有可能只是一个空文件
        if not os.path.exists(COOKIES_FILE):
            success = False
            while not success:
                email = input("请输入email或者手机号码:")
                password = input("请输入密码:")
                success = account.Account().login(email, password)
        if success:
            result = func(self, *args, **kwargs)
            return result

    return wrapper

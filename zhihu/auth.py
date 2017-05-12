# encoding: utf-8

import os
import requests

from zhihu.models import account
import requests.utils

try:
    input = raw_input  # py2
except:
    pass


def login():
    success = False
    while not success:
        email = input("请输入email或者手机号码:")
        password = input("请输入密码:")
        success = account.Account().login(email, password)
    # session.cookies.save(ignore_discard=True)


def need_login(func):
    """
    用户认证装饰器(判断用户是否已经登录)
    """

    def wrapper(self, *args, **kwargs):
        if 'z_c0' not in requests.utils.dict_from_cookiejar(self._session.cookies):
            # 先尝试加载本地cookies
            try:
                self._session.cookies.load(ignore_discard=True)
            except:
                pass
            # 如果加载cookies后依然无登录信息，则重新登录
            if 'z_c0' not in requests.utils.dict_from_cookiejar(self._session.cookies):
                login()
        return func(self, *args, **kwargs)

    return wrapper

# encoding: utf-8

"""
用户认证装饰器(判断用户是否已经登录)
"""

import requests
import requests.utils

from ..models.account import Account


def authenticated(func):
    def wrapper(self, *args, **kwargs):
        success = False
        # 先判断有没有cookie文件, 崽判断cookie是否有效
        if 'z_c0' in requests.utils.dict_from_cookiejar(self.cookies):
            from ..url import URL
            r = self._execute(method="get", url=URL.profile(user_slug="zhijun-liu"))
            success = r.ok
        while not success:
            account = input("请输入Email或者手机号码:")
            password = input("请输入密码:")
            obj = Account()
            data = obj.login(account, password)
            if data.get("r") == 0:
                success = True
                self.cookies = obj.cookies
            else:
                print(data.get("msg"))
        else:
            return func(self, *args, **kwargs)

    return wrapper

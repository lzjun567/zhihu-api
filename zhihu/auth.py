# encoding: utf-8

import requests
import requests.utils

from zhihu.models.account import Account


# from .models.zhihux import ZhihuX



def need_login(func):
    """
    用户认证装饰器(判断用户是否已经登录)
    """

    def wrapper(self, *args, **kwargs):
        print('xxx')
        success = False
        # 先判断有没有cookie文件, 在判断cookie有没有效
        if 'z_c0' in requests.utils.dict_from_cookiejar(self.cookies):
            from .url import URL
            r = self.get(URL.profile(user_slug="zhijun-liu"))
            success = r.ok
        while not success:
            account = input("请输入Email或者手机号码:")
            password = input("请输入密码:")
            data = Account().login(account, password)
            print(data)
            if data.get("r") == 0:
                success = True
            else:
                print(data.get("msg"))
        else:
            return func(self, *args, **kwargs)

    return wrapper

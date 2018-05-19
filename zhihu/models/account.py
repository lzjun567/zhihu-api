# encoding: utf-8

import logging
import re
import time
from bs4 import BeautifulSoup

from zhihu import settings
from zhihu.models.base import Model
from zhihu.error import ZhihuError
from zhihu.models import RequestDataType
from zhihu.url import URL


class Account(Model):
    def login(self, account, password):
        """
        账户登录
        :param account: email或者手机号码
        :param password:
        :return:
        """
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        phone_regex = r"\+?\d{10,15}$"
        email_pattern = re.compile(email_regex)
        phone_pattern = re.compile(phone_regex)

        if email_pattern.match(account) or phone_pattern.match(account):
            return self._login_api(account, password)
        else:
            raise ZhihuError("无效的用户名")

    def _login_api(self, account, password):
        time_stamp = str(int((time.time() * 1000)))
        _xsrf, _dc0 = self._get_xsrf_dc0()
        self.headers.update({
            "authorization": "oauth c3cef7c66a1843f8b3a9e6a1e3160e20",  # 固定值
            "X-Xsrftoken": _xsrf,
        })
        captcha = self._get_captcha()
        data = {
            "client_id": "c3cef7c66a1843f8b3a9e6a1e3160e20",
            "grant_type": "password",
            "timestamp": time_stamp,
            "source": "com.zhihu.web",
            "password": password,
            "username": account,
            "captcha": "",
            "lang": "en",
            "ref_source": "homepage",
            "utm_source": "",
            "signature": self._get_signature(time_stamp),
            'captcha': captcha
        }
        return self._login_execute(url=URL.api_login(), data=data)

    def _login_execute(self, url=None, data=None):
        r = self._execute(method="post", url=url, data=data, headers=self.headers, cookies=self.cookies)
        result = r.json()
        if r.status_code == 201:
            self.cookies.save(ignore_discard=True)  # 保存登录信息cookies
            self.cookies.load(filename=settings.COOKIES_FILE, ignore_discard=True)
        return result

    def _register_validate(self, data):
        """
        注册前的验证,是否已经注册
        :return:
        """
        r = super(Account, self)._execute(method="post",
                                          url=URL.register_validate(),
                                          data=data,
                                          data_type=RequestDataType.FORM_DATA)
        if r.ok and r.json().get("r") == 0:
            return True
        else:
            if r.ok and r.json().get("r") == 1:
                self.log(r.text)
            return False

    def register(self, name=None, phone_num=None, password=None):
        data = {
            "fullname": name,
            "phone_num": phone_num,
            "password": password,
            "_xsrf": super(Account, self)._get_xsrf_dc0(),
            "captcha": super(Account, self)._get_captcha(_type="register"),
            "captcha_source": "register",
        }
        valid = self._register_validate(data)
        if valid:
            self.log("账号验证成功,发送短信验证码")
            params = {"phone_num": phone_num, "captcha_source": "register"}
            # 发送验证码
            r = self._execute(method="get", url=URL.register_sms_code(), params=params)
            self.log(r.json().get("msg"))
            code = input("输入短信验证码:")
            data['verification_code'] = code
            data.pop("captcha")
            r = self._execute(method="post", url=URL.register(), data=data, data_type=RequestDataType.FORM_DATA)
            if r.ok and r.json().get("r") == 0:
                self.log("注册成功")
                return r.json()
            else:
                if r.ok and r.json().get("r") != 0:
                    self.log(r.json().get("msg"), level=logging.ERROR)
                if not r.ok:
                    self.log("请求失败", level=logging.ERROR)
                return r.json()
        else:
            raise ZhihuError("验证失败,请查看日志")

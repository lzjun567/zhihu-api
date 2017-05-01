# encoding: utf-8

from zhihu.models import Model
from zhihu.url import URL
from zhihu.models import RequestDataType
import re
import logging


class Account(Model):
    def login(self, account, password, **kwargs):
        """
        账户登录
        :param account: email或者手机号码
        :param password:
        :param kwargs:
        :return:
        """
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        pattern = re.compile(email_regex)
        if pattern.match(account):
            return self._login_with_email(account, password, **kwargs)
        else:
            return self._login_with_phone(account, password, **kwargs)

    def _login_with_phone(self, phone, password, **kwargs):
        data = {
            '_xsrf': self._get_xsrf(),
            'password': password,
            'phone_num': phone,
            "captcha": self._get_captcha(),
            "remeber_me": "true",
        }
        return self._execute(url=URL.phone_login(), data=data, **kwargs)

    def _login_with_email(self, email, password, **kwargs):
        data = {'email': email,
                'password': password,
                '_xsrf': self._get_xsrf(**kwargs),
                "captcha": self._get_captcha(**kwargs),
                'remember_me': 'true'}
        return self._execute(url=URL.email_login(), data=data, **kwargs)

    def _execute(self, method="post", url=None, data=None, data_type=RequestDataType.JSON_DATA, **kwargs):

        r = super(Account, self)._execute(method="post", url=url, data=data, data_type=RequestDataType.FORM_DATA,
                                          **kwargs)

        if r.ok:
            result = r.json()
            if result.get("r") == 0:
                self.log(result.get("msg"))
                return True
            else:

                self.log(result.get("msg"), level=logging.ERROR)
                return False

        else:
            self.log("登录失败", level=logging.ERROR)
            self.log(r.text)
            return False

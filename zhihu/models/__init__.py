# encoding: utf-8

import logging
import os
import platform
import re
import subprocess

try:
    from http import cookiejar  # py3
except:
    import cookielib as cookiejar  # py2

try:
    input = raw_input  # py2
except:
    pass

import requests
import requests.packages.urllib3 as urllib3
from bs4 import BeautifulSoup
from ..error import ZhihuError
from ..url import URL
from .. import settings

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class RequestDataType(object):
    """
    发送请求时,传给知乎服务器的数据类型
    有两种请求,1. 表单类型,2 json格式的字符串
    """
    FORM_DATA, JSON_DATA = range(2)


class Model(object):
    def __init__(self, **kwargs):
        self._session = requests.Session()
        self._session.verify = False
        self._session.headers = settings.HEADERS
        self._session.cookies = cookiejar.LWPCookieJar(filename=settings.COOKIES_FILE)
        for k, v in kwargs.items():
            setattr(self._session, k, v)
        try:
            self._session.cookies.load(ignore_discard=True)
        except:
            pass

    @property
    def logger(self):
        logger = logging.getLogger(self.__class__.__name__)
        return logging.LoggerAdapter(logger, {'zhihu': self})

    def log(self, message, level=logging.INFO, **kw):
        self.logger.log(level, message, **kw)

    def _get_captcha(self, _type="login", **kwargs):
        r = self._session.get(URL.captcha(_type=_type), **kwargs)
        with open('captcha.jpg', 'wb') as f:
            f.write(r.content)

        if platform.system() == 'Darwin':
            subprocess.call(['open', 'captcha.jpg'])
        elif platform.system() == 'Linux':
            subprocess.call(['xdg-open', 'captcha.jpg'])
        else:
            os.startfile('captcha.jpg')
        captcha = input("输入验证码：")
        return captcha

    def _get_xsrf(self, url=None, **kwargs):
        """
        获取某个页面下的xsrf
        :param url:
        :param kwargs:
        :return:
        """
        response = self._session.get(url or URL.index(), **kwargs)
        soup = BeautifulSoup(response.content, "html.parser")
        xsrf = soup.find('input', attrs={"name": "_xsrf"}).get("value")
        return xsrf

    def _user_id(self, user_slug):
        """
        user_slug 转 user_id
        :param user_slug:
        :return:
        """
        profile = self.user(user_slug=user_slug)
        user_id = profile.get("id")
        return user_id

    def _user_slug(self, profile_url):
        """
        profile_url 转 user_slug
        :param profile_url:
        :return:
        """
        pattern = re.compile("https?://www.zhihu.com/people/([\w-]+)")
        match = pattern.search(profile_url)
        if match:
            user_slug = match.group(1)
            return user_slug
        else:
            raise ZhihuError("invalid profile url")

    def _execute(self, method="post", url=None, params=None, data=None, data_type=RequestDataType.JSON_DATA, **kwargs):
        """
        通用请求方法
        :param method: 请求方法
        :param url:     请求URL
        :param params:  请求参数
        :param data:    请求数据
        :param data_type:    提交的数据格式(可能是表单类型,也可能是json格式的字符串)
        :param kwargs:  requests支持的参数，比如可以设置代理参数
        :return: response
        """
        if data_type == RequestDataType.JSON_DATA:
            r = getattr(self._session, method)(url, json=data, params=params, **kwargs)
        else:
            r = getattr(self._session, method)(url, data=data, params=params, **kwargs)
        return r

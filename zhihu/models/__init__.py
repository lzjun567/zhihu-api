# encoding: utf-8

import os
import platform
import re
import subprocess
from enum import Enum

import requests
import requests.packages.urllib3 as urllib3
from bs4 import BeautifulSoup

from zhihu import settings
from zhihu.error import ZhihuError
from zhihu.url import URL

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class RequestDataType(Enum):
    """
    发送请求时,传给知乎服务器的数据类型
    有两种请求,1. 表单类型,2 json格式的字符串
    """
    FORM = 1
    JSON = 2


class Zhihu(requests.Session):
    def __init__(self):
        # self.cookies = cookiejar.LWPCookieJar(filename=settings.COOKIES_FILE)
        # self.cookies.load(filename=settings.COOKIES_FILE, ignore_discard=True)
        self.verify = False
        self.headers = settings.HEADERS
        super(Zhihu, self).__init__()

    def _get_captcha(self, _type="login"):
        r = self.get(URL.captcha(_type=_type))
        with open('captcha.jpg', 'wb') as f:
            f.write(r.content)

        # 调用系统图片预览工具
        if platform.system() == 'Darwin':
            subprocess.call(['open', 'captcha.jpg'])
        elif platform.system() == 'Linux':
            subprocess.call(['xdg-open', 'captcha.jpg'])
        else:
            os.startfile('captcha.jpg')
        captcha = input("输入验证码：")
        return captcha

    def _get_xsrf(self, url=None):
        """
        获取某个URL页面下的xsrf
        :param url:
        :return: xsrf
        """
        response = self.get(url or URL.index())
        print(response)
        soup = BeautifulSoup(response.content, "lxml")
        print(soup)
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

    def _execute(self, method="post", url=None, params=None, data=None, data_type=RequestDataType.JSON):
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
        if data_type == RequestDataType.JSON:
            r = getattr(self, method)(url, json=data, params=params)
        else:
            r = getattr(self, method)(url, data=data, params=params)
        return r

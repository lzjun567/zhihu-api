# encoding: utf-8

"""

获取知乎数据对象的抽象既基类，任何对象都可以继承该类

比如 Answer, Question, Account

"""

import os
import execjs  # 加密
from urllib.parse import urlencode

import platform
import re
from http import cookiejar
import subprocess
import hmac
from hashlib import sha1
import json
import base64

import requests
import requests.packages.urllib3 as urllib3

from zhihu import settings
from zhihu.error import ZhihuError
from zhihu.url import URL

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Model(requests.Session):
    def __init__(self):
        super(Model, self).__init__()
        self.cookies = cookiejar.LWPCookieJar(filename=settings.COOKIES_FILE)
        try:
            self.cookies.load(ignore_discard=True)
        except FileNotFoundError:
            pass
        self.verify = False
        self.headers = settings.HEADERS

    def _get_captcha(self, _type="login"):
        response = self.get(URL.api_captcha())
        r = re.findall('"show_captcha":(\w+)', response.text)
        if r[0] == 'false':
            return ''
        else:
            response = self.put(
                'https://www.zhihu.com/api/v3/oauth/captcha?lang=en', headers=self.headers)
            show_captcha = json.loads(response.text)['img_base64']
            with open('captcha.jpg', 'wb') as f:
                f.write(base64.b64decode(show_captcha))
            # 调用系统图片预览工具
            if platform.system() == 'Darwin':
                subprocess.call(['open', 'captcha.jpg'])
            elif platform.system() == 'Linux':
                subprocess.call(['xdg-open', 'captcha.jpg'])
            else:
                os.startfile('captcha.jpg')
            captcha = input("输入验证码：")
            data = {"input_text": captcha}

            response = self.post('https://www.zhihu.com/api/v3/oauth/captcha?lang=en',
                                 headers=self.headers, data=data)
            return captcha

    @staticmethod
    def _get_signature(time_stamp):
        # 生成signature,利用hmac加密
        # 根据分析之后的js，可发现里面有一段是进行hmac加密的
        # 分析执行加密的js 代码，可得出加密的字段，利用python 进行hmac解码
        h = hmac.new(key='d1b964811afb40118a12068ff74a12f4'.encode(
            'utf-8'), digestmod=sha1)
        grant_type = 'password'
        client_id = 'c3cef7c66a1843f8b3a9e6a1e3160e20'
        source = 'com.zhihu.web'
        now = time_stamp
        h.update((grant_type + client_id + source + now).encode('utf-8'))
        return h.hexdigest()

    def _get_xsrf_dc0(self, url=None):
        """
        获取某个URL页面下的xsrf
        :param url:
        :return: xsrf
        """
        response = self.get(url or URL.index(), headers=self.headers)
        xsrf = response.cookies["_xsrf"]
        # dc0 = response.cookies["d_c0"]
        # return xsrf, dc0
        return xsrf, None

    def _user_id(self, user_slug=None, user_url=None):
        """
        user_slug 转 user_id
        :param user_slug:
        :param user_url:
        :return:
        """
        if not user_slug:
            user_slug = self._user_slug(user_url=user_url)
        profile = self.profile(user_slug=user_slug)
        user_id = profile.get("id")
        return user_id

    def _user_slug(self, user_url):
        pattern = re.compile("https?://www.zhihu.com/people/([\w-]+)")
        match = pattern.search(user_url)
        if match:
            user_slug = match.group(1)
            return user_slug
        else:
            raise ZhihuError("invalid url")

    def _execute(self, method="post", url=None, params=None, json=None, data=None, **kwargs):
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
        r = getattr(self, method)(url, json=json,
                                  data=data, params=params, **kwargs)
        return r

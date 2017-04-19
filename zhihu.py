# encoding: utf-8
# !/usr/bin/env python

"""
知乎API
"""
import logging
import os
import re
import time
from http import cookiejar

import requests
from bs4 import BeautifulSoup
from url import URL

logging.basicConfig(level=logging.INFO)

# cookies 文件保存在当前用户目录,
# 下次程序重新启动时,直接加载cookie文件,无需再输入用户名和密码登录
cookie_filename = os.path.join(os.path.expanduser('~'), "cookies.txt")


class ZhihuError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


def need_login(func):
    """
    用户认证(判断用户是否已经登录的装饰器)
    """

    def wrapper(self, *args, **kwargs):
        success = True
        if not os.path.exists(cookie_filename):
            success = False
            while not success:
                email = input("请输入email:")
                password = input("请输入密码:")
                success = self.login(email, password)
        if success:
            result = func(self, *args, **kwargs)
            return result

    return wrapper


class Zhihu(object):
    logger = logging.getLogger(__name__)

    def __init__(self):
        self._session = requests.session()
        self._session.verify = False
        self._session.headers = {"Host": "www.zhihu.com",
                                 "Referer": "https://www.zhihu.com/",
                                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36'
                                               ' (KHTML, like Gecko) Chrome/56.0.2924.87',
                                 }
        self._session.cookies = cookiejar.LWPCookieJar(filename=cookie_filename)
        try:
            self._session.cookies.load(ignore_discard=True)
        except:
            pass

    def _get_captcha(self):
        t = str(int(time.time() * 1000))
        r = self._session.get(URL.captcha(t))
        with open('captcha.jpg', 'wb') as f:
            f.write(r.content)
        captcha = input("验证码：")
        return captcha

    def _get_xsrf(self):
        response = self._session.get(URL.index())
        soup = BeautifulSoup(response.content, "html.parser")
        xsrf = soup.find('input', attrs={"name": "_xsrf"}).get("value")
        return xsrf

    def _user_id(self, user_slug):
        profile = self.user(user_slug=user_slug)
        user_id = profile.get("id")
        return user_id

    def _user_slug(self, profile_url):
        pattern = re.compile("https?://www.zhihu.com/people/([\w-]+)")
        match = pattern.search(profile_url)
        if match:
            user_slug = match.group(1)
            return user_slug
        else:
            raise ZhihuError("invalid profile url")

    def login(self, email, password):
        """
        登录需要的验证码会保存在当前目录,需要用户自己识别,并输入
        """
        request_body = {'email': email,
                        'password': password,
                        '_xsrf': self._get_xsrf(),
                        "captcha": self._get_captcha(),
                        'remember_me': 'true'}

        response = self._session.post(URL.login(), data=request_body)
        if response.ok:
            data = response.json()
            if data.get("r") == 0:
                # 登录成功'
                self._session.cookies.save()
                self.logger.info("登录成功")
                return True
            else:
                self.logger.info("登录失败, %s" % data.get("msg"))

        else:
            self.logger.error(response.content)
        return False

    @need_login
    def send_message(self, content, user_id=None, profile_url=None, user_slug=None):
        """
        给指定的用户发私信
        :param content 私信内容
        :param user_id 用户id
        :param profile_url :用户主页地址
        :param user_slug : 用户的个性域名

        >>> send_message(profile_url = "https://www.zhihu.com/people/xiaoxiaodouzi")
        >>> send_message(user_slug = "xiaoxiaodouzi")
        >>> send_message(user_id = "1da75b85900e00adb072e91c56fd9149")
        """

        if not any([user_id, profile_url, user_slug]):
            raise ZhihuError("至少指定一个关键字参数")

        if user_id is None:
            user_slug = self._user_slug(profile_url) if user_slug is None else user_slug
            user_id = self._user_id(user_slug)

        data = {"type": "common", "content": content, "receiver_hash": user_id}
        response = self._session.post(URL.message(), json=data)
        data = response.json()
        if data.get("error"):
            self.logger.info("私信发送失败, %s" % data.get("error").get("message"))
        else:
            self.logger.info("发送成功")
        return data

    @need_login
    def user(self, user_slug=None, profile_url=None):
        """
        获取用户信息
        :param user_slug : 用户的个性域名
        :param profile_url: 用户主页地址

        :return:dict

        >>> user(profile_url = "https://www.zhihu.com/people/xiaoxiaodouzi")
        >>> user(user_slug = "xiaoxiaodouzi")

        """

        if not any([profile_url, user_slug]):
            raise ZhihuError("至少指定一个关键字参数")

        user_slug = self._user_slug(profile_url) if user_slug is None else user_slug
        response = self._session.get(URL.profile(user_slug))
        if response.ok:
            return response.json()
        else:
            self.logger.error(u"获取用户信息失败, status code: %s" % response.status_code)

    @need_login
    def follow(self, user_slug=None, profile_url=None):
        """
        关注指定用户
        :param user_slug: 用户的个性域名
        :param profile_url: 用户主页地址
        """
        if not any([profile_url, user_slug]):
            raise ZhihuError(u"至少指定一个关键字参数")
        user_slug = self._user_slug(profile_url) if user_slug is None else user_slug
        response = self._session.post(URL.follow(user_slug))
        if response.ok:
            self.logger.info(u"关注成功")
            return response.json()
        else:
            self.logger.error(u"关注用户失败, status code: %s" % response.status_code)

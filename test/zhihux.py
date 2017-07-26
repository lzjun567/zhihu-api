# encoding: utf-8


import unittest

from zhihu.models.zhihu import Zhihu

__author__ = 'liuzhijun'


class ZhihuXTestCase(unittest.TestCase):
    def test_user_profile(self):
        """
        获取用户信息
        :return:
        """

        profile = Zhihu().profile(user_url="https://www.zhihu.com/people/zhijun-liu")
        self.assertIn("avatar_url_template", profile)

    def test_send_message(self):
        """
        不带关键字参数，抛出异常
        :return:
        """
        r = Zhihu().send_message("nihhao", user_slug="zhijun-liu")
        self.assertTrue(r.ok)

    def test_follow(self):
        data = Zhihu().follow(user_slug="zhijun-liu")
        self.assertTrue(data.get("followed"))

    def test_unfollow(self):
        data = Zhihu().unfollow(user_slug="zhijun-liu")
        self.assertFalse(data.get("followed"))

    def test_followers(self):
        data = Zhihu().followers(user_slug="zhijun-liu")
        self.assertIn('paging', data)

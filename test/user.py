# encoding: utf-8


import unittest

from zhihu.models.user import User

__author__ = 'liuzhijun'


class UserTestCase(unittest.TestCase):
    def test_user_profile(self):
        """
        获取用户信息
        :return:
        """

        profile = User().profile(user_url="https://www.zhihu.com/people/zhijun-liu")
        self.assertIn("avatar_url_template", profile)

    def test_send_message(self):
        """
        不带关键字参数，抛出异常
        :return:
        """
        r = User().send_message("nihhao", user_slug="zhijun-liu")
        self.assertTrue(r.ok)

    def test_follow(self):
        data = User().follow(user_slug="zhijun-liu")
        self.assertTrue(data.get("followed"))

    def test_unfollow(self):
        data = User().unfollow(user_slug="zhijun-liu")
        self.assertFalse(data.get("followed"))

    def test_followers(self):
        data = User().followers(user_slug="zhijun-liu")
        self.assertIn('paging', data)

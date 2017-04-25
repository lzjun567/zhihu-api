# encoding: utf-8
import unittest

from zhihu import Zhihu
from zhihu.error import ZhihuError
import time


class CommonTestCase(unittest.TestCase):
    def test_send_message_with_no_kwargs(self):
        """
        不带关键字参数，抛出异常
        :return:
        """
        zhihu = Zhihu()
        self.assertRaises(ZhihuError, zhihu.send_message, "hello")

    def test_follow_with_no_kwargs(self):
        """
        不带关键字参数，抛出异常
        :return:
        """
        time.sleep(1)
        zhihu = Zhihu()
        self.assertRaises(ZhihuError, zhihu.follow)

    def test_follow_with_url(self):
        """
        带url，返回follower数量
        :return:
        """
        time.sleep(1)
        zhihu = Zhihu()
        response = zhihu.follow(profile_url="https://www.zhihu.com/people/gao-yu-dong-41")
        self.assertIn(response, 'follower_count')

    def test_follow_with_user_slug(self):
        """
        带user_slug，返回follower数量
        :return:
        """
        time.sleep(1)
        zhihu = Zhihu()
        response = zhihu.follow(user_slug="xiaoxiaodouzi")
        self.assertIn(response, 'follower_count')

    def test_follow_with_no_kwargs(self):
        """
        不带关键字参数，抛出异常
        :return:
        """
        time.sleep(1)
        zhihu = Zhihu()
        self.assertRaises(ZhihuError, zhihu.unfollow)

    def test_unfollow_with_url(self):
        """
        带url，返回follower数量
        :return:
        """
        time.sleep(1)
        zhihu = Zhihu()
        response = zhihu.unfollow(profile_url="https://www.zhihu.com/people/gao-yu-dong-41")
        self.assertIn(response, 'follower_count')

    def test_unfollow_with_user_slug(self):
        """
        带user_slug，返回follower数量
        :return:
        """
        time.sleep(1)
        zhihu = Zhihu()
        response = zhihu.unfollow(user_slug="xiaoxiaodouzi")
        self.assertIn(response, 'follower_count')

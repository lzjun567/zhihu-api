# encoding: utf-8
__author__ = 'liuzhijun'

import unittest
from zhihu.models.zhihux import ZhihuX

class ZhihuXTestCase(unittest.TestCase):
    def test_user_profile(self):
        """
        获取用户信息
        :return:
        """
        zhihu = Model()
        profile = zhihu.user(user_slug="xiaoxiaodouzi")
        data = {'avatar_url_template': 'https://pic1.zhimg.com/v2-ca13758626bd7367febde704c66249ec_{size}.jpg',
                'name': '我是小号',
                'is_advertiser': False, 'url': 'http://www.zhihu.com/api/v4/people/1da75b85900e00adb072e91c56fd9149',
                'gender': -1, 'user_type': 'people', 'url_token': 'xiaoxiaodouzi', 'headline': '程序员',
                'avatar_url': 'https://pic1.zhimg.com/v2-ca13758626bd7367febde704c66249ec_is.jpg', 'is_org': False,
                'type': 'people', 'badge': [], 'id': '1da75b85900e00adb072e91c56fd9149'}
        self.assertEqual(data, profile)

    def test_send_message(self):
        """
        不带关键字参数，抛出异常
        :return:
        """
        zhihu = ZhihuX().send_message("nihhao", user_slug="zhijun-liu")
        print(zhihu)

# encoding: utf-8
import unittest

from zhihu import Zhihu
from zhihu.error import ZhihuError


class CommonTestCase(unittest.TestCase):
    def test_send_message_with_no_kwargs(self):
        """
        不带关键字参数，抛出异常
        :return:
        """
        zhihu = Zhihu()
        self.assertRaises(ZhihuError, zhihu.send_message, "hello")

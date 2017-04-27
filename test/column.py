# encoding: utf-8

from zhihu import Column
import unittest
import time


class ColumnTestCase(unittest.TestCase):

    def test_followers_with_slug(self):
        slug = "pythoneer"
        from zhihu import Zhihu
        data = Column(slug=slug).followers(limit=10, headers=Zhihu().)
        self.assertEqual(10, len(data))



# https://zhuanlan.zhihu.com/api/columns/pythoneer/followers
# https://zhuanlan.zhihu.com/api/columns/pythoneer/followers
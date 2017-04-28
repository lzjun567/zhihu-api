# encoding: utf-8

import unittest

from zhihu import Column


class ColumnTestCase(unittest.TestCase):
    def test_followers_with_slug(self):
        slug = "pythoneer"
        data = Column(slug=slug).followers(limit=10)
        self.assertEqual(10, len(data))

    def test_followers_with_url(self):
        url = "https://zhuanlan.zhihu.com/pythoneer"
        data = Column(url=url).followers(limit=10)
        self.assertEqual(10, len(data))

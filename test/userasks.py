# encoding: utf-8

import unittest

from zhihu import Userasks


class UserasksTestCase(unittest.TestCase):
    def test_asks_list_with_slug(self):
        slug = "heikehuawuya"
        data = Userasks(slug=slug).asks_list()
        self.assertIn('黑客电影和现实区别？', data)

    def test_asks_list_with_url(self):
        url = "https://www.zhihu.com/people/heikehuawuya"
        data = Userasks(url=url).asks_list()
        self.assertIn('黑客电影和现实区别？', data)

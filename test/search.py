# encoding: utf-8

from zhihu import Search
import unittest
import time


class SearchTestCase(unittest.TestCase):
    def setUp(self):
        self.search = Search()

    def test_search_question(self):
        time.sleep(1)
        ids, titles = self.search.search_question('python', 20)
        self.assertEqual(len(ids), len(titles), msg="The numbers of IDs and titles we get should be the same.")
        self.assertEqual(len(ids), 20, msg="We should get 20 IDs.")
        self.assertEqual(len(ids), len(set(ids)), msg="All the IDs should be unique.")

    def test_search_people(self):
        time.sleep(1)
        ids, names = self.search.search_people('python', 20)
        self.assertEqual(len(ids), len(names), msg="The numbers of IDs and names we get should be the same.")
        self.assertEqual(len(ids), 20, msg="We should get 20 IDs.")
        self.assertEqual(len(ids), len(set(ids)), msg="All the IDs should be unique.")

    def test_search_topic(self):
        time.sleep(1)
        ids, topics = self.search.search_topic('python', 20)
        self.assertEqual(len(ids), len(topics), msg="The numbers of IDs and topics we get should be the same.")
        self.assertEqual(len(ids), 20, msg="We should get 20 IDs.")
        self.assertEqual(len(ids), len(set(ids)), msg="All the IDs should be unique.")

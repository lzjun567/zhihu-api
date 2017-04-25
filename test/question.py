from zhihu import Answer
from zhihu import Question
import unittest
import time


class QuestionTestCase(unittest.TestCase):
    def test_follow_question(self):
        data = Question(id=58809107).follow_question()
        self.assertIn("is_following", data)
        self.assertIn("true", data)

    def test_unfollow_question(self):
        data = Question(id=58809107).unfollow_question()
        self.assertEqual(204, data)


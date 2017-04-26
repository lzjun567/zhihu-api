from zhihu import Answer
from zhihu import Question
import unittest
import time


class QuestionTestCase(unittest.TestCase):
    def test_follow_question_with_id(self):
        data = Question(id=32096743).follow_question()
        self.assertIn("is_following", data)
        self.assertIn("true", data)

    def test_unfollow_question_with_id(self):
        data = Question(id=32096743).unfollow_question()
        self.assertEqual('', data)

    def test_follow_question_with_url(self):
        data = Question(url='https://www.zhihu.com/question/58684385').follow_question()
        self.assertIn("is_following", data)
        self.assertIn("true", data)

    def test_unfollow_question_with_url(self):
        data = Question(url='https://www.zhihu.com/question/58684385').unfollow_question()
        self.assertEqual('', data)



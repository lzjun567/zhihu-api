# encoding: utf-8

from zhihu import Answer
import unittest
import time


class AnswerTestCase(unittest.TestCase):
    def test_vote_up_with_id(self):
        data = Answer(id=14005147).vote_up()
        self.assertIn("voting", data)
        self.assertIn("voteup_count", data)

    def test_vote_up_with_url(self):
        time.sleep(1)
        answer = Answer(url="https://www.zhihu.com/question/19761434/answer/14005147")
        data = answer.vote_up()
        self.assertEqual("14005147", answer.id)
        self.assertIn("voting", data)
        self.assertIn("voteup_count", data)

    def test_vote_down_with_id(self):
        time.sleep(1)
        data = Answer(id=14005147).vote_down()
        self.assertIn("voting", data)
        self.assertIn("voteup_count", data)

    def test_vote_neutral_with_url(self):
        time.sleep(1)
        data = Answer(url="https://www.zhihu.com/question/19761434/answer/14005147").vote_neutral()
        self.assertIn("voting", data)
        self.assertIn("voteup_count", data)

    def test_thank_with_url(self):
        time.sleep(1)
        data = Answer(url="https://www.zhihu.com/question/19761434/answer/14005147").thank()
        self.assertIn("is_thanked", data)
        self.assertIn("true", data)

    def test_thank_cancel_with_url(self):
        time.sleep(1)
        data = Answer(url="https://www.zhihu.com/question/19761434/answer/14005147").thank_cancel()
        self.assertIn("is_thanked", data)
        self.assertIn("false", data)

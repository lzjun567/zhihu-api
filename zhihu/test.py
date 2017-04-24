from zhihu import Answer
from zhihu import Article
import unittest
import time


class AnswerTestCase(unittest.TestCase):
    def test_vote_up_with_id(self):
        data = Answer(id=14005147).vote_up()
        print(data)
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

    def test_vote_nature_with_url(self):
        time.sleep(1)
        data = Answer(url="https://www.zhihu.com/question/19761434/answer/14005147").vote_neutral()
        self.assertIn("voting", data)
        self.assertIn("voteup_count", data)

class ArticleTestCase(unittest.TestCase):
    def test_request(self):
        article = Article(id=26096748)
        data = article.request()
        self.assertIn("content", data.keys())
        self.assertIn("content", article.__dict__.keys())
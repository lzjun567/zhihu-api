from zhihu import Answer
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
    def test_vote_up_with_id(self):
        time.sleep(1)
        data=Article(id="26415908")
        
        #self.assertIn("like",data)

        #assertIn这边还没有很清楚

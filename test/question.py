# encoding: utf-8
import unittest

from zhihu import Question


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

    def test_follow_question_with_answer_url(self):
        """
        也支持回答的URL，因为从回答中也能找到问题的ID
        :return:
        """
        data = Question(url='https://www.zhihu.com/question/59001738/answer/160832685').follow_question()
        self.assertIn("is_following", data)
        self.assertIn("true", data)

    def test_unfollow_question_with_url(self):
        data = Question(url='https://www.zhihu.com/question/58684385').unfollow_question()
        self.assertEqual('', data)

    def test_get_comments_with_id(self):
        total, data = Question(id=23497514).get_comments()
        self.assertEqual(type(total), type(0))
        self.assertEqual(type(data), type([]))

    def test_get_comments_with_url(self):
        total, data = Question(url='https://www.zhihu.com/question/23497514').get_comments()
        self.assertEqual(type(total), type(0))
        self.assertEqual(type(data), type([]))

    def test_make_comments_with_id(self):
        data = Question(id=22519728).make_comments(u"好")
        self.assertIn('allow_reply', data)

    def test_make_comments_with_url(self):
        data = Question(url='https://www.zhihu.com/question/21155768').make_comments("老问题了")
        self.assertIn('type', data)


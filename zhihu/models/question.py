# encoding: utf-8

import re
import json

from zhihu.auth import need_login
from zhihu.error import ZhihuError
from zhihu.models import Model
from zhihu.url import URL


class Question(Model):
    def __init__(self, id=None, url=None):
        id = id if id is not None else self._extract_id(url)
        if not id:
            raise ZhihuError("没有指定问题的id或者url")
        self.id = str(id)
        super(Question, self).__init__()

    @staticmethod
    def _extract_id(url):
        """
        从url中提取目标id
        """
        pattern = re.compile("https://www.zhihu.com/question/(\d+).*?")
        match = pattern.search(url)
        return match.group(1) if match else None

    @need_login
    def follow_question(self, **kwargs):
        """关注某问题"""
        return self._execute(url=URL.follow_question(self.id), **kwargs)

    @need_login
    def unfollow_question(self, **kwargs):
        """取消关注某问题"""
        return self._execute(method="delete", url=URL.unfollow_question(self.id), **kwargs)

    @need_login
    def get_comments(self, **kwargs):
        """查看当前的评论"""
        data = {
            "include": 'data%5B*%5D.author%2Ccollapsed%2Creply_to_author%2Cdisliked%2Ccontent%2Cvoting%2Cvote_count%2Cis_parent_author%2Cis_author,',
            "order": 'normal',
            "limit": "10",
            "offset": "0",
            "status": "0",
        }
        data = self._execute(method="get", url=URL.get_comments(self.id) + 'comments?', data=data, **kwargs)
        # print(type(data))
        dataObj = json.loads(data)
        # print(type(dataObj))
        totals = dataObj['paging']['totals']
        content_data = dataObj['data']
        return totals, content_data

    @need_login
    def make_comments(self, comment, **kwargs):
        """添加评论"""
        comment = comment
        data = {
            "include": 'author,collapsed,reply_to_author,disliked,content,voting,vote_count,is_parent_author,is_author',
            "content": "<p>" + comment + "</p>",
        }
        response = self._execute(method="post", url=URL.make_comments(self.id), data=data, **kwargs)
        return response

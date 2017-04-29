# encoding: utf-8

import re

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

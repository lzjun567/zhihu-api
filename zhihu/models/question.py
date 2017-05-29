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

    # def _execute(self, method="post", url=None, data=None, **kwargs):
    #     super(Question, self)._execute(method=method, url=url, data=data, **kwargs)

    @need_login
    def follow_question(self, **kwargs):
        """关注某问题"""
        r = self._execute(url=URL.follow_question(self.id), **kwargs)
        if r.ok:
            return r.json()
        else:
            raise ZhihuError("操作失败：%s" % r.text)

    @need_login
    def unfollow_question(self, **kwargs):
        """取消关注某问题"""
        r = self._execute(method="delete", url=URL.unfollow_question(self.id), **kwargs)
        if r.ok:
            return {'is_following': False}
        else:
            raise ZhihuError("操作失败：%s" % r.text)

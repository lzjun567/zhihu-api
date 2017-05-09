# encoding: utf-8

import re

from zhihu.auth import need_login
from zhihu.error import ZhihuError
from zhihu.models import Model
from zhihu.url import URL


class Answer(Model):
    def __init__(self, id=None, url=None):
        id = id if id is not None else self._extract_id(url)
        if not id:
            raise ZhihuError("没有指定回答的id或者url")
        self.id = str(id)
        super(Answer, self).__init__()

    @staticmethod
    def _extract_id(url):
        """
        从url中提取目标id
        """
        pattern = re.compile("https://www.zhihu.com/question/\d+/answer/([\w-]+)")
        match = pattern.search(url)
        return match.group(1) if match else None

    @need_login
    def vote_up(self, **kwargs):
        """
        赞同
        """
        r = self._execute(url=URL.vote_up(self.id), data={"type": "up"}, **kwargs)
        if r.ok:
            return r.json()

    @need_login
    def vote_down(self, **kwargs):
        """
        反对
        """
        r = self._execute(url=URL.vote_down(self.id), data={"type": "down"}, **kwargs)
        if r.ok:
            return r.json()

    @need_login
    def vote_neutral(self, **kwargs):
        """
        中立
        """
        r = self._execute(url=URL.vote_neutral(self.id), data={"type": "neutral"}, **kwargs)
        if r.ok:
            return r.json()

    @need_login
    def thank(self, **kwargs):
        """
        感谢
        """
        r = self._execute(url=URL.thank(self.id), **kwargs)
        if r.ok:
            return r.json()

    @need_login
    def thank_cancel(self, **kwargs):
        """
        感谢取消
        """
        r = self._execute(method="delete", url=URL.thank_cancel(self.id), **kwargs)
        if r.ok:
            return r.json()

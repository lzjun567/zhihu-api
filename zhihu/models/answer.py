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
            raise ZhihuError("没有指定回答的id")
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

    def request(self, method=None, url_name=None, data=None, **kwargs):
        url_name = getattr(URL, url_name)(self.id)
        r = getattr(self._session, method)(url_name, json=data, **kwargs)
        if r:
            self.log("操作成功")
        else:
            self.log("操作失败")
        return r.text

    @need_login
    def vote_up(self, **kwargs):
        """
        赞同
        """
        return self.request(method="post", url_name="vote_up", data={"type": "up"}, **kwargs)

    @need_login
    def vote_down(self, **kwargs):
        """
        反对
        """
        return self.request(method="post", url_name="vote_up", data={"type": "down"}, **kwargs)

    @need_login
    def vote_neutral(self, **kwargs):
        """
        中立
        """
        return self.request(method="post", url_name="vote_up", data={"type": "neutral"}, **kwargs)

    @need_login
    def thank(self, **kwargs):
        """
        感谢
        """
        return self.request(method="post", url_name="thank", **kwargs)

    @need_login
    def thank_cancel(self, **kwargs):
        """
        感谢取消
        """
        return self.request(method="delete", url_name="thank", **kwargs)

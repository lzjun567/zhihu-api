# encoding: utf-8

import re

from zhihu.url import URL
from zhihu.models import Model
from zhihu.auth import need_login


class Answer(Model):
    def __init__(self, id=None, url=None):
        self.id = str(id)
        if id is None and url:
            pattern = re.compile("https://www.zhihu.com/question/\d+/answer/([\w-]+)")
            match = pattern.search(url)
            if match:
                self.id = match.group(1)
        super(Answer, self).__init__()

    def request(self, method=None, url=None, data=None, **kwargs):
        url = getattr(URL, url)(self.id)
        r = getattr(self._session, method)(url, json=data, **kwargs)
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
        return self.request(method="post", url="vote_up", data={"type": "up"}, **kwargs)

    @need_login
    def vote_down(self, **kwargs):
        """
        反对
        """
        return self.request(method="post", url="vote_up", data={"type": "down"}, **kwargs)

    @need_login
    def vote_neutral(self, **kwargs):
        """
        中立
        """
        return self.request(method="post", url="vote_up", data={"type": "neutral"}, **kwargs)

    @need_login
    def thank(self, **kwargs):
        """
        感谢
        """
        return self.request(method="post", url="thank", **kwargs)

    @need_login
    def thank_cancel(self, **kwargs):
        """
        感谢取消
        """
        return self.request(method="delete", url="thank", **kwargs)

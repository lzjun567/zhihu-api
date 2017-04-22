# encoding: utf-8

from zhihu.url import URL
from . import Model
import re


class Answer(Model):
    def __init__(self, id=None, url=None):
        self.id = str(id)
        if id is None and url:
            pattern = re.compile("https://www.zhihu.com/question/\d+/answer/([\w-]+)")
            match = pattern.search(url)
            if match:
                self.id = match.group(1)
        super(Answer, self).__init__()

    def request(self, data=None, **kwargs):
        url = URL.vote_up(self.id)
        r = self._session.post(url, json=data, **kwargs)
        if r.ok:
            self.log("操作成功")
        else:
            self.log("操作失败")
        return r.text

    def vote_up(self, **kwargs):
        """
        赞同
        """
        return self.request(data={"type": "up"}, **kwargs)

    def vote_down(self, **kwargs):
        """
        反对
        """
        return self.request(data={"type": "down"}, **kwargs)

    def vote_neutral(self, **kwargs):
        """
        中立
        """
        return self.request(data={"type": "neutral"}, **kwargs)

# encoding: utf-8

import re

from zhihu.url import URL
from zhihu.models import Model
from zhihu.auth import need_login


class Question(Model):
    def __init__(self, id=None, url=None):
        self.id = str(id)
        if id is None and url:
            pattern = re.compile("https://www.zhihu.com/question/\d+/answer/([\w-]+)")
            match = pattern.search(url)
            if match:
                self.id = match.group(1)
        super(Question, self).__init__()

    def request(self, method=None, url_name=None, data=None, **kwargs):
        url_name = getattr(URL, url_name)(self.id)
        r = getattr(self._session, method)(url_name, json=data, **kwargs)
        if r.status_code==204:
            print("取消关注成功")
            self.log("操作成功")
            return r.status_code
        elif r.status_code==200:
            print("操作成功")
            self.log("操作失败")
        return r.text

    @need_login
    def follow_question(self, **kwargs):
        """关注某问题"""
        return self.request(method="post", url_name="follow_question", data=None, **kwargs)

    @need_login
    def unfollow_question(self, **kwargs):
        """取消关注某问题"""
        return self.request(method="delete", url_name="unfollow_question", data=None, **kwargs)


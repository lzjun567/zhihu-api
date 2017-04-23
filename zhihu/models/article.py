# encoding: utf-8

from zhihu.url import URL
from . import Model

from ..auth import need_login

class Article(Model):
    def __init__(self, id=None):
        self.id=str(id)


    @need_login
    def vote_up(self, **kwargs):
        '''
        文章赞同
        '''
        url=URL.vote_up(self.id)
        r=self._session.put(url, **kwargs)
        if r.ok:
            self.log("操作成功")
        else:
            self.log("操作失败")

        return r.text

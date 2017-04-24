from zhihu.url import URL
from zhihu.auth import need_login
from . import Model
import re

class Article(Model):
    def __init__(self, id=None, url=None):
        self.id = str(id)
        if id is None and url:
            pattern = re.compile("https://zhuanlan.zhihu.com/p/(\d+)")
            match = pattern.search(url)
            if match:
                self.id = match.group(1)
        super(Article, self).__init__()

    @need_login
    def request(self, **kwargs):
        url = URL.article(self.id)
        self._session.headers['Host'] = 'zhuanlan.zhihu.com'
        response = self._session.get(URL.article(self.id))
        self._session.headers['Host'] = 'www.zhihu.com'
        if response.ok:
            data = response.json()
            for key,val in data.items():
                self.__dict__[key] = val # ['excerptTitle', 'summary', 'tipjarState', 'reviewers', 'author', 'slug', 'links', 'meta', 'reviewingCommentsCount', 'url', 'titleImageSize', 'rating', 'title', 'likesCount', 'collapsedCount', 'canComment', 'content', 'topics', 'pageCommentsCount', 'commentsCount', 'sourceUrl', 'state', 'href', 'commentPermission', 'publishedTime', 'snapshotUrl', 'isTitleImageFullScreen', 'titleImage', 'lastestLikers']
            return data
        else:
            self.logger.error(u"文章获取失败, status code: %s" % response.status_code)
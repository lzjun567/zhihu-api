# encoding: utf-8

from bs4 import BeautifulSoup

from zhihu.auth import need_login
from zhihu.error import ZhihuError
from zhihu.models import Model
from zhihu.url import URL

class Search(Model):
    @need_login
    def search_content(self, q=''):
        """
        搜索内容
        :param q: 搜索关键词
        :return: (ids, titles) 问题id与题目
        >>> search = zhihu.Search()
        >>> search.search_content('python')
        """
        html = self._get_search_response(type='content', q=q)
        return self._extract_questions(html)

    def _get_search_response(self, type='content', q=''):
        response = self._session.get(URL.search(), params={'type': type, 'q':q})
        return response.text

    def _extract_questions(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.find('ul', {'class': ['list', 'contents', 'navigable']})
        ids = [li.div.a['href'][10:] for li in ul.findChildren() if li.name == 'li']
        titles = [li.div.a.getText() for li in ul.findChildren() if li.name == 'li']
        return ids, titles

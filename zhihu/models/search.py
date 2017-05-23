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
        html = self._get_search_response(search_type='content', key_words=q)
        return self._extract_questions(html)

    def _get_search_response(self, search_type='content', key_words=''):
        response = self._session.get(URL.search(), params={'type': search_type, 'q': key_words})
        return response.text

    @staticmethod
    def _extract_questions(html):
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.find('ul', {'class': ['list', 'contents', 'navigable']})
        ids = [li.div.a['href'][10:] for li in ul.findChildren(recursive=False)]
        titles = [li.div.a.getText() for li in ul.findChildren(recursive=False)]
        return ids, titles

# encoding: utf-8

from bs4 import BeautifulSoup

from zhihu.auth import need_login
from zhihu.error import ZhihuError
from zhihu.models import Model
from zhihu.url import URL

class Search(Model):
    @need_login
    def search_content(self, key_words='', number_of_results=10):
        """
        搜索内容
        :param key_words: 搜索关键词
        :param number_of_results: 想要获得的结果数量
        :return: (ids, titles) 问题id与题目
        >>> search = zhihu.Search()
        >>> search.search_content('python', 10)
        """
        html = self._get_search_response(search_type='content', key_words=key_words)
        ids, titles = self._extract_questions(html)
        offset = 10
        while len(titles) < number_of_results:
            html = self._get_search_response(search_type='content', key_words=key_words, get_more=True, offset=offset)
            if not html:
                break
            new_ids, new_titles = self._extract_questions(html, get_more=True)
            ids += new_ids
            titles += new_titles
            offset += 10
        return ids[:number_of_results], titles[:number_of_results]

    def _get_search_response(self, search_type='content', key_words='', get_more=False, offset=0):
        if get_more:
            params = {
                'type': search_type,
                'q': key_words,
                'correction': 0,
                'offset': offset
            }
            response = self._session.get(URL.search(get_more=True), params=params)
            return response.json()['htmls'][0]
        else:
            response = self._session.get(URL.search(), params={'type': search_type, 'q': key_words})
            return response.text

    @staticmethod
    def _extract_questions(html, get_more=False):
        soup = BeautifulSoup(html, 'html.parser')
        if get_more:
            parent = soup
        else:
            parent = soup.find('ul', {'class': ['list', 'contents', 'navigable']})
        ids = [li.div.a['href'][10:] for li in parent.findChildren(recursive=False) if "question" in li.div.a['href']]
        titles = [li.div.a.getText() for li in parent.findChildren(recursive=False) if "question" in li.div.a['href']]
        return ids, titles

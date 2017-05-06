#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__mtime__ = 2017/5/1 0001
"""

import re

from zhihu.auth import need_login
from zhihu.error import ZhihuError
from zhihu.models import Model
from zhihu.url import URL
from bs4 import BeautifulSoup


class Userasks(Model):
    """
    获取指定用户的“提问”列表
    """
    def __init__(self, slug=None, url=None):
        slug = slug if slug is not None else self._extract_slug(url)
        if not slug:
            raise ZhihuError("没有指定用户的的slug或者url")
        self.slug = slug
        super(Userasks, self).__init__()

    @staticmethod
    def _extract_slug(url):
        """
        从url中提取目标id
        :param url: 
        :return: 
        """
        pattern = re.compile("https://www.zhihu.com/people/(\w+).*?")
        match = pattern.search(url)
        return match.group(1) if match else None

    def asks_list(self, **kwargs):
        question_list = []
        url = []
        url.append(URL.user_asks(self.slug))
        response = self._session.get(URL.user_asks(self.slug),**kwargs)
        soup = BeautifulSoup(response.content, "html.parser")
        page_tag = soup.find(name="div", class_="Pagination")
        if page_tag:
            url = []
            for button in page_tag.find_all("button"):
                if re.match(r'^\d$', button.get_text()):
                    url.append(URL.user_asks(self.slug) + '?page=' + button.get_text())

        for page in url:
            response = self._session.get(page, **kwargs)
            soup = BeautifulSoup(response.content, "html.parser")
            tag_list = soup.find_all(name="div", class_="List-item")
            for name in tag_list:
                question_list.append(name.find("a").get_text())

        return question_list

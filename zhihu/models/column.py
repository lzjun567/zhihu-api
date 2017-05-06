# encoding: utf-8

import re

from zhihu.error import ZhihuError
from zhihu.models import Model
from zhihu.settings import ZHUANLAN_HEADERS
from zhihu.url import URL


class Column(Model):
    """
    专栏
    """

    def __init__(self, slug=None, url=None):
        slug = slug if slug is not None else self._extract_slug(url)
        if not slug:
            raise ZhihuError("没有指定专栏的的slug或者url")
        self.slug = slug
        super(Column, self).__init__(headers=ZHUANLAN_HEADERS)

    @staticmethod
    def _extract_slug(url):
        """
        从url中提取目标slug
        """
        pattern = re.compile("https://zhuanlan.zhihu.com/(\w+)/?.*?")
        match = pattern.search(url)
        return match.group(1) if match else None

    def followers(self, limit=500, offset=0, **kwargs):
        """
        用户关注列表
        :param limit: 最大获取条数,不能超过500条
        :param offset: 偏移量
        :return: 返回用户列表
        """
        r = self._session.get(URL.column_followers(self.slug), params={"limit": limit, "offset": offset}, **kwargs)
        return r.json()

# encoding: utf-8

import os
import re
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from ..decorators.auth import authenticated
from .base import Model
from ..error import ZhihuError
from ..url import URL


class Answer(Model):
    def __init__(self, id=None, url=None):
        id = id if id is not None else self._extract_id(url)
        if not id:
            raise ZhihuError("没有指定回答的id或者url")
        self.id = str(id)

        self.url = url
        super(Answer, self).__init__()

    @staticmethod
    def _extract_id(url):
        """
        从url中提取目标id
        """
        pattern = re.compile("https://www.zhihu.com/question/\d+/answer/([\w-]+)")
        match = pattern.search(url)
        return match.group(1) if match else None

    @authenticated
    def vote_up(self):
        """
        赞同
        """
        r = self._execute(method="post", url=URL.vote_up(self.id), json={"type": "up"})
        if r.ok:
            return r.json()
        else:
            raise ZhihuError("操作失败：%s" % r.text)

    @authenticated
    def vote_down(self):
        """
        反对
        """
        r = self._execute(method="post", url=URL.vote_down(self.id), json={"type": "down"})
        if r.ok:
            return r.json()
        else:
            raise ZhihuError("操作失败：%s" % r.text)

    @authenticated
    def vote_neutral(self, ):
        """
        中立
        """
        r = self._execute(method="post", url=URL.vote_neutral(self.id), json={"type": "neutral"})
        if r.ok:
            return r.json()
        else:
            raise ZhihuError("操作失败：%s" % r.text)

    @authenticated
    def thank(self):
        """
        感谢
        """
        r = self._execute(method="post", url=URL.thank(self.id))
        if r.ok:
            return r.json()
        else:
            raise ZhihuError("操作失败：%s" % r.text)

    @authenticated
    def thank_cancel(self):
        """
        感谢取消
        """
        r = self._execute(method="delete", url=URL.thank_cancel(self.id))
        if r.ok:
            return r.json()
        else:
            raise ZhihuError("操作失败：%s" % r.text)

    @authenticated
    def nothelp(self):
        """
        没有帮助
        """
        r = self._execute(method="delete", url=URL.nothelp(self.id))
        if r.ok:
            return r.json()
        else:
            raise ZhihuError("操作失败：%s" % r.text)

    @authenticated
    def nothelp_cancel(self):
        """
        撤销没有帮助
        """
        r = self._execute(method="delete", url=URL.nothelp_cancel(self.id))
        if r.ok:
            return r.json()
        else:
            raise ZhihuError("操作失败：%s" % r.text)

    def images(self, path="."):
        """
        提取回答中的图片
        :param path 保存路径
        """
        assert self.url, "必须指定URL"
        r = self._execute(method='get', url=self.url)
        soup = BeautifulSoup(r.text, 'lxml')
        content_tag = soup.find('div', class_="RichContent-inner")
        images = content_tag.find_all("img")
        result = []
        for i in images:
            url = i['src']
            if url.startswith("http"):
                filename = urlparse(url).path[1:]
                filename = os.path.join(path, filename)
                with open(filename, 'wb') as fd:
                    r = requests.get(url)
                    for chunk in r.iter_content(chunk_size=128):
                        fd.write(chunk)
                result.append(filename)
        return result

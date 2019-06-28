#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-06-26 20:08:54
# @Author  : Kelly Hwong

from zhihu.models.base import Model
from zhihu.decorators.auth import authenticated
from zhihu.decorators.slug import slug
from zhihu.error import ZhihuError
from zhihu.url import URL


class Collection(Model):
    def __init__(self, collection_id=None):
        if not collection_id:
            raise ZhihuError("没有指定收藏夹的id或者url")
        self.collection_id = str(collection_id)
        super(Collection, self).__init__()

    @authenticated
    def info(self, collection_id=None, **kwargs):
        """
        获取收藏夹信息
        :param collection_id : 收藏夹id

        :return:dict

        >>> Collection(collection_url="https://www.zhihu.com/collection/220173652")
        >>> Collection(collection_id=220173652)
        """
        r = self._execute(
            method="get", url=URL.follow_collection(self.collection_id), **kwargs)
        if r.ok:
            return r.json()
        else:
            raise ZhihuError("操作失败：%s" % r.text)

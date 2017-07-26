# encoding: utf-8

"""
判断方法中的是否有 usr_slug 参数的方法
如果有user_url，就自动专程user_slug
"""
from ..error import ZhihuError


def slug(func):
    def wrapper(self, *args, **kwargs):

        if "user_url" not in kwargs and 'user_slug' not in kwargs:
            raise ZhihuError("至少指定[user_url, user_slug]中的任意一个关键字参数")
        if 'user_slug' not in kwargs:
            user_slug = self._user_slug(user_url=kwargs.get("user_url"))
            kwargs['user_slug'] = user_slug

        return func(self, *args, **kwargs)

    return wrapper

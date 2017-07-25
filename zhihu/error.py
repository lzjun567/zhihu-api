# encoding: utf-8
__author__ = 'liuzhijun'


class ZhihuError(Exception):
    def __init__(self, *args, **kwargs):
        super(ZhihuError, self).__init__(*args, **kwargs)

# encoding: utf-8

"""
通用ＵＲＬ类,知乎官方ＵＲＬ接口地址
"""


class URL(object):
    # 登录
    @staticmethod
    def login():
        return "https://www.zhihu.com/login/email"

    # 私信
    @staticmethod
    def message():
        return "https://www.zhihu.com/api/v4/messages"

    # 验证码
    @staticmethod
    def captcha(timestamp):
        return 'https://www.zhihu.com/captcha.gif?r={timestamp}&type=login'

    # 首页
    @staticmethod
    def index():
        return "https://www.zhihu.com"

    # 用户信息
    @staticmethod
    def profile(url_token):
        return "https://www.zhihu.com/api/v4/members/{url_token}".format(url_token=url_token)

# encoding: utf-8

"""
通用ＵＲＬ类,知乎官方ＵＲＬ接口地址
"""


class URL(object):
    host = "https://www.zhihu.com"

    # 登录
    @staticmethod
    def login():
        return URL.host + "/login/email"

    # 私信
    @staticmethod
    def message():
        return URL.host + "/api/v4/messages"

    # 验证码
    @staticmethod
    def captcha(timestamp):
        return URL.host + "/captcha.gif?r={timestamp}&type=login".format(timestamp=timestamp)

    # 首页
    @staticmethod
    def index():
        return URL.host + ""

    # 用户信息
    @staticmethod
    def profile(user_slug):
        return URL.host + "/api/v4/members/{user_slug}".format(user_slug=user_slug)

    # 关注用户
    @staticmethod
    def follow_people(user_slug):
        return URL.host + "/api/v4/members/{user_slug}/followers".format(user_slug=user_slug)

    # 赞同/反对/中立
    @staticmethod
    def vote_up(answer_id):
        return URL.host + "/api/v4/answers/{id}/voters".format(id=answer_id)

    vote_down = vote_neutral = vote_up

    # 某答案下感谢答主/取消感谢
    @staticmethod
    def thank(answer_id):
        return URL.host + "/api/v4/answers/{id}/thankers".format(id=answer_id)

    thank_cancel = thank

    # 关注某问题/取消关注某问题
    @staticmethod
    def follow_question(question_id):
        return URL.host + "/api/v4/questions/{id}/followers".format(id=question_id)

    unfollow_question = follow_question

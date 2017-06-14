# encoding: utf-8
"""
通用ＵＲＬ类,知乎官方ＵＲＬ接口地址
"""

import time


class URL(object):
    host = "https://www.zhihu.com"
    zhuanlan_host = "https://zhuanlan.zhihu.com"

    # 邮箱登录
    @staticmethod
    def email_login():
        return URL.host + "/login/email"

    # 手机登录
    @staticmethod
    def phone_login():
        return URL.host + "/login/phone_num"

    # 私信
    @staticmethod
    def message():
        return URL.host + "/api/v4/messages"

    # 验证码
    @staticmethod
    def captcha(_type="login"):
        return URL.host + "/captcha.gif?r={timestamp}&type={type}".format(timestamp=str(int(time.time() * 1000)),
                                                                          type=_type)

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

    # 某答案没有帮助/撤销没有帮助
    @staticmethod
    def nothelp(answer_id):
        return URL.host + "/api/v4/answers/{id}/unhelpers".format(id=answer_id)

    nothelp_cancel = nothelp

    # 关注某问题/取消关注某问题
    @staticmethod
    def follow_question(question_id):
        return URL.host + "/api/v4/questions/{id}/followers".format(id=question_id)

    unfollow_question = follow_question

    # 专栏
    @staticmethod
    def column(slug):
        return "https://zhuanlan.zhihu.com/api/columns/{slug}".format(slug=slug)

    # 专栏主页
    @staticmethod
    def column_index(slug):
        return URL.zhuanlan_host + "/{slug}".format(slug=slug)

    # 专栏的关注者
    @staticmethod
    def column_followers(slug):
        a = URL.zhuanlan_host + "/api/columns/{slug}/followers".format(slug=slug)
        return a

    # 关注某专栏/取消关注某专栏
    @staticmethod
    def follow_column(slug):
        return URL.zhuanlan_host + "/api/columns/{slug}/follow".format(slug=slug)

    unfollow_column = follow_column

    # 注册用的短信验证码
    @staticmethod
    def register_sms_code():
        return URL.host + "/send_register_verification_code/sms"

    # 注册验证URL
    @staticmethod
    def register_validate():
        return URL.host + "/register/phone_num/validation"

    # 注册
    @staticmethod
    def register():
        return URL.host + "/register/phone_num"

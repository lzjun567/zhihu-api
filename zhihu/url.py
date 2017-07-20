# encoding: utf-8
"""
通用ＵＲＬ类,知乎官方ＵＲＬ接口地址
"""

import time


class URL(object):
    host = "https://www.zhihu.com"
    zhuanlan_host = "https://zhuanlan.zhihu.com"

    # 邮箱登录
    @classmethod
    def email_login(cls):
        return cls.host + "/login/email"

    # 手机登录
    @classmethod
    def phone_login(cls):
        return cls.host + "/login/phone_num"

    # 私信
    @classmethod
    def message(cls):
        return cls.host + "/api/v4/messages"

    # 验证码
    @classmethod
    def captcha(cls, _type="login"):
        return cls.host + "/captcha.gif?r={timestamp}&type={type}".format(timestamp=str(int(time.time(cls) * 1000)),
                                                                          type=_type)

    # 首页
    @classmethod
    def index(cls):
        return cls.host + ""

    # 用户信息
    @classmethod
    def profile(cls, user_slug):
        return cls.host + "/api/v4/members/{user_slug}".format(user_slug=user_slug)

    # 关注用户
    @classmethod
    def follow_people(cls, user_slug):
        return cls.host + "/api/v4/members/{user_slug}/followers".format(user_slug=user_slug)

    # 赞同/反对/中立
    @classmethod
    def vote_up(cls, answer_id):
        return cls.host + "/api/v4/answers/{id}/voters".format(id=answer_id)

    vote_down = vote_neutral = vote_up

    # 某答案下感谢答主/取消感谢
    @classmethod
    def thank(cls, answer_id):
        return cls.host + "/api/v4/answers/{id}/thankers".format(id=answer_id)

    thank_cancel = thank

    # 某答案没有帮助/撤销没有帮助
    @classmethod
    def nothelp(cls, answer_id):
        return cls.host + "/api/v4/answers/{id}/unhelpers".format(id=answer_id)

    nothelp_cancel = nothelp

    # 关注某问题/取消关注某问题
    @classmethod
    def follow_question(cls, question_id):
        return cls.host + "/api/v4/questions/{id}/followers".format(id=question_id)

    unfollow_question = follow_question

    # 专栏
    @classmethod
    def column(cls, slug):
        return "https://zhuanlan.zhihu.com/api/columns/{slug}".format(slug=slug)

    # 专栏主页
    @classmethod
    def column_index(cls, slug):
        return cls.zhuanlan_host + "/{slug}".format(slug=slug)

    # 专栏的关注者
    @classmethod
    def column_followers(cls, slug):
        a = cls.zhuanlan_host + "/api/columns/{slug}/followers".format(slug=slug)
        return a

    # 关注某专栏/取消关注某专栏
    @classmethod
    def follow_column(cls, slug):
        return cls.zhuanlan_host + "/api/columns/{slug}/follow".format(slug=slug)

    unfollow_column = follow_column

    # 注册用的短信验证码
    @classmethod
    def register_sms_code(cls):
        return cls.host + "/send_register_verification_code/sms"

    # 注册验证URL
    @classmethod
    def register_validate(cls):
        return cls.host + "/register/phone_num/validation"

    @classmethod
    def register(cls):
        return cls.host + "/register/phone_num"

    # 粉丝列表URL
    @classmethod
    def followers(cls, user_slug):
        return cls.host + "/api/v4/members/{slug}/followers?include=data[*].answer_count,gender,follower_count," \
                          "badge[?(type=best_answerer)].topics".format(slug=user_slug)

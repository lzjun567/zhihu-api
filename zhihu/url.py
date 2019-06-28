# encoding: utf-8
"""
通用ＵＲＬ类,知乎官方ＵＲＬ接口地址
"""

import time


class URL(object):
    host = "https://www.zhihu.com"
    zhuanlan_host = "https://zhuanlan.zhihu.com"

    @classmethod
    def api_login(cls):
        # API登陆
        return cls.host + "/api/v3/oauth/sign_in"

    @classmethod
    def api_captcha(cls):
        return cls.host + "/api/v3/oauth/captcha?lang=en"

    @classmethod
    def email_login(cls):
        # 邮箱登录
        return cls.host + "/login/email"

    @classmethod
    def phone_login(cls):
        # 手机登录
        return cls.host + "/login/phone_num"

    @classmethod
    def message(cls):
        # 私信
        return cls.host + "/api/v4/messages"

    @classmethod
    def captcha(cls, _type="login"):
        # 验证码
        return cls.host + "/captcha.gif?r={timestamp}&type={type}".format(timestamp=str(int(time.time() * 1000)),
                                                                          type=_type)

    @classmethod
    def index(cls):
        # 首页
        return cls.host + ""

    @classmethod
    def profile(cls, user_slug):
        # 用户信息
        return cls.host + "/api/v4/members/{user_slug}".format(user_slug=user_slug)

    @classmethod
    def follow_people(cls, user_slug):
        # 关注用户
        return cls.host + "/api/v4/members/{user_slug}/followers".format(user_slug=user_slug)

    @classmethod
    def vote_up(cls, answer_id):
        # 赞同/反对/中立
        return cls.host + "/api/v4/answers/{id}/voters".format(id=answer_id)

    vote_down = vote_neutral = vote_up

    @classmethod
    def thank(cls, answer_id):
        # 某答案下感谢答主/取消感谢
        return cls.host + "/api/v4/answers/{id}/thankers".format(id=answer_id)

    thank_cancel = thank

    @classmethod
    def nothelp(cls, answer_id):
        # 某答案没有帮助/撤销没有帮助
        return cls.host + "/api/v4/answers/{id}/unhelpers".format(id=answer_id)

    nothelp_cancel = nothelp

    @classmethod
    def follow_question(cls, question_id):
        # 关注某问题/取消关注某问题
        return cls.host + "/api/v4/questions/{id}/followers".format(id=question_id)

    unfollow_question = follow_question

    @classmethod
    def follow_collection(cls, collection_id):
        # 关注某问题/取消关注某收藏夹
        return "https://api.zhihu.com/collections/{cid}".format(cid=collection_id)

    unfollow_collection = follow_collection

    @classmethod
    def column(cls, slug):
        # 专栏
        return "https://zhuanlan.zhihu.com/api/columns/{slug}".format(slug=slug)

    @classmethod
    def column_index(cls, slug):
        # 专栏主页
        return cls.zhuanlan_host + "/{slug}".format(slug=slug)

    @classmethod
    def column_followers(cls, slug):
        # 专栏的关注者
        return cls.zhuanlan_host + "/api/columns/{slug}/followers".format(slug=slug)

    @classmethod
    def follow_column(cls, slug):
        # 关注某专栏/取消关注某专栏
        return cls.zhuanlan_host + "/api/columns/{slug}/follow".format(slug=slug)

    unfollow_column = follow_column

    @classmethod
    def register_sms_code(cls):
        # 注册用的短信验证码
        return cls.host + "/send_register_verification_code/sms"

    @classmethod
    def register_validate(cls):
        # 注册验证URL
        return cls.host + "/register/phone_num/validation"

    @classmethod
    def register(cls):
        return cls.host + "/register/phone_num"

    @classmethod
    def followers(cls, user_slug):
        # 粉丝列表URL
        return cls.host + "/api/v4/members/{slug}/followers?include=data[*].answer_count,gender,follower_count," \
                          "badge[?(type=best_answerer)].topics".format(
                              slug=user_slug)

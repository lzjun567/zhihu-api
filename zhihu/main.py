import logging
# from zhihu import Answer
# from zhihu import Account

# account = Account()
# account.login("邮箱地址或者手机号码", "这里是密码")
# account.login("+33752962193", "zhihudetail")

# from zhihu import Zhihu
#
# z = Zhihu()
# z.user(user_slug="liuzhijun001")
#
#
# def vote_up_with_id():
#     data = Answer(id=14005147).vote_up()
#     print(data)


logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    # vote_up_with_id()
    # from zhihu import Question
    # Question(id="60231684").unfollow_question()

    # Zhihu().login("+33752962193", "zhihudetail")
    # model.login("158", "xxxx")

    # from zhihu import Zhihu
    #
    # profile  = Zhihu().user(user_slug="xiaoxiaodouzi")
    # # print(profile)
    #
    # from zhihu import Account
    #
    # account = Account()
    # account.register("续航小三", phone_num="+33752962193", password="zhihudetail")

    from zhihu.models.zhihux import ZhihuX
    data = ZhihuX().profile(user_slug="zhijun-liu")
    print(data)

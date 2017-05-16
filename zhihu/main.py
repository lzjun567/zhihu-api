from zhihu import Answer


def vote_up_with_id():
    data = Answer(id=14005147).vote_up()
    print(data)


from zhihu.models import Model
from zhihu.models.account import Account

import logging

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    # vote_up_with_id()

    # model = Account()
    # model.login("ssss@qq.com", "ssss")
    # model.login("158", "xxxx")

    from zhihu import Zhihu

    # zhihu = Zhihu()
    # print(zhihu)
    # profile  = zhihu.user(user_slug="xiaoxiaodouzi")
    # print(profile)

    from zhihu import Account

    account = Account()
    account.register("续航小三", phone_num="+33752962193", password="zhihudetail")


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

    zhihu = Zhihu()
    profile  = zhihu.user(user_slug="xiaoxiaodouzi")
    print(profile)


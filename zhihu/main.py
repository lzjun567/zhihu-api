from zhihu import Answer
from zhihu import Zhihu
from zhihu import Userasks
from zhihu import Column

def vote_up_with_id():
    data = Answer(id=14005147).vote_up()
    print(data)

<<<<<<< HEAD
def zhihu_user():
    data = Zhihu().user(user_slug="6xian")
    print(data)

def user_asks():
    data = Userasks(slug='heikehuawuya').asks_list()
    print(data)

def column():
    data = Column("pythoneer").followers(5)
    print(data)

if __name__ == '__main__':
    # vote_up_with_id()
    user_asks()


from zhihu.models import Model
from zhihu.models.account import Account

import logging

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    # vote_up_with_id()

    model = Account()
    model.login("ssss@qq.com", "ssss")
    model.login("158", "xxxx")


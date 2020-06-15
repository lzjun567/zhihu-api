# Python 3.6.1

import requests.utils
import pickle
from http.cookies import SimpleCookie

from zhihu import User
from zhihu import Answer
from zhihu import Account

zhihu = User()
print(zhihu.cookies)

# 用户登录
account = Account()
result = account.login()
print(result)

# 查看用户profile 成功
# profile = zhihu.profile(user_slug="xiaoxiaodouzi")
# print(profile)

# 发送私信 成功
# response = zhihu.send_message(content='TESTMESSAGE', user_slug="xiaoxiaodouzi")
# print(response)

# 关注用户 成功
# response = zhihu.follow(user_slug='SemitLee')
# print(response)

answer = Answer(url="https://www.zhihu.com/question/34401174/answer/389502954")
r = answer.images(path="images")
# print(r)
# 赞同答案 成功
response = answer.vote_neutral()
answer.thank_cancel()
# print(response)

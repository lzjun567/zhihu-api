
## 关于

Zhihu-API 的初衷是希望提供一套简洁、优雅的、Pythonic的API接口，面向的用户是对知乎数据有兴趣的群体，它可以用在数据分析、数据挖掘、增长黑客、以及希望通过程序自动完成知乎某个操作等应用场景。

注意:只支持Python3

## 安装

```python
pip install -U zhihu
# 或者安装最新包
pip install git+git://github.com/lzjun567/zhihu-api --upgrade
```

## 快速上手


```python

from zhihu import Zhihu
zhihu = Zhihu()

#获取用户基本信息
profile = zhihu.profile(user_slug="xiaoxiaodouzi")
print(profile)

>>>
{
    'name': '我是x',
     'headline': '程序员',
     'gender': -1,
     'user_type': 'people',
     'is_advertiser': False,
     'url_token': 'xiaoxiaodouzi',
     'id': '1da75b85900e00adb072e91c56fd9149',
     'is_org': False
}

# 发送私信
>>> zhihu.send_message(content="私信测试", user_slug="xiaoxiaodouzi")
<Response [200]>

# 关注用户
>>> zhihu.follow(user_slug="xiaoxiaodouzi")
{'follower_count': 12, 'followed': True}

# 取消关注
>>> zhihu.unfollow(user_slug="xiaoxiaodouzi")
{'follower_count': 11, 'followed': False}


>>> from zhihu import Answer
>>> answer = Answer(url="https://www.zhihu.com/question/62569341/answer/205327777")

# 赞同回答
>>> answer.vote_up()
{'voting': 1, 'voteup_count': 260}

# 反对
>>> answer.vote_down()
{'voting': -1, 'voteup_count': 259}

# 中立
>>> answer.vote_neutral()
{'voting': 0, 'voteup_count': 260}

# 感谢回答
>>> answer.thank()
{'is_thanked': True}

# 取消感谢
>>> answer.thank_cancel()
{'is_thanked': False}

# 提取回答中的图片
>>> answer.images(path="images")
['8160c14ea69b3a6674152f2c1ae6cd7a_b.jpg']


>>> from zhihu import Zhihu
>>> zhihu = Zhihu()
# 关注用户
>>>zhihu.follow(user_slug="zhijun-liu")

# 取消关注
>>>zhihu.unfollow(user_slug="zhijun-liu")

# 粉丝列表
>>> zhihu.followers(user_slug="zhijun-liu")



```


## 贡献者
欢迎 PR, 所有贡献者都将出现在这里，排名不分先后

* [@BigBorg](https://github.com/BigBorg)
* [@xiaowenlong100](https://github.com/xiaowenlong100)
* [@chenghengchao](https://github.com/chenghengchao)
* [@MaxPoon](https://github.com/MaxPoon)
* [@Oopswc](https://github.com/Oopswc)

## 交流
群已经加不进，可以先加微信：lzjun567 拉你入群

![群](https://dn-mhke0kuv.qbox.me/30f70119cd4a840560d4.jpeg)


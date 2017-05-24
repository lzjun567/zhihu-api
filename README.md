
## 关于

Zhihu-API 的初衷是希望提供一套简洁、优雅的、Pythonic的API接口，面向的用户是对知乎数据有兴趣的群体，它可以用在数据分析、数据挖掘、增长黑客、以及希望通过程序自动完成知乎某个操作等应用场景。

## 前置条件

* Python3.x
* Requests
* BeautifulSoup4

## 安装

```python
pip install git+git://github.com/lzjun567/zhihu-api --upgrade
```

### API

**个人信息**
```
>>> from zhihu import Zhihu
>>> zhihu = Zhihu()
>>> zhihu.user(user_slug="xiaoxiaodouzi")

{'avatar_url_template': 'https://pic1.zhimg.com/v2-ca13758626bd7367febde704c66249ec_{size}.jpg',
     'badge': [],
     'name': '我是小号',
     'headline': '程序员',
     'gender': -1,
     'user_type': 'people',
     'is_advertiser': False,
     'avatar_url': 'https://pic1.zhimg.com/v2-ca13758626bd7367febde704c66249ec_is.jpg',
     'url': 'http://www.zhihu.com/api/v4/people/1da75b85900e00adb072e91c56fd9149', 'type': 'people',
     'url_token': 'xiaoxiaodouzi',
     'id': '1da75b85900e00adb072e91c56fd9149',
     'is_org': False}
```

**私信发送**

```python
>>> zhihu.send_message("你好,问候2", user_slug="xiaoxiaodouzi")
```

**关注用户和被关注用户**

```
>>> zhihu.follows("高日日")
{"following": 30,
 "followers": 4}
```

**关注用户**
```
>>> zhihu.follow(user_slug="xiaoxiaodouzi")
{"follower_count": 6}
```
**取消关注**
```
>>> zhihu.unfollow(user_slug="xiaoxiaodouzi")
{'follower_count': 5}
```

**点赞回答**
```
>>> from zhihu import Answer
>>> data = Answer(id=14005147).vote_up()
>>> data
>>> {"voting": 1, "voteup_count": 314}
```

**反对**
```
>>> from zhihu import Answer
>>> data = Answer(id=14005147).vote_down()
>>> data
>>> {"voting": 1, "voteup_count": 314}
```


**中立**
```
>>> from zhihu import Answer
>>> data = Answer(id=14005147).vote_neutral()
>>> data
>>> {"voting": 1, "voteup_count": 314}
```


**专栏的关注列表**
```
>>> from zhihu import Column
>>> column = Column(url="https://zhuanlan.zhihu.com/pythoneer")
>>> column.followers(limit=2, offset=1)
[{u'bio': u'python', u'hash': u'463e2651f6a856d88c33bfb7fd673bf4', u'description': u'', u'isOrg': False,
              u'name': u'zpf1024', u'profileUrl': u'https://www.zhihu.com/people/zpf1024',
              u'avatar': {u'id': u'da8e974dc', u'template': u'https://pic1.zhimg.com/{id}_{size}.jpg'},
              u'isOrgWhiteList': False, u'slug': u'zpf1024', u'uid': 841267452498296832L},
             {u'bio': None, u'hash': u'45bbaa0aca55fec0d768ccb4845a1c53', u'description': u'', u'isOrg': False,
              u'name': u'keyoka', u'profileUrl': u'https://www.zhihu.com/people/yi-hu-84',
              u'avatar': {u'id': u'785bfd914', u'template': u'https://pic1.zhimg.com/{id}_{size}.jpg'},
              u'isOrgWhiteList': False, u'slug': u'yi-hu-84', u'uid': 43738302775296L}]
```


**关注专栏**
```
>>> column.follow()
关注专栏成功
```

**取消关注专栏**
```
>>> column.follow()
取消关注专栏成功
```

每个接口都提供了不只一种方式调用，更多参考单元测试里面的例子


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


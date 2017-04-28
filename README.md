### 目标

试图构建一个更加简洁、优雅的、Pythonic 的知乎 API。

### 使用场景
* 如果你想基于知乎社区做数据分析
* 如果你想通过程序自动给回答点赞
* 如果你想批量关注用户
* 如果你想批量发送信息
* 如果你想构建一个自己的知乎客户端
* 如果你想...

如果你有以上需求，那么 zhihu-api 项目可能适合你，不过你要记住，如果是批量操作，你需要有频次地操作，否则容易被知乎判断为机器人。

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
>>> from zhihu.zhihu import Zhihu
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

**关注用户**
```
>>> zhihu.follow(user_slug="xiaoxiaodouzi")
{"follower_count": 6}
```
**取消关注**
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

每个接口都提供了不只一种方式调用，更多参考单元测试里面的例子


## 贡献者
欢迎 PR, 所有贡献者都将出现在这里，排名部分先后

* [@BigBorg](https://github.com/BigBorg)
* [@xiaowenlong100](https://github.com/xiaowenlong100)
* [@chenghengchao](https://github.com/chenghengchao)
* [@MaxPoon](https://github.com/MaxPoon)
* [@Oopswc](https://github.com/Oopswc)

## 交流
群已经加不进，可以先加微信：lzjun567 拉你入群

![群](https://dn-mhke0kuv.qbox.me/30f70119cd4a840560d4.jpeg)


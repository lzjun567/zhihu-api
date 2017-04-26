## 项目简介

### 目标

试图构建一个更加简洁、优雅的、Pythonic 的知乎 API。

### 使用场景
* 如果你想自动给你喜欢的人点赞
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
pip install git+git://github.com/lzjun567/zhihu-api

# 升级到最新的代码，附加参数  --upgrade
# 推荐
pip install git+git://github.com/lzjun567/zhihu-api --upgrade
```


## API

### 用户个人公开信息
```
>>> from zhihu.zhihu import Zhihu
>>> zhihu = Zhihu()
>>> zhihu.user(profile_url="https://www.zhihu.com/people/xiaoxiaodouzi")

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

# 还可以用
>>> zhihu.user(user_slug="xiaoxiaodouzi")

```

### 私信发送



```python
>>> zhihu.send_message("你好,问候3", user_id="1da75b85900e00adb072e91c56fd9149")

# 还支持 user_slug
>>> zhihu.send_message("你好,问候2", user_slug="xiaoxiaodouzi")

# 还支持 profile_url
>>> zhihu.zhihu.send_message("你好,问候1", profile_url="https://www.zhihu.com/people/xiaoxiaodouzi")
```

### 关注用户
```
>>> zhihu.follow(profile_url="https://www.zhihu.com/people/gao-yu-dong-41")
{"follower_count": 6}

>>> zhihu.follow(user_slug="xiaoxiaodouzi")
{"follower_count": 6}
```

### 点赞
```
>>> from zhihu import Answer
>>> data = Answer(id=14005147).vote_up()
>>> data
>>> {"voting": 1, "voteup_count": 314}

>>> data = Answer(url="https://www.zhihu.com/question/19761434/answer/14005147").vote_up()
```

### 反对
vote_down

### 中立
vote_neutral



## TODO

* 文章点赞
* ...

## 贡献者
欢迎 PR, 所有贡献者都将出现在这里，排名部分先后

* [@BigBorg](https://github.com/BigBorg)
* [@xiaowenlong100](https://github.com/xiaowenlong100)
* [chenghengchao](https://github.com/chenghengchao)
* [MaxPoon](https://github.com/MaxPoon)

## 交流
群已经加不进，可以先加微信：lzjun567 拉你入群

![群](https://dn-mhke0kuv.qbox.me/30f70119cd4a840560d4.jpeg)


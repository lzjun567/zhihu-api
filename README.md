## 项目简介

### 目标

试图构建一个更加简洁、优雅的、Pythonic 的知乎 API。


## 前置条件

* Python3.x
* Requests
* BeautifulSoup4

## 安装

```python
git@github.com:lzjun567/zhihu-api.git
cd  zhihu-api
pip install -r requirement.txt
```

## API

### 用户个人公开信息
```
>>> from zhihu import Zhihu
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
欢迎 PR, 所有贡献者都将出现在这里

## 交流
群已经加不进，可以先加微信：lzjun567 拉你入群

![群](https://dn-mhke0kuv.qbox.me/30f70119cd4a840560d4.jpeg)


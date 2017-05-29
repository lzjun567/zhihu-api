入门
==========
.. module:: zhihu


登录
-------

    >>> Account().login("+xxxxx", "xxxxxxxx")
    输入验证码：ehmk
    True

注册
--------



用户信息
---------------------

    >>> from zhihu import Zhihu
    >>> Zhihu().user(user_slug="xiaoxiaodouzi")
    {
        'avatar_url_template': 'https://pic1.zhimg.com/v2-ca13758626bd7367febde704c66249ec_{size}.jpg',
        'name': '我是小号',
        'headline': '程序员',
        'gender': -1,
        'user_type': 'people',
        'url_token': 'xiaoxiaodouzi',
        'is_advertiser': False,
        'avatar_url': 'https://pic1.zhimg.com/v2-ca13758626bd7367febde704c66249ec_is.jpg',
        'url': 'http://www.zhihu.com/api/v4/people/1da75b85900e00adb072e91c56fd9149',
        'type': 'people',
        'badge': [],
        'id': '1da75b85900e00adb072e91c56fd9149',
        'is_org': False
    }
    >>>

关注用户
------------------------

    >>> Zhihu().follow(user_slug="liuzhijun001")
    {'follower_count': 8, 'followed': True}


取消关注
------------------------

   >>> Zhihu().unfollow(user_slug="liuzhijun001")
    {'follower_count': 7, 'followed': False}


私信
----

    >>> Zhihu().send_message(user_slug="liuzhijun001", content="你好")
    {'sender': {'avatar_url_template': 'https://pic1.zhimg.com/da8e974dc_{size}.jpg',
                'badge': [], 'name': '续航小三',
                'is_advertiser': False,
                'url': 'http://www.zhihu.com/api/v4/people/97996c282f7f033178c8c2f4a19ed8a5',
                'url_token': 'xu-hang-xiao-san',
                'user_type': 'people',
                'headline': 'x',
                'avatar_url': 'https://pic1.zhimg.com/da8e974dc_is.jpg',
                'is_org': False,
                'gender': -1,
                'type': 'people',
                'id': '97996c282f7f033178c8c2f4a19ed8a5'},
    'url': '',
    'has_read': False,
    'content': '你好',
    'receiver': {'avatar_url_template': 'https://pic1.zhimg.com/v2-2d1c4b6eee96f9bbe2816cdff8b42ac4_{size}.jpg',
                'badge': [],
                'name': '刘志军',
                'is_advertiser': False,
                'url': 'http://www.zhihu.com/api/v4/people/dcd3957ea2aa33ad705781be46a2480b',
                'url_token': 'liuzhijun001',
                'user_type': 'people',
                'headline': 'Python开发者',
                'avatar_url': 'https://pic1.zhimg.com/v2-2d1c4b6eee96f9bbe2816cdff8b42ac4_is.jpg',
                'is_org': False,
                'gender': 1,
                'type': 'people',
                'id': 'dcd3957ea2aa33ad705781be46a2480b'},
    'created_time': 1496020263,
    'type': 'message',
    'id': '2426993620'}


.. module:: zhihu.models.zhihu
.. autoclass:: Zhihu
    :members:


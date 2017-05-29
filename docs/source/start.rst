入门
==========
.. module:: zhihu

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


.. module:: zhihu.models.zhihu
.. autoclass:: Zhihu
    :members:


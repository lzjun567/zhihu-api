# encoding: utf-8
"""
通用的操作放在此模块中
"""
import logging

from . import Model
from ..auth import need_login
from ..error import ZhihuError
from ..url import URL

from zhihu.models import account

class Zhihu(account.Account):
    def __init__(self, **kwargs):
        super(Zhihu, self).__init__(**kwargs)
        
    @need_login
    def send_message(self, content, user_id=None, profile_url=None, user_slug=None, **kwargs):
        """
        给指定的用户发私信
        :param content 私信内容
        :param user_id 用户id
        :param profile_url: 用户主页地址
        :param user_slug : 用户的个性域名

        >>> send_message(profile_url = "https://www.zhihu.com/people/xiaoxiaodouzi")
        >>> send_message(user_slug = "xiaoxiaodouzi")
        >>> send_message(user_id = "1da75b85900e00adb072e91c56fd9149")
        """
        if not any([user_id, profile_url, user_slug]):
            raise ZhihuError("至少指定一个关键字参数")

        if user_id is None:
            user_slug = self._user_slug(
                profile_url) if user_slug is None else user_slug
            user_id = self._user_id(user_slug)

        data = {"type": "common", "content": content, "receiver_hash": user_id}
        response = self._session.post(URL.message(), json=data, **kwargs)
        if response.ok:
            return response.json()
            self.log("发送成功")
        else:
            self.log("发送失败")
            raise ZhihuError("操作失败：%s" % response.text)

    @need_login
    def user(self, user_slug=None, profile_url=None, **kwargs):
        """
        获取用户信息
        :param user_slug : 用户的个性域名
        :param profile_url: 用户主页地址

        :return:dict

        >>> user(profile_url = "https://www.zhihu.com/people/xiaoxiaodouzi")
        >>> user(user_slug = "xiaoxiaodouzi")

        """
        if not any([profile_url, user_slug]):
            raise ZhihuError("至少指定一个关键字参数")

        user_slug = self._user_slug(profile_url) if user_slug is None else user_slug
        response = self._session.get(URL.profile(user_slug), **kwargs)

        if response.ok:
            return response.json()
        else:
            raise ZhihuError("操作失败：%s" % response.text)

    @need_login
    def follow(self, user_slug=None, profile_url=None, **kwargs):
        """
        关注用户
        :param user_slug:
        :param profile_url:
        :return: {"follower_count": int}

        >>> follow(profile_url = "https://www.zhihu.com/people/xiaoxiaodouzi")
        >>> follow(user_slug = "xiaoxiaodouzi")
        """
        if not any([profile_url, user_slug]):
            raise ZhihuError("至少指定一个关键字参数")

        user_slug = self._user_slug(profile_url) if user_slug is None else user_slug
        response = self._session.post(URL.follow_people(user_slug), **kwargs)
        if response.ok:
            data = response.json()
            data['followed'] = True
            return data
        else:
            raise ZhihuError("操作失败：%s" % response.text)

    @need_login
    def unfollow(self, user_slug=None, profile_url=None, **kwargs):
        """
        取消关注用户
        :param user_slug:
        :param profile_url:
        :return: {"follower_count": int}

        >>> unfollow(profile_url = "https://www.zhihu.com/people/xiaoxiaodouzi")
        >>> unfollow(user_slug = "xiaoxiaodouzi")
        """
        if not any([profile_url, user_slug]):
            raise ZhihuError("至少指定一个关键字参数")

        user_slug = self._user_slug(
            profile_url) if user_slug is None else user_slug
        response = self._session.delete(URL.follow_people(user_slug), **kwargs)
        if response.ok:
            data = response.json()
            data['followed'] = False
            return data
        else:
            raise ZhihuError("操作失败：%s" % response.text)

    @need_login
    def followers(self, user_slug=None, profile_url=None, limit=20, offset=0, **kwargs):
        """
        获取某个用户的粉丝列表
        :param user_slug:
        :param profile_url:
        :param limit: 最大返回数量
        :param offset:游标
        :param kwargs:
        :return:
                {
                    "paging": {
                        "is_end": true,
                        "totals": 1381207,
                        "is_start": false,
                    },
                    "data": [{
                        "avatar_url_template": "https://pic1.zhimg.com/fdbce7544_{size}.jpg",
                        "badge": [],
                        "name": "OPEN",
                        "is_advertiser": false,
                        "url": "http://www.zhihu.com/api/v4/people/0fcb310a722c5bb99d864ace7bb2d89c",
                        "url_token": "open",
                        "user_type": "people",
                        "answer_count": 50,
                        "headline": "上知乎，恍然大悟！",
                        "avatar_url": "https://pic1.zhimg.com/fdbce7544_is.jpg",
                        "is_org": false,
                        "gender": 1,
                        "follower_count": 78,
                        "type": "people",
                        "id": "0fcb310a722c5bb99d864ace7bb2d89c"
                        },
                        ]
                    }
        """
        if not any([profile_url, user_slug]):
            raise ZhihuError("至少指定一个关键字参数")

        user_slug = self._user_slug(
            profile_url) if user_slug is None else user_slug

        r = self._session.get(URL.followers(user_slug),
                              params={"limit": limit, "offset": offset},
                              **kwargs)
        self.log(r.url)
        if r.ok:
            return r.json()
        else:
            self.log("status code %s, body: %s" % (r.status_code, r.text), level=logging.ERROR)
            raise ZhihuError("操作失败：%s" % r.text)

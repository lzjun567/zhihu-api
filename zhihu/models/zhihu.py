# encoding: utf-8

from . import Model
from ..auth import need_login
from ..error import ZhihuError
from ..url import URL


class Zhihu(Model):
    @need_login
    def send_message(self, content, user_id=None, profile_url=None, user_slug=None, **kwargs):
        """
        给指定的用户发私信
        :param content 私信内容
        :param user_id 用户id
        :param profile_url :用户主页地址
        :param user_slug : 用户的个性域名

        >>> send_message(profile_url = "https://www.zhihu.com/people/xiaoxiaodouzi")
        >>> send_message(user_slug = "xiaoxiaodouzi")
        >>> send_message(user_id = "1da75b85900e00adb072e91c56fd9149")
        """

        if not any([user_id, profile_url, user_slug]):
            raise ZhihuError("至少指定一个关键字参数")

        if user_id is None:
            user_slug = self._user_slug(profile_url) if user_slug is None else user_slug
            user_id = self._user_id(user_slug)

        data = {"type": "common", "content": content, "receiver_hash": user_id}
        response = self._session.post(URL.message(), json=data, **kwargs)
        data = response.json()
        if data.get("error"):
            self.logger.info("私信发送失败, %s" % data.get("error").get("message"))
        else:
            self.logger.info("发送成功")
        return data

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
            self.logger.error(u"获取用户信息失败, status code: %s" % response.status_code)

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
        response = self._session.post(URL.follow(user_slug), **kwargs)
        if response.ok:
            return response.json()
        else:
            self.logger.error(u"关注失败, status code: %s" % response.status_code)

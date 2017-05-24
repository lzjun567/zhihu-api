# encoding: utf-8
"""
通用的操作放在此模块中
"""

from zhihu.auth import need_login
from zhihu.error import ZhihuError
from zhihu.models import Model
from zhihu.url import URL


class Common(Model):
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
            return response.json()
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
            return response.json()
        else:
            raise ZhihuError("操作失败：%s" % response.text)
            
    def follows(self, user_name=None):
        """
        用户所关注人数，被关注的人数
        :param user_slug:
        :param profile_url:
        :return: {"follower_count": int}

        >>> follows(user_name = "高日日")
        """
        if not user_name:
            raise ZhihuError("至少指定一个关键字参数")

        user_slug = self._get_token(user_name)

        response = requests.get(URL.user_followed_number(user_slug), headers={'User-Agent':
                                         'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
                                     })
        if response.ok:
            soup = BeautifulSoup(response.text, 'lxml')
            init_data_renshu = soup.select('div[class="NumberBoard-value"]')

            dicts = dict()
            counts = 0
            for i in init_data_renshu:
                if counts < 1:
                    dicts["following"] = str(i.get_text())
                else:
                    dicts["followers"] = str(i.get_text())
                counts += 1

            print(dicts)
        else:
            raise ZhihuError("操作失败：%s" % response.text)

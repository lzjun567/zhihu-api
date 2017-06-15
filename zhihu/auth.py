# encoding: utf-8

import requests
import requests.utils

from zhihu.models.account import Account

"""
from zhihu.settings import HEADERS
以该形式导入的HEADERS，作为参数传入时
在获取xsrf时出了问题

    def _get_xsrf(self, url=None, **kwargs):  
        response = self._session.get(url or URL.index(), **kwargs)
        soup = BeautifulSoup(response.content, "html.parser")
        xsrf = soup.find('input', attrs={"name": "_xsrf"}).get("value")
        return xsrf
        
    这里soup.find(...)返回的是 NoneType

"""
agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
headers = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent': agent
}

try:
    input = raw_input  # py2
except:
    pass


def need_login(func):
    """
    用户认证装饰器(判断用户是否已经登录)
    """

    def wrapper(self, *args, **kwargs):
        success = False
        print('TEST')
        if 'd_c0' not in requests.utils.dict_from_cookiejar(self._session.cookies):
            while not success:
                account = input("请输入Email或者手机号码:")
                password = input("请输入密码:")
                success = self.login(account, password, headers = headers)
            if success:
                self._session.cookies.load(ignore_discard=True)

        return func(self, *args, **kwargs)

    return wrapper

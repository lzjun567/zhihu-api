# Python 3.6.1

from zhihu import Zhihu

zhihu = Zhihu()
profile = zhihu.profile(user_slug="xiaoxiaodouzi")
print(profile)
# encoding: utf-8

import logging
import re

from zhihu.models import Model
from zhihu.models import RequestDataType
from zhihu.url import URL


class Account(Model):
    def login(self, account, password, **kwargs):
        """
        账户登录
        :param account: email或者手机号码
        :param password:
        :param kwargs:
        :return:
        """
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        phone_regex = r"(^1\d{10}$)"
        email_pattern = re.compile(email_regex)
        phone_pattern = re.compile(phone_regex)

        if email_pattern.match(account):
            return self._login_with_email(account, password, **kwargs)
        elif phone_pattern.match(account):
            return self._login_with_phone(account, password, **kwargs)
        else:
            self.log("登录名错误，需要重新输入.", level=logging.ERROR)
            return False

    def _login_with_phone(self, phone, password, **kwargs):
        data = {
            '_xsrf': self._get_xsrf(),
            'password': password,
            'phone_num': phone,
            "captcha": self._get_captcha(),
            "remeber_me": "true",
        }
        return self._login_execute(url=URL.phone_login(), data=data, **kwargs)

    def _login_with_email(self, email, password, **kwargs):
        data = {'email': email,
                'password': password,
                '_xsrf': self._get_xsrf(**kwargs),
                "captcha": self._get_captcha(**kwargs),
                'remember_me': 'true'}
        return self._login_execute(url=URL.email_login(), data=data, **kwargs)

    def _login_execute(self, url=None, data=None, **kwargs):

        r = super(Account, self)._execute(method="post", url=url, data=data, data_type=RequestDataType.FORM_DATA,
                                          **kwargs)

        if r.ok:
            result = r.json()
            if result.get("r") == 0:
                self.log(result.get("msg"))
                self._session.cookies.save(ignore_discard=True)  # 保存登录信息cookies
                return True
            else:
                self.log(result.get("msg"), level=logging.ERROR)
                return False

        else:
            self.log("登录失败", level=logging.ERROR)
            self.log(r.text)
            return False

    def register(self, name=None, phone_num=None, password=None):
        register_url = "https://www.zhihu.com/register/phone_num/validation"
        data = {
            "fullname": name,
            "phone_num": phone_num,
            "password": password,
            # "captcha_type": "cn",
            "_xsrf": super(Account, self)._get_xsrf(),
            "captcha": super(Account, self)._get_captcha(_type="register"),
            "captcha_source": "register",
            # "captcha": {"img_size": [200, 44], "input_points": [[116.875, 30], [164.875, 29]]},
            "userInfo": {"viewport": [1586, 440, 1494913480568],
                         "trace": [[0, 0, 1494913482574], [0, 0, 1494913483076], [0, 0, 1494913483577],
                                   [0, 0, 1494913484077], [0, 0, 1494913484578], [0, 0, 1494913485080],
                                   [0, 0, 1494913485580], [0, 0, 1494913486081], [0, 0, 1494913486582],
                                   [0, 0, 1494913487083], [0, 0, 1494913487583], [0, 0, 1494913488085],
                                   [0, 0, 1494913488585], [0, 0, 1494913489086], [0, 0, 1494913489586],
                                   [0, 0, 1494913490086], [0, 0, 1494913490588], [0, 0, 1494913491089],
                                   [0, 0, 1494913491589], [0, 0, 1494913492090], [0, 0, 1494913492591],
                                   [0, 0, 1494913493092], [0, 0, 1494913493592], [0, 0, 1494913494092],
                                   [0, 0, 1494913494593], [0, 0, 1494913495093], [0, 0, 1494913495594],
                                   [0, 0, 1494913496094], [0, 0, 1494913496594], [0, 0, 1494913497095],
                                   [0, 0, 1494913497595], [0, 0, 1494913498095], [0, 0, 1494913498595],
                                   [0, 0, 1494913499096], [0, 0, 1494913499598], [0, 0, 1494913500099],
                                   [0, 0, 1494913500600], [0, 0, 1494913501101], [0, 0, 1494913501602],
                                   [0, 0, 1494913502102], [0, 0, 1494913502603], [0, 0, 1494913503104],
                                   [0, 0, 1494913503605], [0, 0, 1494913504107], [0, 0, 1494913504607],
                                   [0, 0, 1494913505107], [0, 0, 1494913505608], [0, 0, 1494913506108],
                                   [0, 0, 1494913506609], [0, 0, 1494913507109], [0, 0, 1494913507610],
                                   [0, 0, 1494913508110], [0, 0, 1494913508610], [0, 0, 1494913509111],
                                   [0, 0, 1494913509611], [0, 0, 1494913510111], [0, 0, 1494913510611],
                                   [0, 0, 1494913511112], [0, 0, 1494913511613], [0, 0, 1494913512113],
                                   [0, 0, 1494913512613], [0, 0, 1494913513114], [0, 0, 1494913513615],
                                   [0, 0, 1494913514115], [0, 0, 1494913514616], [0, 0, 1494913515116],
                                   [0, 0, 1494913515617], [0, 0, 1494913516117], [0, 0, 1494913516617],
                                   [0, 0, 1494913517117], [0, 0, 1494913517619], [0, 0, 1494913518119],
                                   [0, 0, 1494913518620], [682, 214, 1494913519120], [725, 75, 1494913519622],
                                   [725, 75, 1494913520123], [725, 75, 1494913520624], [725, 75, 1494913521124],
                                   [725, 75, 1494913521625], [663, 78, 1494913522127], [425, 434, 1494913522628],
                                   [425, 434, 1494913523128], [425, 434, 1494913523629], [425, 434, 1494913524130],
                                   [456, 419, 1494913524630], [456, 419, 1494913525130], [456, 419, 1494913525631],
                                   [456, 419, 1494913526132], [456, 419, 1494913526634], [456, 419, 1494913527134],
                                   [456, 419, 1494913527635], [456, 419, 1494913528135], [456, 419, 1494913528636],
                                   [456, 419, 1494913529136], [456, 419, 1494913529638], [456, 419, 1494913530139],
                                   [723, 160, 1494913530639], [751, 79, 1494913531140], [751, 79, 1494913531642],
                                   [751, 79, 1494913532142], [751, 79, 1494913532643], [751, 79, 1494913533143],
                                   [751, 79, 1494913533644], [751, 79, 1494913534146], [751, 79, 1494913534647],
                                   [751, 79, 1494913535148], [740, 113, 1494913535648], [755, 108, 1494913536148],
                                   [630, 107, 1494913536649], [630, 107, 1494913537150], [630, 140, 1494913537652],
                                   [683, 150, 1494913538152], [597, 155, 1494913538652], [597, 155, 1494913539154],
                                   [597, 155, 1494913539654], [597, 155, 1494913540155], [597, 155, 1494913540655],
                                   [597, 155, 1494913541157], [597, 155, 1494913541657], [595, 155, 1494913542157],
                                   [548, 232, 1494913542659], [642, 263, 1494913543159], [699, 244, 1494913543659],
                                   [483, 438, 1494913544161], [483, 438, 1494913544661], [483, 438, 1494913545162],
                                   [483, 438, 1494913545663], [483, 438, 1494913546164], [483, 438, 1494913546665],
                                   [483, 438, 1494913547165], [483, 438, 1494913547666], [483, 438, 1494913548166],
                                   [696, 380, 1494913548666], [700, 370, 1494913549168], [719, 341, 1494913549669],
                                   [758, 310, 1494913550170], [809, 239, 1494913550671], [829, 238, 1494913551172],
                                   [858, 238, 1494913551672], [834, 255, 1494913552173], [586, 437, 1494913552675],
                                   [586, 437, 1494913553176], [586, 437, 1494913553678], [586, 437, 1494913554179],
                                   [586, 437, 1494913554679], [659, 350, 1494913555179], [765, 310, 1494913555679],
                                   [424, 400, 1494913556181], [784, 303, 1494913556683], [784, 303, 1494913557184]],
                         "register": {
                             "submit": [["mouseenter", 31, 34, 1494913519074], ["mouseleave", 39, -1, 1494913519122],
                                        ["mouseenter", 6, 39, 1494913530466], ["mouseleave", 64, -5, 1494913530522],
                                        ["mouseenter", 7, 13, 1494913543972], ["mouseleave", -19, 37, 1494913543979],
                                        ["mouseenter", 103, 39, 1494913550130], ["mouseleave", 148, -1, 1494913550330],
                                        ["mouseenter", 152, 1, 1494913552204], ["mouseleave", 90, 44, 1494913552234],
                                        ["mouseenter", 94, 40, 1494913555338], ["mouseleave", 31, 43, 1494913555906],
                                        ["mouseenter", 100, 39, 1494913556339], ["mousedown", 141, 20, 1494913556951]],
                             "password": {
                                 "mouse": [["mouseenter", 42, 46, 1494913519154], ["mouseleave", 60, -1, 1494913519210],
                                           ["mouseenter", 70, 46, 1494913530554], ["mouseleave", 88, -3, 1494913530713],
                                           ["mouseenter", 88, 0, 1494913535707], ["mouseleave", 93, -3, 1494913535962],
                                           ["mouseenter", 0, 20, 1494913537746], ["mouseleave", -4, 26, 1494913538553]],
                                 "keyborad": [["keydown", 1494913539842], ["keydown", 1494913539970],
                                              ["keydown", 1494913540027], ["keyup", 1494913540036],
                                              ["keyup", 1494913540066], ["keydown", 1494913540163],
                                              ["keyup", 1494913540204], ["keyup", 1494913540258],
                                              ["keydown", 1494913540362], ["keyup", 1494913540474],
                                              ["keydown", 1494913540570], ["keyup", 1494913540652],
                                              ["keydown", 1494913540729], ["keyup", 1494913540857],
                                              ["keydown", 1494913540914], ["keydown", 1494913541018],
                                              ["keydown", 1494913541106], ["keyup", 1494913541138],
                                              ["keyup", 1494913541195], ["keyup", 1494913541237],
                                              ["keydown", 1494913541287], ["keyup", 1494913541387]]}, "phone_num": {
                                 "mouse": [["mouseenter", 63, 40, 1494913519219], ["mouseleave", 76, -4, 1494913519345],
                                           ["mouseenter", 3, 1, 1494913522146], ["mouseleave", -2, 5, 1494913522154],
                                           ["mouseenter", 88, 45, 1494913530713],
                                           ["mouseleave", 103, -1, 1494913530882],
                                           ["mouseenter", 107, 1, 1494913535394], ["mouseleave", 88, 48, 1494913535707],
                                           ["mouseenter", 93, 45, 1494913535962],
                                           ["mouseleave", -1, 26, 1494913536570]],
                                 "keyborad": [["keydown", 17, 1494913536962], ["keydown", 86, 1494913537171],
                                              ["keyup", 86, 1494913537329], ["keyup", 17, 1494913537401]]},
                             "fullname": {
                                 "mouse": [["mouseenter", 76, 44, 1494913519346], ["click", 81, 27, 1494913522049],
                                           ["mouseleave", 27, 27, 1494913522054], ["mouseenter", 79, 19, 1494913522055],
                                           ["click", 79, 19, 1494913522056], ["mouseleave", 27, 27, 1494913522057],
                                           ["mouseenter", 27, 27, 1494913522057], ["click", 27, 27, 1494913522058],
                                           ["mouseleave", 27, 27, 1494913522059], ["mouseenter", 23, 28, 1494913522119],
                                           ["mouseleave", 3, 49, 1494913522146], ["mouseenter", 103, 46, 1494913530890],
                                           ["click", 107, 31, 1494913531242], ["mouseleave", 107, 35, 1494913533818],
                                           ["mouseenter", 107, 46, 1494913533997],
                                           ["mouseleave", 107, 49, 1494913535394]],
                                 "keyborad": [["keydown", 229, 1494913532682], ["keydown", 229, 1494913532739],
                                              ["keyup", 88, 1494913532762], ["keyup", 73, 1494913532818],
                                              ["keydown", 229, 1494913532842], ["keydown", 229, 1494913532923],
                                              ["keyup", 65, 1494913532954], ["keyup", 79, 1494913533049],
                                              ["keydown", 229, 1494913533082], ["keyup", 83, 1494913533178],
                                              ["keydown", 229, 1494913533250], ["keydown", 229, 1494913533354],
                                              ["keyup", 65, 1494913533418], ["keyup", 78, 1494913533466],
                                              ["keydown", 229, 1494913534844], ["keyup", 50, 1494913534946]]}}}
            # "captcha": super(Account, self)._get_captcha(_type="register")
        }
        print(data)
        r = super(Account, self)._execute(method="post", url=register_url, data=data,
                                          data_type=RequestDataType.FORM_DATA)
        print(r.status_code)
        print(r.text)

        sms_url = "https://www.zhihu.com/send_register_verification_code/sms?phone_num=%2B33752962193&captcha_source=register"

        r = self._session.get(sms_url, params={"phone_num": phone_num, "captcha_source": "register"})
        print(r.status_code)
        print(r.text)


        xx_url = "https://www.zhihu.com/register/phone_num"

        code = input("短信验证码")


        data['verification_code'] = code
        data.pop("captcha")
        r = self._execute(method="post", url=xx_url, data=data, data_type=RequestDataType.FORM_DATA)
        print(r.status_code)
        print(r.text)
        pass

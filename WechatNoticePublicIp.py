import json
import os.path
from platform import mac_ver, win32_ver, system
from sys import version_info as vi

import distro
from requests import get, __version__, post


class WechatNoticePublicIp():
    def __init__(self, token, fileName):
        self.__IpApiUrl = 'https://api.ipify.org/?format=json'
        self.__osVersionInfo = {
            'Linux': '%s' % (distro.id()),
            'Windows': '%s' % (win32_ver()[0]),
            'Darwin': '%s' % (mac_ver()[0]),
        }

        self.__userAgent = 'python-ipify/%s python/%s %s/%s' % (
            __version__,
            '%s.%s.%s' % (vi.major, vi.minor, vi.micro),
            system(),
            self.__osVersionInfo.get(system(), ''),
        )

        self.__ipFilePath = os.path.join(os.path.split(os.path.realpath(__file__))[0], fileName)
        self.__token = token  # 在 pushplus 官網查自己的 token
        self.__sendMessageURL = "https://www.pushplus.plus/send"

    def getFilePath(self):
        return self.__ipFilePath

    def getPublicIp(self):
        ip = get(self.__IpApiUrl, headers={'user-agent': self.__userAgent})
        print("public ip get : " + ip.text)
        return ip.text

    def isSameIp(self, ip):
        file = open(self.__ipFilePath, 'r')
        if ip == file.read():
            return True
        return False

    def updateIpText(self, ip):
        file = open(self.__ipFilePath, 'w')
        file.write(ip)
        file.close()

    def sendPushPlusMessage(self, title, content):
        data = {
            "token": self.__token,
            "title": title,  # 標題
            "content": content,  # 內容
            "template": "txt"  # 文本展示
        }
        req = post(url=self.__sendMessageURL, json=data)
        res = json.loads(req.text)
        print(res)
        if res['code'] == 200:
            print("send message success")
            return True
        else:
            return False

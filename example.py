import os
import sys

import WechatNoticePublicIp

if __name__ == '__main__':
    noticeCheckIp = WechatNoticePublicIp.WechatNoticePublicIp('your token', 'your file name')
    ipText = noticeCheckIp.getPublicIp()
    if ipText == "Bad Gateway":
        print("website error: Bad Gateway.")
        sys.exit()

    print(f"IP is: {ipText}.")
    sendTitle = "your title"
    # 若存在文件
    if os.path.exists(noticeCheckIp.getFilePath()):
        isSame = noticeCheckIp.isSameIp(ipText)
        # 若不同
        if not isSame:
            print("ip had changed : " + ipText)
            hasSendMessage = noticeCheckIp.sendPushPlusMessage(sendTitle, ipText)
            if hasSendMessage:
                noticeCheckIp.updateIpText(ipText)
    else:
        print("create file and write ip : " + ipText)
        hasSendMessage = noticeCheckIp.sendPushPlusMessage(sendTitle, ipText)
        if hasSendMessage:
            noticeCheckIp.updateIpText(ipText)

# WechatNoticePublicIp

check public ip, and send pushplus message to wechat if changed.

How to use
---------------

- 登入 pushplus 官網，在一對一推送頁面找到自己的微信 token
- 參考 example.py 使用
- 設定定時器，定時執行該腳本
- 建議使用 python 3.7.3 以上的版本

流程
---------------

- 若該腳本當前目錄下無文件時，執行腳本會自動創建文件
- 若文件內容與取得的 IP 不一致時，發送 pushplus 訊息並更新文件內容
- 若文件內容與取得的 IP 一致時，直接結束腳本

pushplus link
---------------
https://www.pushplus.plus/

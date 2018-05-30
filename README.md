# WechatWarning

有时候不在电脑旁也想知道程序运行状态，怎么办？使用微信测试公众号作为通知载体，方便快捷的获取通知消息。目前支持python3。


## 开通测试公众号
1. 扫码登陆[微信测试公众号后台](https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login)
2. 登陆后记录测试号信息==>appID,appsecret
3. 下拉后台页面，扫码关注测试号二维码，关注后刷新页面可以获取自己的微信号代码==>my_wxid
4. 创建模板消息 标题、内容自定义即可。记录模板ID ==> wx_model_id
5. 将上述记录的 ID 信息，替换掉 config.ini 文件中的对应内容。

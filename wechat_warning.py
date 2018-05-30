import requests
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('.\config.ini')
APPID = cfg.get('wechat_id','APPID')
APP_SECRET = cfg.get('wechat_id','APP_SECRET')
MY_WXID =cfg.get('wechat_id','MY_WXID')
WX_MODEL_ID = cfg.get('wechat_id','WX_MODEL_ID')

WX_MSG = {  
     "touser":MY_WXID,
    "template_id":WX_MODEL_ID,
    "url":"http://www.google.com",
    "topcolor":"#FF000",
    "data":{
        "type":{
                "value":"微信",# 对应模板中的{{type.DATA}}
                }
    }
}

def get_token():
    token_url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s"%(APPID,APP_SECRET)
    a = requests.post(token_url)
    # print(a.status)
    return(a.json()['access_token'])

def send_msg(access_token):
    msg_url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=" + access_token
    r = requests.post(msg_url,json=WX_MSG)
    print(r.content)

def get_informed():
    send_msg(get_token())

if __name__ == '__main__':
    get_informed()

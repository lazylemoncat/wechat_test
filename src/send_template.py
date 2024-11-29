import datetime
import requests
import logging
from pytz import timezone
from envConfig import envConfig

# 发送模板消息
def send_wechat_template_message(data: dict, url='') -> dict:
    access_token = get_access_token()
    post_url = (
        f"https://api.weixin.qq.com/cgi-bin/message/template/send"
        f"?access_token={access_token}"
    )
    payload = create_message_json(data, url)
    logging.info(f"Sending message: {payload}")
    logging.info(f"data is {data}")
    response = requests.post(post_url, json=payload)
    log_response(response)
    return response.json()

# 获取 access_token
def get_access_token() -> str:
    app_id, app_secret = envConfig.wechat_app_id, envConfig.wechat_app_secret
    url = (
        f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential"
        f"&appid={app_id}&secret={app_secret}"
    )
    response = requests.get(url)
    return response.json().get('access_token')

# 创建消息模板
def create_message_json(data: dict, post_url: str) -> dict:
    return {
        "touser": envConfig.wechat_touser,
        "template_id": envConfig.wechat_template_id,
        "url": post_url,
        "topcolor": "#FF0000",
        "data": data,
    }

# 记录响应日志
def log_response(response: requests.Response):
    date = datetime.datetime.now(timezone(envConfig.timezone)).strftime('%Y-%m-%d')
    logging.info(f"{date} status: {response.json()}")
import os
from dataclasses import dataclass 

@dataclass
class EnvConfig:
    # 微信测试号配置
    wechat_touser: str
    wechat_template_id: str
    wechat_app_id: str
    wechat_app_secret: str
    # 和风天气配置
    weather_city_code: str
    weather_city: str
    weather_api_key: str
    # 时区
    timezone: str = 'Asia/Shanghai'

envConfig = EnvConfig(
    wechat_touser=os.getenv('WECHAT_TOUSER', ''),
    wechat_template_id=os.getenv('WECHAT_TEMPLATE_ID', ''),
    wechat_app_id=os.getenv('WECHAT_APP_ID', ''),
    wechat_app_secret=os.getenv('WECHAT_APP_SECRET', ''),
    weather_city_code=os.getenv('WEATHER_CITY_CODE', ''),
    weather_city=os.getenv('WEATHER_CITY', ''),
    weather_api_key=os.getenv('WEATHER_API_KEY', ''),
    timezone=os.getenv('TIMEZONE', 'Asia/Shanghai') if os.getenv('TIMEZONE') != '' else 'Asia/Shanghai'
)
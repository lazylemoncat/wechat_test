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

def read_config_file(config_file: str | None) -> EnvConfig:
    '''读取配置文件'''
    import configparser
    configParser = configparser.ConfigParser()
    if config_file:
        configParser.read(config_file)
        return EnvConfig(
            wechat_touser=configParser.get('wechat', 'touser'),
            wechat_template_id=configParser.get('wechat', 'template_id'),
            wechat_app_id=configParser.get('wechat', 'app_id'),
            wechat_app_secret=configParser.get('wechat', 'app_secret'),
            weather_city_code=configParser.get('weather', 'city_code'),
            weather_city=configParser.get('weather', 'city'),
            weather_api_key=configParser.get('weather', 'api_key'),
            timezone=configParser.get('general', 'timezone')
        )
    else:
        raise ValueError(f"Failed to read config file: {config_file}")

def read_env_config() -> EnvConfig:
    '''读取环境变量'''
    return EnvConfig(
        wechat_touser=os.getenv('WECHAT_TOUSER', ''),
        wechat_template_id=os.getenv('WECHAT_TEMPLATE_ID', ''),
        wechat_app_id=os.getenv('WECHAT_APP_ID', ''),
        wechat_app_secret=os.getenv('WECHAT_APP_SECRET', ''),
        weather_city_code=os.getenv('WEATHER_CITY_CODE', ''),
        weather_city=os.getenv('WEATHER_CITY', ''),
        weather_api_key=os.getenv('WEATHER_API_KEY', ''),
        timezone=os.getenv('TIMEZONE', 'Asia/Shanghai')
    )

if os.getenv('CONFIG_FILE') is not None:
    envConfig = read_config_file(os.getenv('CONFIG_FILE'))
else: 
    envConfig = read_env_config()
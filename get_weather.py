import datetime
import logging
import requests
from pytz import timezone
from envConfig import envConfig

# 获取天气信息
def get_weather(city_code: str, api_key: str) -> dict:
    # 和风天气API
    url = (
        f"https://devapi.qweather.com/v7/weather/3d"
        f"?location={city_code}&key={api_key}"
    )
    response = requests.get(url)
    # 如果获取失败则抛出异常
    if response.status_code != 200:
        raise Exception(f"Failed to get weather data: {response.status_code}")
    # 如果获取失败则返回空字典
    try:
        weather = response.json()['daily'][0]
    except (KeyError, IndexError) as e:
        logging.error(f"Error fetching weather data: {e}")
        return {}
    res = {
        'temp_max': weather['tempMax'], # 最高温度
        'temp_min': weather['tempMin'], # 最低温度
        'text_day': weather['textDay'], # 白天天气
        'text_night': weather['textNight'], # 晚上天气
    }
    return res

# 获取天气信息字典
def get_weather_data() -> dict:
    # 读取环境变量中的天气信息
    city_code = envConfig.weather_city_code
    city = envConfig.weather_city
    api_key = envConfig.weather_api_key
    # 获取当前日期使用上海时区
    date = datetime.datetime.now(timezone('Asia/Shanghai')).strftime('%Y-%m-%d')
    # 获取天气信息
    weather = get_weather(city_code, api_key)

    # 设置模板消息数据
    data = {
        'date': {
            'value': date,
        },
        'city': {
            'value': city,
        },
        'temp_max': {
            'value': weather['temp_max'],
        },
        'temp_min': {
            'value': weather['temp_min'],
        },
        'text_day': {
            'value': weather['text_day'],
        },
        'text_night': {
            'value': weather['text_night'],
        },
    }
    return data

if __name__ == "__main__":
    print(get_weather_data())
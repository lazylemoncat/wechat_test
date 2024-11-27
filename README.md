[TOC]

# 项目介绍

本项目旨在使用微信测试公众号达到免费定时向自己发送数据的需求，比如推送当天的天气和微博热搜等。

测试公众号需要在微信公众平台进行申请，获取 appid 和 appsecret，同时需要配备部署该服务的url（必须是80端口），设置 token等，建立消息模板，获取模板 id。

天气服务使用的是和风天气 api 的免费接口，也可自行改为使用其他接口。

使用 docker 进行打包和部署，key 等信息使用环境变量存储。

也可自行简单重构一下达到给多名用户发送信息，或是重构为正式公众号亦或是短信发送服务。

# 功能

## 设置定时任务

如每天早上八点发送当天的该城市的天气。

## 获取天气信息

使用和风天气 api 免费接口，需要在该网站获取 api key, 找到当前所处的城市并获取 city code，city code 有接口可以获取的，但懒得写那个了（todo）

## （todo）获取微博热搜

用爬虫获取当天微博热搜前 20 条，以免落下时事热点。

也可自行修改方法获取想要的明星的动向或八卦。

# 使用说明

1.   下载项目文件到本地
2.   项目根目录下终端执行 `pip install -r requirements.txt` 安装依赖
3.   创建 docker container `docker build -t wechat_test:latest .` 其中镜像名和标签可以根据喜好定义
4.   `docker run -d -it --name wechat_test -e WECHAT_APP_ID=YOUR_APP_ID wechat_test:latest` 启动容器,记得将环境变量补全,每个环境变量用 -e 分隔, 如果需要新增环境变量在 envConfig 中定义

# 环境变量

+   WECHAT_TOUSER:  要发送的用户的 open_id
+   WECHAT_TEMPLATE_ID: 消息模板的模板 id
+   WECHAT_APP_ID: 微信公众号的 app_id
+   WECHAT_APP_SECRET: 微信公众号的 app_secret
+   WEATHER_CITY_CODE: 城市代码
+   WEATHER_CITY: 城市
+   WEATHER_API_KEY: 和风天气的 api_key
+   (非必须) TIMEZONE: 时区, 默认为亚洲上海 Asia/Shanghai 
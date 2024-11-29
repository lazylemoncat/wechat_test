import logging
from apscheduler.schedulers.blocking import BlockingScheduler
from pytz import timezone
from get_weather import get_weather_data
from send_template import send_wechat_template_message
from envConfig import envConfig

# 发送天气消息
def job_send_weather():
    send_wechat_template_message(get_weather_data(), "")

if __name__ == "__main__":
    # logging 加入时间戳并允许输出 INFO 级别的日志
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    # 设置定时任务调度器
    scheduler = BlockingScheduler(timezone=timezone(envConfig.timezone))
    
    # 添加每日 08:00 执行报天气任务
    scheduler.add_job(job_send_weather, 'cron', hour=8, minute=0)
    
    logging.info("Start")
    scheduler.start()
import logging
from apscheduler.schedulers.blocking import BlockingScheduler
from pytz import timezone
from get_weather import get_weather_data
from send_template import send_wechat_template_message
from envConfig import envConfig

if __name__ == "__main__":
    # 设置定时任务调度器
    scheduler = BlockingScheduler(timezone=timezone(envConfig.timezone))
    
    # 添加每日 08:00 执行报天气任务
    scheduler.add_job(
        send_wechat_template_message, 'cron', 
        args=[get_weather_data, ""], hour=8, minute=0
    )
    
    logging.info("Start")
    scheduler.start()
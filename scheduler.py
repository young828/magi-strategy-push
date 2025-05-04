import os
import requests
from apscheduler.schedulers.background import BackgroundScheduler

def send_telegram_message():
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    message = "[MAGI 전략 보고]\n자동 푸시 정상 작동 중입니다."

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    requests.post(url, data=payload)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_telegram_message, "interval", hours=1)
    scheduler.start()

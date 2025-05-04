# MAGI Telegram Push

Flask 서버 + APScheduler 기반 텔레그램 자동 푸시 시스템입니다.

## 환경변수 설정
- TELEGRAM_TOKEN
- CHAT_ID

## Render 배포 시
- Build Command: pip install -r requirements.txt
- Start Command: gunicorn app:app

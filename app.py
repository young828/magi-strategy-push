from flask import Flask
from scheduler import start_scheduler

app = Flask(__name__)

@app.route("/")
def home():
    return "MAGI Telegram Push Server is running."

if __name__ == "__main__":
    start_scheduler()
    app.run(host="0.0.0.0", port=5000)

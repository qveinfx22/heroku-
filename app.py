from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Heroku Test: SUCCESS!</h1><p>Мой первый сайт на Heroku работает.</p>"

if __name__ == "__main__":
    # Heroku сам назначает порт, берем его из переменных окружения
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

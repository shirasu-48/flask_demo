from flask import Flask, render_template
import time

app = Flask(__name__)


@app.route("/")
def index():
  today = time.strftime("%Y/%m/%d")
  now = time.strftime("%H:%M:%S")
  return render_template('index.html', today = today, now = now)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=80, debug=True)

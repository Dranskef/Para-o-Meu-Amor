from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    start_date = datetime(2025, 5, 13, 18, 18, 0)
    return render_template("index.html", start_date=start_date.isoformat())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

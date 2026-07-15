from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>Welcome to DevOps Monitoring Project</h1>
    <h2>{datetime.now()}</h2>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

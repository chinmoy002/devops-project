from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()

    return f"""
    <h1>DevOps Project</h1>
    <p>Application is running!</p>
    <p>Hostname: {hostname}</p>
    <p>Version: 1.2</p>
    """

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

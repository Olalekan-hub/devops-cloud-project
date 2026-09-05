from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from my DevOps project! This app is running inside Flask. My name is Yusuf Hammed and I am a Cloud Security Engineer"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
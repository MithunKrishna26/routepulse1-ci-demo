from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "RoutePulse Delivery Network service is running on 12144!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=12144)

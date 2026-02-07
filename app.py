from flask import Flask
from flask_cors import CORS
from routes.api import api_bp
from routes.register import register_bp
from routes.chat import chat_bp
# from routes.predict import predict_bp

app = Flask(__name__)
CORS(app)  # Allow frontend to talk to backend

app.register_blueprint(api_bp, url_prefix="/api")
app.register_blueprint(register_bp, url_prefix="/api")
app.register_blueprint(chat_bp, url_prefix="/api")
# app.register_blueprint(predict_bp, url_prefix="/api")


@app.route("/")
def home():
    return {"status": "KrishakSathi backend running"}

if __name__ == "__main__":
    app.run(debug=True)

import requests
from flask import Flask

def get_host_app():
    flask_app = Flask(__name__)
    
    @flask_app.get("/")
    def home():
        return "Service BBBBB container"
    
    @flask_app.get("/send_message")
    def send_message():
        try:
            response = requests.get("http://service_a:4444/secret_message/322")
            return f"Message sent to container Flask app, received response: {response.text}"
        except requests.exceptions.RequestException as e:
            return f"An error occurred: {e}"

    return flask_app


if __name__ == '__main__':
    flask_app = get_host_app()
    
    flask_app.run(
        debug=True,
        host='0.0.0.0', 
        port=8888,
    )

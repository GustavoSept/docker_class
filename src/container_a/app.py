from flask import Flask


def get_app():
    flask_app = Flask(__name__)
    
    @flask_app.get("/")
    def home():
        return "Hello world!"
    
    return flask_app
    
    
    
if __name__ == '__main__':
    flask_app = get_app()
    
    flask_app.run(
        debug=True,
        # host=...,
        # port=...,
    )
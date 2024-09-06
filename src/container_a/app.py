from flask import Flask


def get_app():
    flask_app = Flask(__name__)
    
    @flask_app.get("/")
    def home():
        return "Service AAAAA container"
    
    @flask_app.get("/secret_message/<int:id>")
    def secret_message(id):
        # Converting the number to binary and calculating its square
        binary_representation = bin(id)[2:]  # Convert to binary and strip '0b'
        square = id ** 2
        
        # Creating a fun response
        message = (
            f"Secret for number {id}: \n\n"
            f"Binary representation: {binary_representation} \n\n"
            f"Square of the number: {square} \n\n"
            f"Fun fact: {id} is {'even' if id % 2 == 0 else 'odd'}!"
        )
        
        return message

    return flask_app
    
    
    
if __name__ == '__main__':
    flask_app = get_app()
    
    flask_app.run(
        debug=True,
        host='0.0.0.0',
        port=4444,
    )
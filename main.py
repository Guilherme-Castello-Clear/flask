from flask import Flask
app = Flask(__name__)

test = {
    "test": "a"
}

@app.route('/')
def hello_world():
    global test
    return test

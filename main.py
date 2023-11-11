from flask import Flask
app = Flask(__name__)

test = {
    "test": "a"
}

@app.route('/')
def hello_world():
    return "Hellow World"

@app.route('/bye')
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()

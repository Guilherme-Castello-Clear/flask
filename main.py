from flask import Flask
app = Flask(__name__)

test = {
    "test": "a"
}

@app.route('/')
def hello_world():
    return "Hellow World"

@app.route('/username/<name>/<int:age>')
def greet(name, age):
    return f"Hello {name}, u are {age}y old"


if __name__ == "__main__":
    app.run(debug=True)

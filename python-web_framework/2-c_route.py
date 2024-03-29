"""
this module is for flask project
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello HBNB!'

@app.route('/hbnb')
def two():
    return 'HBNB'

@app.route('/c/<text>')
def hbnb(text):
    formated_text = text.replace('_', ' ')
    return f'C {formated_text}'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")

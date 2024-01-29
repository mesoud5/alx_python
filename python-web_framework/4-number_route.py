"""
this module is for flask project
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    return 'HBNB'

@app.route('/c/<text>')
def c(text):
    formated_text = text.replace('_', ' ')
    return f'C {formated_text}'

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    formatted_text = text.replace('_', ' ')
    return f'Python {formatted_text}'

@app.route('/number/<n>', strict_slashes=False)
def number(n):
    if n.isdigit():
        return f'{n} is a number'
    else:
        return f'{n} is not a number'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")

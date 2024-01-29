"""
this module is for flask project
"""
from flask import Flask, abort, render_template

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
        abort(404)

@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    if n.isdigit():
        return render_template('5-number.html', n=n)
    else:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")

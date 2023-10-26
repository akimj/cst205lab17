from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def hello():
   return '<h1>Aidan Kim: NASA, Sydney S: ASAP<h/1>'


@app.route('/AidanNASA')
def t_test():
    return render_template('index.html')


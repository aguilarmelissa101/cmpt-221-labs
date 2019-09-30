##Melissa Aguilar
##Users are able to input anything at the end of the URL by inputting /user/name
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/#portfolio')
def portfolio():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()


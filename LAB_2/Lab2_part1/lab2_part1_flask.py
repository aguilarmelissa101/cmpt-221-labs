##Melissa Aguilar
##Users are able to input anything at the end of the URL by inputting /user/name
from flask import Flask
app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return """
    <h1>Hello World!</h1>
    <p>If you want a custom message with your name to appear, go to the URL and input '/name/yourname'</p>
    """

@app.route('/name/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/about')
def about_page():
    return """
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title>About Flask</title>
      </head>
      <body>
        
        <ul><li>Who am I?</li></ul>
        
        <h1> About Flask </h1>
        <p> Flask is a micro web framework written in Python.</p>
        <p> Applications that use the Flask framework include Pinterest,
          LinkedIn, and the community web page for Flask itself.</p>
      </body>
    </html>

    """

if __name__ == '__main__':
    app.run()


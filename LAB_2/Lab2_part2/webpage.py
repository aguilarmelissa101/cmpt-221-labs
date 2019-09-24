##Melissa Aguilar
##Users are able to input anything at the end of the URL by inputting /user/name
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home')
@app.route('/')
def index():
    return render_template("home_page.html")

@app.route('/resume')
def resume():
    return render_template("resume_page.html")

if __name__ == '__main__':
    app.run()


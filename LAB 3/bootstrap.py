##Melissa Aguilar
##Users are able to input anything at the end of the URL by inputting /user/name
from flask import Flask, render_template

# Declare the Flask Object
app = Flask(__name__)


# Adding dynamic route with templates
@app.route("/")
def index():
    return render_template("index.html"), 200


# Run Flask Programmatically
if __name__ == "__main__":
    # Set Debug to true, set host IP to localhost, and set port to 80
    app.run(debug=True, host="127.0.0.1")




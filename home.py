from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route('/icad')
def hello_icad():
    return "HELLO ICAD"

if __name__ == '__main__':
    app.run(port=5000, debug=True)
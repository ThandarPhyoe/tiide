from flask import Flask

app = Flask(__name__)

@app.route("/")
def Thandar():
    return "Hello World"

@app.route("/Thandar")
def tiide():
    return "Welcome to ThandarPhyoe"

from flask import Flask, request, jsonify,render_template

app = Flask(__name__)

@app.route("/", methods = ["POST"])
def pwskills():
    return "Welcome to Data science Masters class!"

@app.route("/mentor", methods = ["POST"])
def mentor():
    return "Hello there, I am Sudhanshu Kumar your mentor for Data Science Masters Class."

@app.route("/disciple", methods = ["POST"])
def disciple():
    return "Hello sir, I am Rushikesh Jadhav your disciple for Data Science Masters Class."

if __name__=="__main__":
    app.run(host="0.0.0.0")
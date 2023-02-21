from flask import Flask,url_for,redirect

app = Flask(__name__)

@app.route("/")
def pwskills():
    return "Welcome to Data science Masters class!"

@app.route("/mentor")
def mentor():
    return "Hello there, I am Sudhanshu Kumar your mentor for Data Science Masters Class."

@app.route("/disciple")
def disciple():
    return "Hello sir, I am Rushikesh Jadhav your disciple for Data Science Masters Class."

@app.route("/user")
def user():
    if name == "/":
        return (redirect(url_for("pwskills")))
    elif name == "mentor":
        return (redirect(url_for("mentor")))
    else :
        return (redirect(url_for("disciple")))

if __name__=="__main__":
    app.run(host="0.0.0.0")
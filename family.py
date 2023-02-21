from flask import Flask

app = Flask(__name__)

@app.route("/")

def family():
    print("My mother name is Chhaya and she is 55 years old")
    

if __name__=="__main__":
    app.run(host="0.0.0.0")

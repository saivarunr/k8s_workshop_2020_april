from flask import Flask

app = Flask(__name__)

@app.route("/index")
def index_route():
    return "Hello this is index route"

@app.route("/wish-a-friend/<name>")
def wish_a_friend(name):
    return "Hello "+name+" How are you?"

@app.route("/division-problem/<num_one>/<num_two>")
def division_problem(num_one,num_two):
    try:
        return str(int(num_one)/int(num_two)+1)
    except Exception as e:
        return str(e)

app.run(port=5000,host='0.0.0.0')
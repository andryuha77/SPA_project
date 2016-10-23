# Originally adapted from:
#   http://flask.pocoo.org/

import flask as fl
import itertools as it
app = fl.Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file('index.html')

@app.route("/perms", methods=["GET", "POST"])
def perms():
	perms = [''.join(p) for p in it.permutations(fl.request.values["userinput"])]
	return '\n'.join(perms)

#    return "Hello " + fl.request.form["name"] + "!!!"
#    return app.send_static_file('index.html', **locals())

if __name__ == "__main__":
    app.run()


    
#@app.route("/BMI")
#def BMICalculate():
#    return app.send_static_file('BMI.js')
#
#@app.route("/name", methods=["GET", "POST"])
#def name():
#    return "BMI : " + fl.request.form["BMI"] + "!"	
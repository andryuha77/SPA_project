import flask as fl
app = fl.Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file('index.html')
	
@app.route("/name", methods=["GET", "POST"])
def name():
    return "Hello " + fl.request.form["name"] + "!"	
	
if __name__ == "__main__":
    app.run()
    
#@app.route("/BMI")
#def BMICalculate():
#    return app.send_static_file('BMI.js')
#
#@app.route("/name", methods=["GET", "POST"])
#def name():
#    return "BMI : " + fl.request.form["BMI"] + "!"	
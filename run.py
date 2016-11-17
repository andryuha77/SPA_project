# Originally adapted from:
# http://flask.pocoo.org/
# https://github.com/mjhea0/thinkful-mentor/tree/master/python/jinja/flask_example

from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """convert a datetime to a different format."""
    return value.strftime(format)

app.jinja_env.filters['datetimefilter'] = datetimefilter

@app.route("/", methods=['GET', 'POST'])
def template_test():
    return render_template('template.html', current_time=datetime.datetime.now())

@app.route("/result", methods=['GET', 'POST'])
def result():
    return render_template('result.html',title="Result", current_time=datetime.datetime.now())

@app.route("/about")
def about():
    return render_template('template.html', my_string="Bar", 
    title="About", current_time=datetime.datetime.now())


#include debuger
if __name__ == '__main__':
    app.run(debug=True)

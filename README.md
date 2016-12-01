# SPA_project
Single-page web application using the Flask framework for Data Representation project
The module is taught to undergraduate students at [GMIT](http://www.gmit.ie) in the Department of Computer Science and Applied Physics.
The lecturer is [Ian McLoughlin](https://ianmcloughlin.github.io).

# Web Application Project
#### Data Representation and Querying Project 2016

### Project Overview
I have created a Single-Page Web Application (SPA) that lets users calculate BMI.
This application was selected after some deliberation.
Initially, I considered three different applications:

1. A [Power supply calculator](http://outervision.com/power-supply-calculator) alternative.
2. A [BMI calculator](http://www.bmicalculator.ie/) alternative.
3. A [Yelp](https://www.yelp.ie/) alternative.

I chose BMI calculator after some consideration, as I were more interested in the idea.

The project was guided by the following excerpt from the project instructions:
>You are required to develop a single-page web application(SPA) written in the programming language Python using the Flask framework. 
You must devise an idea for a web application, write the software, write documentation explaining how the application works, and write a short user guide for it.


### How to run the application
The application is written using the [Flask](http://flask.pocoo.org/) library in [Python 3](https://www.python.org).
Both must be installed to run the project.

Jinja2 was used for html inheritance.

Once these prerequisites are installed, the application can be run locally:
```bash
$ python run.py
```
Once the application is running, it can be accessed by pointing your browser at http://127.0.0.1:5000/ .

### Architecture
This web application runs in [Python 3](https://www.python.org) using the [Flask](http://flask.pocoo.org/) web micro-framework and uses SQLite as a database.
Python 3 and Flask were requirements for the project.
I chose SQLite as it is easy to use and does not require much setup to get the web application up and running.

### Reference
BMI.js file Adapted from: http://blog.excelstrategiesllc.com/2014/11/18/coding-your-first-javascript-bmi-calculator
App Template Adapted from: https://github.com/mjhea0/thinkful-mentor/tree/master/python/jinja/flask_example

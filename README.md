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

1. A [ToDoListMe](http://todolistme.net/) alternative.
2. A [Pastebin](http://pastebin.com/) alternative.
3. A [Yelp](https://www.yelp.ie/) alternative.

In our early discussions, we excluded option 3 as it would be too difficult to construct in the short time we had to complete the project.
That left option 1 and 2.
We chose 2 after some consideration, as we were more interested in the idea.

The project was guided by the following excerpt from the project instructions:
>You are required to develop a single-page web application(SPA) written in the programming language Python using the Flask framework. 
You must devise an idea for a web application, write the software, write documentation explaining how the application works, and write a short user guide for it.


### How to run the application
The application is written using the [Flask](http://flask.pocoo.org/) library in [Python 3](https://www.python.org).
Both must be installed to run the project.

We use the [sqlite3](https://docs.python.org/2/library/sqlite3.html) package for persistence in the application.
This must also be installed.
However, no further configuration our setup is required, as the database is fully contained in the db directory in this repository.

Once these prerequisites are installed, the application can be run locally:
```bash
$ python h.py
```
Once the application is running, it can be accessed by pointing your browser at http://127.0.0.1:5000/ .

### Architecture
This web application runs in [Python 3](https://www.python.org) using the [Flask](http://flask.pocoo.org/) web micro-framework and uses SQLite as a database.
Python 3 and Flask were requirements for the project, but SQLite was selected by the team.
We chose SQLite as it is easy to use and does not require much setup to get the web application up and running.



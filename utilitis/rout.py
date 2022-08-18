from datetime import datetime

from flask import Flask, render_template, request, redirect
from models import Employees
from app import app, db
from helps.help import *


@app.route('/', methods=['Get'])
def add_user():
    return render_template('structure.html')


@app.route('/show', methods=['Post'])
def shows():
    form = request.form
    a = Employees(employee_id=form["employee_id"], first_name=form["first_name"], last_name=form["last_name"],
                  Email=form["Email"], phone_number=form["phone_number"],
                  hire_date=form["hire_date"],
                  job_id=form["job_id"], salary=form["salary"], commission_pct=form["commission_pct"],
                  manager_id=form["manager_id"], department_id=form["department_id"])
    db.session.add(a)
    db.session.commit()
    return a.serialize


@app.route('/all', methods=['get'])
def show_all():
    e = Employees.query.all()
    return convert_all(e)


@app.route('/')
def index():
    return "sadasdasdasds"


@app.route('/search')
def search():
    return render_template("search.html")


@app.route('/employee', methods=['get'])
def employee_id():
    return render_template('employee_id.html')


@app.route('/search/employee_id', methods=['post'])
def search_employee_id():
    form = request.form
    i = 0
    if Employees.query.filter_by(employee_id=form['employee_id']):
        i += 1
    if i > 0:
        d = Employees.query.filter_by(employee_id=form['employee_id']).first()
        return d.serialize
    elif i == 0:
        "<h1>incorrect data</h1>"


@app.route('/fname', methods=['get'])
def fnmae():
    return render_template('/fname.html')


@app.route('/fname/search', methods=['post'])
def fname_search():
    form = request.form
    i = 0
    list = []
    a = []
    if Employees.query.filter_by(first_name=form['first_name']):
        i = i + 1

    if i > 0:
        list = Employees.query.all()
        for i in list:
            if i.fname == form['first_name']:
                a.append(i.serialize)
        return a
    elif i == 0:
        return "incorect data"


@app.route('/hire', methods=['get'])
def hire_search():
    return render_template('hire_date.html')


@app.route('/search/hire', methods=['post'])
def hire_s():
    form = request.form
    i = 0
    list = []
    a = []
    if Employees.query.filter_by(hire_date=form['hire_date']):
        i = i + 1
    if i > 0:
        list = Employees.query.all()
        for i in list:
            if str(i.hire) == str(form['hire_date'])+" 00:00:00":
                a.append(i.serialize)
        return a
    elif i == 0:
        return "incorect data"

@app.route('/email',methods=['get'])
def email_s():
    return render_template("Email_search.html")

@app.route("/search/email",methods=['post'])
def search_email():
    form = request.form
    i = 0
    if Employees.query.filter_by(Email=form['Email']):
        i += 1
    if i > 0:
        d = Employees.query.filter_by(Email=form['Email']).first()
        return d.serialize
    elif i == 0:
        "<h1>incorrect data</h1>"

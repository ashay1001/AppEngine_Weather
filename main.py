#!/usr/bin/env python
from datetime import datetime
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from weather import query_api

app = Flask(__name__)

@app.route('/')
@app.route("/index")
def index():
    return render_template(
        'weather.html',
        data=[{'name':'Mumbai'}, {'name':'Delhi'}, {'name':'Bangalore'},
        {'name':'Pune'}, {'name':'Hyderabad'}, {'name':'Chennai'},
        {'name':'Kolkata'}, {'name':'Ahmedabad'}, {'name':'Lucknow'}, 
        {'name':'Visakhapatnam'}])

@app.route("/result" , methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select)
    pp(resp)
    if resp:
       data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    today = datetime.today()
    date = today.strftime("%d %B %Y")
    return render_template(
        'result.html',
        date=date,
        data=data,
        error=error,
        )
if __name__=='__main__':
    app.run(debug=True)
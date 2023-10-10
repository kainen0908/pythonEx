# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:31:26 2023

@author: kainen
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello World!</h1>'

# 이 py파일이 있는 곳으로 cd
# set FLASK_APP=flask_basic.py
# flask run 
# http://127.0.0.1:5000
# 으로 접속하면 hello World 출력
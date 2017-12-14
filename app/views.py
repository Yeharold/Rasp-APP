#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-12 16:24:26
# @Author  : YeHarold (1174484433@qq.com)
# @Link    : http://example.org


from flask import render_template, request
from app import *
from app.controler import *
import multiprocessing
import os


# ----------------------------
global PID
p = multiprocessing.Process(target=startGet)
p.start()
PID = str(p.pid)
os.system('kill -STOP ' + PID)
# -----------------------------------------


@app.route('/on', methods=['POST', 'GET'])
def on():

    if request.method == 'POST':
        onLight()

    return render_template('raspberry.html')


@app.route('/off', methods=['POST', 'GET'])
def off():

    if request.method == 'POST':
        offLigth()

    return render_template('raspberry.html')


@app.route('/start', methods=['POST', 'GET'])
def start():

    global PID
    if request.method == 'POST':

        os.system("kill -CONT " + PID)

    return render_template('raspberry.html')


@app.route('/stop', methods=['POST', 'GET'])
def end():

    global PID

    if request.method == 'POST':

        os.system('kill -STOP ' + PID)

    return render_template('raspberry.html')

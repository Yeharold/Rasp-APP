#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-12 16:32:53
# @Author  : YeHarold (1174484433@qq.com)
# @Link    : http://example.org


from app.sensor import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)
# --------------------------------


def onLight():
    '''打开灯
    '''
    
    GPIO.output(22, GPIO.HIGH)
    # pass


def offLigth():
    '''关闭灯
    '''

    GPIO.output(22, GPIO.LOW)
    # pass


def startGet():
    '''开始获取数据
    '''
    while True:
        
        getTemperature()


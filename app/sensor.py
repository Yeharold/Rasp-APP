#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-12 16:48:05
# @Author  : YeHarold (1174484433@qq.com)
# @Link    : http://example.org

import time as t
import os
from app.models import *


# def getTemperature():
#     '''传感器获取温度
#     '''
#     # 温度传感器芯片DS18B20

#     os.system('sudo modprobe w1-gpio')
#     os.system('sudo modprobe w1-therm')

#     tfile = open("/sys/bus/w1/devices/28-03170371d7ff/w1_slave", 'rb')
#     text = tfile.read()
#     tfile.close()
#     secondline = text.split("\n")[1]
#     temperaturedata = secondline.split(" ")[9]
#     temperature = float(temperaturedata[2:])

#     tempData = temperature / 1000.0
#     timeData = t.ctime()

#     putData(tempData, timeData)

#     t.sleep(5)





# ----------------test------------------------

def getTemperature():


	tempData = 20.0
	timeData = t.ctime()

	putData(tempData,timeData)

	t.sleep(3)

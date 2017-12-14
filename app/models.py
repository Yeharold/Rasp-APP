#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-12 17:03:10
# @Author  : YeHarold (1174484433@qq.com)
# @Link    : http://example.org

import sqlite3 as db 


conn = db.connect('app/database/app.db',check_same_thread = False)
c = conn.cursor()



def putData(tempData,timeData):

	''' 往数据库中放入数据
		tempData	是温度数据
		timeData	是采集温度时间
	'''

	sql = 'insert into data (tempData,timeData) values("%s","%s")'%(tempData,timeData)

	c.execute(sql)
	conn.commit()

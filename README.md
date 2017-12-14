### @Date    : 2017-12-14 14:58:35
### @Author  : YeHarold (1174484433@qq.com)
### @Link    : https://github.com/Yeharold

### 第一步:连接树莓派   ssh或putty

----------------------------------------------
### 第二步:把APP拷贝到树莓派(注意替换成自己树莓派的用户名和IP)
	执行:
	 	scp -r Rasp-APP pi@192.168.0.103:

-------------------------------------------
### 第三步:在树莓派中安装nginx服务器
	执行:
		sudo apt-get install nginx

------------------------------------------------
### 第四步:在树莓派中安装flask和gunicorn
	查看有没有安装pip执行:
					  pip -v

	如果没有pip需要执行: sudo apt-get install python-pip
	如果已安装直接执行:
					sudo pip install flask
							
					sudo pip install gunicorn

	如果没报错就OK(如果提示pip版本问题不用care)

-------------------------------------------------

### 第五步:配置nginx服务器
	执行:
		cd /etc/nginx/site-avalidable/
		sudo rm default
		sudo nano default 
		把下面配置粘贴进去,然后ctrl+o,ctrl+x
	
server {
    listen 80;
    location / {
        proxy_pass http://127.0.0.1:8080; 
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

--------------------------------------------------

### 第六步:重启nginx服务器
	执行:	
		sudo service nginx restart

--------------------------------------------------
### 第七步:启动APP
	执行:
		cd ~
		cd Rasp-APP
		gunicorn -w 1 -b 127.0.0.1:8080 run:app

	gunicorn运行开始后就不能在输入

-------------------------------------------------
### 第八步:接灯(程序中设置为GPIO.setmode(GPIO.BOARD))
		led正极接	树莓派外排第11针	(pin22)
		led负极接	树莓派外排第7 针 	(pin14)

-------------------------------------------------
### 第九步:局域网计算机打开浏览器
		输入树莓派ip(自己树莓派ip)如:

					192.168.0.103/on
		即可看到控制界面
		
-------------------------------------------------
## 其他说明:
	传感器采集数据部分是模拟采集
	代码还行进一步完善

	停此gunicorn执行:		killall gunicorn

	查看是否采集数据:		
				cd ~
				cd Rasp-APP/app/database
				sqlite3 data.db
				select * from data;

				看看采集时间timedata字段



		
		
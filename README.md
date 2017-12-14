### @Date    : 2017-12-14 14:58:35
### @Author  : YeHarold (1174484433@qq.com)
### @Link    : https://github.com/Yeharold

### 第一步:链接树莓派   ssh或putty

----------------------------------------------
### 第二步:把APP拷贝到树莓派(注意替换成自己树莓派的用户名和IP)
	 执行:
	 	 scp -r APP pi@192.168.0.103:

-------------------------------------------
### 第三步:在树莓派中安装nginx服务器
	执行:
		sudo apt-get install nginx

------------------------------------------------
### 第四步:在树莓派中安装flask和gunicorn
	执行:
		sudo pip install gunicorn
				
		sudo pip install flask

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
			cd APP
			gunicorn -w 1 -b 127.0.0.1:8080 run:app

-------------------------------------------------
### 第八步:接灯
	led正极接		pin22
	led负极接		pin7
		
		
## 创建blog 项目
### 环境
> python2 -m pip install --upgrade pip  
> pip install virtualenv virtualenvwrapper  
> virtualenv django  
> active.bat / deactive.bat  
> pip install django    
> pip freeze >requirements.txt 

### 构建简单blog 项目(开启虚拟环境)
1. `django-admin startproject blog .`  
    
		$ tree
		|-- manage.py
		|-- blog
			 |-- settings.py
			 |-- urls.py
			 |-- wsgi.py
			 |__ __init__.py

	| 文件        | 说明                                  |
	| :---------- | :------------------------------------ |
	| manage.py   | 项目管理cli工具(应用创建，数据库迁移) |
	| settings.py | 项目配置文件(数据库参数               |
	| urls.py     | URL路径映射配置                       |
	| wsgi        | 定义wsgi接口信息                      |
		
2. 配置数据库  
   安装: `pip install mysqlclient`  
   
			DATABASES = {
				'default': {
				'ENGINE': 'django.db.backends.mysql',
				'NAME': 'blog',
				'USER': 'anyue',
				'PASSWORD': 'anyue',
				'HOST': '192.168.0.109',
				'PORT': '3306',
			}
		}

3. 创建应用，从模型定义生成数据库的表 
  
   		python manage.py startapp user
		python manage.py makemigrations		# 生成迁移文件
		python manage.py migrate			# 迁移数据

4. 创建后台管理员

		python manage.py createsuperuser
		python manage.py runserver

5. 注册应用模块(admin.py)

		from django.contrib import admin
		from .models import User

		# Register your models here.
		admin.site.register(User)		# 注册

### 

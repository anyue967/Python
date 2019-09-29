from flask import Flask # 导入Flask框架
from flask import render_template

app = Flask(__name__) # 创建Flask应用实例

@app.route('/', methods=['GET', 'POST']) # 定义路由(找路径)及视图函数
def hello_world():
	return 'Hello Flask!'

@app.route('/orders/<int:order_id>')
def get_order_id(order_id):
	print type(order_id)
	return 'order_id %s' % order_id

print ("----------------------------------------------")

@app.route('/template') # 定义路由(找路径)及视图函数
def template():
	url = 'www.baidu.com'
	myList = [1, 3, 5, 7, 9]
	myDict = {
		'name': '百度',
		'url': 'www.baidu.com'
	}
	myInt = 40
	return render_template(
		'template.html', 
		url=url, 
		myList=myList, 
		myDict=myDict,
		myInt=myInt
	)

'''
{#template#}
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Flask<title>
</head>
<body>
	{{ url }} <br>
	{{ myList }} <br>
	{{ myList[2] }} <br> 	{#myList.2#}
	{{ myDict.url }} <br>	{#myDict['url']#}
	<hr>
	{#for循环使用#}
	{% for num in myList %}
		{% if num > 3 %}
			{{ num }} <br>
		{% endif %}
	{% endfor %}
	<hr>
	{#过滤器#}
	{{ url | upper }} <br>
	{{ url | reverse }} <br>
	{#过滤器链式调用#}
	{{ url | upper | reverse }}
</body>
</html>
'''

if __name__ == "__main__":
	app.run()
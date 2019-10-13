from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringFiled, PasswordField, SelectField, SubmitFiled
from wtforms.validators import DataRequired, EqualTo

# 解决编码
import sys
reload(sys)
sys.sedefaultencoding('utf-8')

app = Flask(__name__)
'''
给模板传递消息
flash需要对内容加密，因此需要设置secret_key，做加密消息的混淆
'''
app.secret_key = 'anyue'

# 使用WTF实现表单，自定义表单类
class LoginForm(FlaskForm):
	username = StringFiled(u'用户名:', validators=[DataRequired()])
	password = PasswordField(u'密码:', validators=[DataRequired()])
	password2 = PasswordField(u'确认密码:', validators=[DataRequired(), EqualTo('password', '密码填入不一致')])
	submit = SubmitFiled('提交')

@app.route('/form', method=['GET', 'POST'])
def login():
	login_form = LoginForm()
	if request.method == 'POST'
		username = request.form.get('username')
		password = request.form.get('password')
		password2 = request.form.get('password2')
		if login_form.validata_on_submit():
			print username, password
			return 'success'
		else:
			flash('error')

	return render_template('index.html', form=login_form)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		# return 'POST'
		username = request.form.get('username')
		password = request.form.get('password')
		password2 = request.form.get('password2')
		# print(password)
		if not all([username, password, password2]):
			# print '参数不完整'
			flash(u'参数不完整')
		elif password != password2:
			# print '密码不一致'
			flash(u'密码不一致')
		else:
			return success
	return render_template('index.html')

if __name__ == '__main':
	app.run(debua=True)

'''
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<title>Test</title>
</head>
<body>
<form method="post">
	<label>
		用户名:<input type="text" name="username"><br>
		密码:<input type="password" name="password"><br>
		确认密码:<input type="password" name="password2"><br>
		<input type="submit" value="提交"><br>
		{% for message in get_flashed_meassages() %}
			{{ message }}
		{% endfor %}
	</label>
</form>
<hr>
<form method="post">
	{{ form.csrf_token() }}
	{{ form.username.label }}{{ form.username }} <br>
	{{ form.password.label }}{{ form.password }} <br>
	{{ form.password2.label }}{{ form.password2 }} <br>
	{{ form.submit.label }}
</form>
</body>
</html>
'''
# pip install flask-sqlalchemy
# pip install flask-mysqldb

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Role(db.Model):
	# 定义表名
	__tablename__ = 'roles'
	# 定义字段
	id = db.Column(db.Interger, primary_key=True)
	name = db.Column(db.String(16), unique=True)
	# 和User模型关联，增加了user属性
	user = db.relationship('User', backref='role')

	def __repr__(self):
		return '<Role: %s %s>' % (self.name, self.id)

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Interger, primary_key=True)
	name = db.Column(db.String(16), unique=True)
	role_id = db.Column(db.Interger, db.ForeignKey('roles.id'))
	# 

@app.route('/')
def index():
	return ''

if __name__ = '__main__':
	db.drop_all()
	db.create_all()

	ro1 = Role(name='admin')
	db.session.add(ro1)
	db.session.commit()

	ro2 = Role(name='user')
	db.session.add(ro2)
	db.session.commit()
	# 生成数据
	us1 = User(name='wang', email='wang@163.com', password='wang', role_id='ro1_id')
	us2 = User(name='li', email='li@163.com', password='li', role_id='ro2_id')
	us3 = User(name='zhao', email='zhao@163.com', password='zhao', role_id='ro2_id')
	us4 = User(name='zhang', email='zhang@126.com', password='zhang', role_id='ro1_id')
	# 提交数据给用户会话
	db.session.add_all([us1, us2, us3, us4])
	# 提交会话
	db.session.commit()
	app.run(debug=True)
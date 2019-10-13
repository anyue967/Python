from flask import Flask, render_template, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataReuqired

'''
1.配置数据库
2.添加模型(书 作者): 继承db.Model  表名__tablename__  关系引用db.relationship
3.添加数据
4.使用模板显示数据库查询数据
5.使用WTF显示表单
6.实现相关的增删逻辑
'''

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1/flask_books'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'anyue'

# 创建数据库对象
db = SQLAlchemy(app)

# 作者模型
class Author(db.Model):
	__tablename__ = 'authors'
	id = db.Column(db.Integer, Primary_key=True)
	name = db.Column(db.String(16), unique=True)
	books = db.relationship('Book', backref='author')

	def __repr__(self):
		return 'Author: %s' % self.name

# 书籍模型
class Book(db.Model):
	__tablename__ = 'books'
	id = db.Column(db.Integer, Primary_key=True)
	name = db.Column(db.Integer, db.ForeignKey('authors.id'))

	def __repr__(self):
		return 'Book: %s %s' % (self.name, self.author_id)

# 自定义表单类
class AuthorForm(FlaskForm):
	author = StringField('作者：', validators=[DataReuqired()])
	book = StringField('书籍：', validators=[DataReuqired()])
	submit = StringField('提交')

# 删除书籍
@app.route('/delete_book/<book_id>')
def delete_book(book_id):
	book = Book.query.get(book_id)
	if book:
		try:
			db.session.delete(book)
			db.session.commit()
		except Exception as e: 
			print e
			flash('删除书籍出错')
			db.session.rollback()
	else:
		flash('书籍找不到')
	print('index')
	return redirect(url_for('index'))

# 删除作者
@app.route('/delete_author/<author_id>')
def delete_author(author_id):
	author = Author.query.get(author_id)
	if author:
		try:
			Book.query.filter_by(author_id=author_id).delete()
			db.session.delete(author)
			db.session.commit()
		except Exception as e:
			print e
			flash('删除作者失败')
			db.session.rollback()
	else:
		flash('作者没有找到')

	return redirect(url_for('index'))

@app.route('/', method=['GET', 'POST'])
def index():
	# 创建自定义表单类
	author_form = AuthorForm()
	# 调用WTF函数实现验证
	if author_form.validate_on_submit():
		# 验证通过获取数据
		author_name = author_form.author.data
		author_book = author_form.book.data
		# 判断作者是否存在
		author = Author.query.filter_by(name=author_name).first()
		# 存在
		if author:
			book = Book.query.filter_by(name=book_name).first()
			if book:
				flash('存在同名书籍')
			else:
				try:
					new_book =Book(name=book_name, author_id=author.id)
					db.session.add(new_book)
					db.session.commit()
				except Exception as e:
					print e
					flash('添加书籍失败')
					db.session.rollback()
		else:
			# 不存在
			try:
				new_author = Author(name='author_name')
				db.session.add(new_author)
				db.session.commit()

				new_book = Book(name=book_name, author_id=new_author.id)
				db.session.add(new_book)
				db.session.commit()
			except Exception as e:
				print e
				flash('添加作者失败')
				db.session.rollback()
	else:
		if request.method == 'POST':
			flash('参数不全')

	# 查询所有作者信息，传递给模板
	authers = Author.query.all()
	return render_template('05-books.html', authors=authers)

if __name__ == '__main__':
	db.drop_all()
	db.create_all()
	# 生成数据
	au1 = Author(name='老王')
	au2 = Author(name='老惠')
	au3 = Author(name='老刘')
	# 把数据提交给用户会话
	db.session.add_all([au1, au2, au3])
	# 提交会话
	db.session.commit()

	bk1 = Book(name='book1', author_id=au1.id)
	bk2 = Book(name='book2', author_id=au2.id)
	bk3 = Book(name='book3', author_id=au3.id)
	bk4 = Book(name='book4', author_id=au4.id)
	bk5 = Book(name='book5', author_id=au5.id)
	# 数据交给用户会话
	db.session.add_all([bk1, bk2,bk3,bk4,bk5])
	# 提交会话
	db.session.commit()

	app.run(debug=True)
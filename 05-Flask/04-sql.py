from 03-flask import *
'''
# 添加
role = Role(name='admin')
db.session.add(role)
db.session.commit()
user = User(name='anyue', role_id=role.id)
db.session.add(user)
db.session.commit()

# 修改
user.name = '967'
db.session.commit()

# 删除
db.session.delete(user)
db.session.commit()

# 实现关系引用查询
role.users
[<User: zs 1 None None>, <User: ls 2 None None>]

user2.role.name
u'admin'

# 查询
User.query.all()
User.query.count()
User.query.first()
User.query.get(id)
'''
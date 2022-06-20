from App import App
import datetime
from sqlalchemy import text


db = App.get_db()


class Department(db.Model):
    __tablename__ = "department_table"
    department_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    department_code = db.Column(db.String(32), nullable=False, unique=True)
    department_name = db.Column(db.String(10), nullable=False, unique=True)


class User(db.Model):
    __tablename__ = "user_table"
    user_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    username = db.Column(db.String(12), unique=True, nullable=False)
    initialized = db.Column(db.Boolean, server_default=text('False'))
    chinese_name = db.Column(db.String(12), unique=True, nullable=False)
    # default password is "123456"
    password = db.Column(db.String(32), nullable=False, default='e10adc3949ba59abbe56e057f20f883e')
    department_code = db.Column(db.String(32), db.ForeignKey('department_table.department_code'))
    in_company = db.Column(db.Boolean, server_default=text('True'))

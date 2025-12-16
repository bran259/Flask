from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

#define model class => inheriting from db.Model
class User(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

class Post(db.Model):
    __tablename__= 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String(250))



    #create table users(id INTEGER PRIMARY KEY, username TEXT,email TEXT, password TEXT)
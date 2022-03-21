from app.db import db
from sqlalchemy.orm import relationship


class UserRole(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(200))


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.INTEGER, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    age = db.Column(db.INTEGER)
    email = db.Column(db.String(200), unique=True)
    role_id = db.Column(db.String(200), db.ForeignKey('user_roles.id'))
    phone = db.Column(db.String(20), unique=True)

    order = relationship('Order')
    offer = relationship('Offer')
    role = relationship('UserRole')


class Offer(db.Model):
    __tablename__ = 'offers'
    id = db.Column(db.INTEGER, primary_key=True)

    order_id = db.Column(db.INTEGER, db.ForeignKey('orders.id'))
    executor_id = db.Column(db.INTEGER, db.ForeignKey('users.id'))

    order = relationship('Order')
    executor = relationship('User')


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(200))
    description = db.Column(db.String)
    start_date = db.Column(db.String)
    end_date = db.Column(db.String)
    address = db.Column(db.String)
    price = db.Column(db.INTEGER)

    customer_id = db.Column(db.INTEGER, db.ForeignKey('users.id'))
    executor_id = db.Column(db.INTEGER, db.ForeignKey('users.id'))

    customer = relationship('User', foreign_keys='Order.customer_id')
    executor = relationship('User', foreign_keys='Order.executor_id')

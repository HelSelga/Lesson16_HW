from app.db import db
from sqlalchemy.orm import relationship


class UserRole(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(200), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('user_roles.id'))
    phone = db.Column(db.String(20), unique=True)

    role = relationship('UserRole', foreign_keys=role_id)


class Offer(db.Model):
    __tablename__ = 'offers'
    id = db.Column(db.Integer, primary_key=True)

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    order = relationship('Order', foreign_keys=order_id)
    executor = relationship('User', foreign_keys=executor_id)


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    description = db.Column(db.String)
    start_date = db.Column(db.String)
    end_date = db.Column(db.String)
    address = db.Column(db.String)
    price = db.Column(db.Integer)

    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    customer = relationship('User', foreign_keys=customer_id)
    executor = relationship('User', foreign_keys=executor_id)

from datetime import datetime
from app import ma, db
from models.coin import Coin
from models.user import User
from .base import BaseModel, BaseSchema
from marshmallow import fields

class Transaction(db.Model, BaseModel):

    __tablename__ = 'transactions'

    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    buy = db.Column(db.Integer)
    sell = db.Column(db.Integer)
    buy_quantity = db.Column(db.Integer)
    sell_quantity = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='user_transaction')
    coin_id = db.Column(db.Integer, db.ForeignKey('coins.id'))
    coin = db.relationship('Coin', backref='coin_transaction')

class TransactionSchema(ma.ModelSchema, BaseSchema):
    user = fields.Nested('UserSchema', only=('id', 'username'))
    coin = fields.Nested('CoinSchema', only=('currency', 'full_name'))
    class Meta:
        model = Transaction

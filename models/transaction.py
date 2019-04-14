from datetime import datetime
from app import ma, db
from models.coin import Coin
from models.user import User
from .base import BaseModel, BaseSchema
from marshmallow import fields

class Transaction(db.Model, BaseModel):

    __tablename__ = 'transactions'

    timestamp = db.Column(db.Date)
    buy = db.Column(db.Float)
    sell = db.Column(db.Float)
    buy_quantity = db.Column(db.Float)
    sell_quantity = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='user_transaction')
    coin_id = db.Column(db.String, db.ForeignKey('coins.id'))
    coin = db.relationship('Coin', backref='coin_transaction')

class TransactionSchema(ma.ModelSchema, BaseSchema):
    user = fields.Nested('UserSchema', only=('id', 'username'))
    coin = fields.Nested('CoinSchema', only=('currency', 'full_name'))
    class Meta:
        model = Transaction

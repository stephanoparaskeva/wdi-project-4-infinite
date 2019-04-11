from app import ma, db
from .base import BaseModel, BaseSchema
from marshmallow import fields

class Coin(db.Model):

    __tablename__ = 'coins'

    id = db.Column(db.String, primary_key=True)
    currency = db.Column(db.String(6), nullable=False, unique=True)
    full_name = db.Column(db.String(20), unique=True)

class CoinSchema(ma.ModelSchema, BaseSchema):

    coin_transaction = fields.Nested('TransactionSchema', many=True)
    class Meta:

        model = Coin

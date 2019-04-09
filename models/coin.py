from app import ma, db
from .base import BaseModel, BaseSchema
from marshmallow import fields

class Coin(db.Model, BaseModel):

    __tablename__ = 'coins'

    symbol = db.Column(db.String(6), nullable=False, unique=True)
    full_name = db.Column(db.String(20), unique=True)

class CoinSchema(ma.ModelSchema, BaseSchema):
    user_transaction = fields.Nested('TransactionSchema', many=True)
    class Meta:
        model = Coin

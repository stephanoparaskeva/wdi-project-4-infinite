from app import ma, db
from .base import BaseModel, BaseSchema
from marshmallow import fields

class Coin(db.Model):

    __tablename__ = 'coins'

    id = db.Column(db.String, primary_key=True)
    url = db.Column(db.String)
    currency = db.Column(db.String(), nullable=False)
    full_name = db.Column(db.String())

class CoinSchema(ma.ModelSchema, BaseSchema):
    class Meta:

        model = Coin

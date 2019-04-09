from datetime import datetime, timedelta
from app import db, ma, bcrypt
from config.environment import secret
import jwt
from .base import BaseModel, BaseSchema
from marshmallow import validates_schema, ValidationError, validate, fields
from sqlalchemy.ext.hybrid import hybrid_property

class User(db.Model, BaseModel):

    __tablename__ = 'users'

    username = db.Column(db.String(28), nullable=False, unique=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))

    @hybrid_property
    def password(self):
        pass

    @password.setter # two password functions out of scope as theyre in the scope of the decorators
    def password(self, plaintext):
        self.password_hash = bcrypt.generate_password_hash(plaintext).decode('utf-8')

    #different from previous, this is a sperate function to validate on login, hashing new plaintext and comparing that to hashed password
    def validate_password(self, plaintext):
        return bcrypt.check_password_hash(self.password_hash, plaintext)

    #hybrid decorator pulls the password out and virtually creates a field for it
    #password.setter pulls this as plaintext and the adds the hashed version to the table under password_hash

    def generate_token(self):
        payload = {
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(),
        'sub': self.id
        }

        token = jwt.encode(
            payload,
            secret,
            'HS256'
        ).decode('utf-8')

        return token

class UserSchema(ma.ModelSchema, BaseSchema):

    @validates_schema
    def check_passwords_match(self, data):
        if data.get('password') != data.get('password_confirmation'):
            raise ValidationError(
            'Passwords do not match',
            'password_confirmation'
            )

    password = fields.String(
        required=True,
        validate=[validate.Length(min=8, max=50)]
    )

    password_confirmation = fields.String(required=True)

    user_transaction = fields.Nested('TransactionSchema', many=True)

    class Meta:
        model = User
        exclude = ('password_hash',)

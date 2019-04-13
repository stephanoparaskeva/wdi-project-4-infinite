from datetime import datetime
from app import db
from marshmallow import fields

class BaseModel:

    id = db.Column(db.Integer, primary_key=True)

    def save(self):
        self.updated_at = datetime.utcnow()

        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()

class BaseSchema:
    created_at = fields.DateTime(format='%Y-%m-%d %H:%M:%S')
    updated_at = fields.DateTime(format='%Y-%m-%d %H:%M:%S')

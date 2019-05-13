from flask import Blueprint, jsonify, request
from validate_email import validate_email
import re
from models.user import User, UserSchema
from lib.helpers import is_unique

api = Blueprint('auth', __name__)
user_schema = UserSchema()

@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    user, errors = user_schema.load(data)
    if not is_unique(model=User, key='username', value=data['username']):
        errors['username'] = errors.get('username', []) + ['Username already taken']

    if not is_unique(model=User, key='email', value=data['email']):
        errors['email'] = errors.get('email', []) + ['Email already taken']

    # if not validate_email(data['email']):
    #     errors['email'] = errors.get('email', []) + ['Email invalid']
    #
    # if not re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])[\w\d@#$]{6,12}$", data['password']):
    #     errors['password'] = errors.get('password', []) + ['Password must contain at least one uppercase character, one lowercase and one number']

    if errors:
        return jsonify(errors), 422

    user.save()

    return jsonify({'message': 'Registration Successful'}), 201

@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    user = User.query.filter_by(email=data.get('email')).first()

    if not user or not user.validate_password(data.get('password', '')):
        return jsonify({'message': 'Unauthorized'}), 401

    return jsonify({
        'message': 'Welcome back {}!'.format(user.username),
        'token': user.generate_token()
    })

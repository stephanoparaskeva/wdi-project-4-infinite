from lib.secure_route import secure_route
from flask import Blueprint, request, jsonify, g
from models.transaction import Transaction, TransactionSchema
from models.coin import Coin


transaction_schema = TransactionSchema()

api = Blueprint('transactions', __name__)

@api.route('/transactions', methods=['GET'])
def transactions():

    transactions = Transaction.query.all()

    return transaction_schema.jsonify(transactions, many=True), 200

@api.route('/transactions', methods=['POST'])
@secure_route
def post_transactions():

    data = request.get_json()
    transaction, errors = transaction_schema.load(data)
    coin = Coin.query.get(data['coin_id'])
    if errors:
        return jsonify(errors), 422
    transaction.coin = coin
    transaction.user = g.current_user
    transaction.save()

    return transaction_schema.jsonify(transaction), 200

@api.route('/transactions/<int:transaction_id>', methods=['PUT'])
@secure_route
def update_transaction(transaction_id):
    transaction = Transaction.query.get(transaction_id)
    transaction, errors = transaction_schema.load(request.get_json(), instance=transaction, partial=True)
    if errors:
        return jsonify(errors), 422

    if transaction.user != g.current_user:
        return jsonify({'message': 'Unauthorized'}), 401

    transaction.save()
    return transaction_schema.jsonify(transaction)

@api.route('/transactions/<int:transaction_id>', methods=['DELETE'])
@secure_route
def delete_transaction(transaction_id):
    transaction = Transaction.query.get(transaction_id)
    if transaction.user != g.current_user:
        return jsonify({'message': 'Unauthorized'}), 401
    transaction.remove()
    return '', 204

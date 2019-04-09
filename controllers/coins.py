from lib.secure_route import secure_route
from flask import Blueprint, request, jsonify, g
from models.coin import Coin, CoinSchema

coin_schema = CoinSchema()

api = Blueprint('coins', __name__)

@api.route('/coins', methods=['GET'])
def coins():

    coins = Coin.query.all()

    return coin_schema.jsonify(coins, many=True), 200

@api.route('/coins', methods=['POST'])
@secure_route
def post_transactions():

    data = request.get_json()
    coin, errors = coin_schema.load(data)
    if errors:
        return jsonify(errors), 422
    coin.save()

    return coin_schema.jsonify(coin), 200

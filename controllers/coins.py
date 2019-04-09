from flask import Blueprint, request, jsonify, g
from models.coin import Coin, CoinSchema

coin_schema = CoinSchema()

api = Blueprint('coins', __name__)

@api.route('/coins', methods=['GET'])
def coins():

    coins = Coin.query.all()

    return coin_schema.jsonify(coins, many=True), 200

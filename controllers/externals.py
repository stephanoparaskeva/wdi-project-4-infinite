import os
from flask import Blueprint, request
import requests

api = Blueprint('external', __name__)

@api.route('/nomics/candles', methods=['GET'])
def get_candles():
    url = 'https://api.nomics.com/v1/candles'
    key = os.environ.get('NOMICS_API_KEY')
    interval = '1d'
    currency = request.args.get('currency')
    start = request.args.get('start')
    end = request.args.get('end')
    payload = {'key': key, 'interval': interval, 'currency': currency, 'start': start, 'end': end}
    r = requests.get(url, params=payload)
    return r.text

@api.route('/nomics/tickers', methods=['GET'])
def get_tickers():
    url = 'https://api.nomics.com/v1/currencies/ticker'
    key = os.environ.get('NOMICS_API_KEY')
    payload = {'key': key}
    r = requests.get(url, params=payload)
    return r.text

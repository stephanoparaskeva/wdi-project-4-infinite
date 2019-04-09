from app import app, db

from models.coin import Coin
from models.transaction import Transaction
from models.user import UserSchema
user_schema = UserSchema()

with app.app_context():
    db.drop_all()
    db.create_all()

    stephano, errors = user_schema.load({
        'username': 'stephano',
        'email': 'stephano@email.com',
        'password': 'password',
        'password_confirmation': 'password'
    })

    if errors:
        raise Exception(errors)

    db.session.add(stephano)

    alexander, errors = user_schema.load({
        'username': 'alexander',
        'email': 'alexander@email.com',
        'password': 'password',
        'password_confirmation': 'password'
    })

    if errors:
        raise Exception(errors)

    db.session.add(alexander)

    btc = Coin(symbol='BTC', full_name='Bitcoin')
    eth = Coin(symbol='ETH', full_name='Ethereum')
    ltc = Coin(symbol='LTC', full_name='Litecoin')
    usdt = Coin(symbol='USDT', full_name='Tether')

    transaction1 = Transaction(user=stephano, buy=1000, coin=btc)
    transaction2 = Transaction(user=stephano, sell=500, coin=btc)
    transaction3 = Transaction(user=alexander, buy=840, coin=eth)
    transaction4 = Transaction(user=alexander, buy=302, coin=ltc)

    db.session.add_all([btc, eth, ltc, usdt, transaction1, transaction2, transaction3, transaction4])

    db.session.commit()

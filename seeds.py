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
    #
    # sabo, errors = user_schema.load({
    #     'username': 'sabo',
    #     'email': 'sabo@email.com',
    #     'password': 'password',
    #     'password_confirmation': 'password'
    # })
    #
    # if errors:
    #     raise Exception(errors)
    #
    # db.session.add(sabo)

    btc = Coin(currency='BTC', full_name='Bitcoin')
    eth = Coin(currency='ETH', full_name='Ethereum')
    xrp = Coin(currency='XRP', full_name='Ripple')
    ltc = Coin(currency='LTC', full_name='Litecoin')
    bch = Coin(currency='BCH', full_name='Bitcoin Cash')
    eos = Coin(currency='EOS', full_name='Eos')
    bnb = Coin(currency='BNB', full_name='Binance Coin')
    xlm = Coin(currency='XLM', full_name='Stellar')
    ada = Coin(currency='ADA', full_name='Cardano')
    usdt = Coin(currency='USDT', full_name='Tether')

    transaction1 = Transaction(user=stephano, buy=5000, buy_quantity=10, coin=btc)
    transaction2 = Transaction(user=stephano, sell=5000, sell_quantity=5, coin=btc)
    # transaction3 = Transaction(user=stephano, buy=1000, buy_quantity=5, coin=eth)
    # transaction4 = Transaction(user=stephano, sell=500, sell_quantity=3, coin=eth)
    # transaction5 = Transaction(user=stephano, buy=1000, buy_quantity=6, coin=ltc)
    # transaction6 = Transaction(user=stephano, sell=500, sell_quantity=2, coin=ltc)
    # transaction7 = Transaction(user=stephano, buy=1000, buy_quantity=8, coin=xrp)
    # transaction8 = Transaction(user=stephano, sell=500, sell_quantity=1, coin=xrp)
    # transaction9 = Transaction(user=stephano, sell=500, buy_quantity=3, coin=ltc)
    # transaction10 = Transaction(user=stephano, sell=500, coin=ltc)
    # transaction11 = Transaction(user=stephano, sell=500, coin=btc)
    # transaction12 = Transaction(user=stephano, sell=500, sell_quantity=6, coin=btc)

    db.session.add_all([btc, eth, xrp, ltc, bch, eos, bnb, xlm, ada, usdt, transaction1, transaction2])

    db.session.commit()

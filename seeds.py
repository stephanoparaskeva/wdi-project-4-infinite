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

    sabo, errors = user_schema.load({
        'username': 'sabo',
        'email': 'sabo@email.com',
        'password': 'password',
        'password_confirmation': 'password'
    })

    if errors:
        raise Exception(errors)

    db.session.add(sabo)

    btc = Coin(currency='BTC', full_name='Bitcoin', id='BTC')
    eth = Coin(currency='ETH', full_name='Ethereum', id='ETH')
    xrp = Coin(currency='XRP', full_name='Ripple', id='XRP')
    ltc = Coin(currency='LTC', full_name='Litecoin', id='LTC')
    bch = Coin(currency='BCH', full_name='Bitcoin Cash', id='BCH')
    eos = Coin(currency='EOS', full_name='Eos', id='EOS')
    bnb = Coin(currency='BNB', full_name='Binance Coin', id='BNB')
    xlm = Coin(currency='XLM', full_name='Stellar', id='XLM')
    ada = Coin(currency='ADA', full_name='Cardano', id='ADA')
    usdt = Coin(currency='USDT', full_name='Tether', id='USDT')

    transaction3 = Transaction(user=stephano, buy=1000, buy_quantity=5, coin=eth, timestamp='2015-03-18')
    transaction2 = Transaction(user=stephano, sell=500, sell_quantity=2, coin=ltc, timestamp='2015-02-18')
    transaction13 = Transaction(user=stephano, sell=500, sell_quantity=2, coin=btc, timestamp='2015-02-18')
    transaction14 = Transaction(user=stephano, sell=500, sell_quantity=2, coin=btc, timestamp='2015-02-18')
    transaction1 = Transaction(user=stephano, buy=1000, buy_quantity=13, coin=btc, timestamp='2015-01-18')
    transaction5 = Transaction(user=stephano, buy=1000, buy_quantity=6, coin=ltc, timestamp='2015-05-18')
    transaction6 = Transaction(user=stephano, sell=500, sell_quantity=2, coin=ltc, timestamp='2015-06-18')
    transaction15 = Transaction(user=stephano, sell=500, sell_quantity=2, coin=eth, timestamp='2015-06-18')
    transaction16 = Transaction(user=stephano, sell=500, sell_quantity=2, coin=btc, timestamp='2015-06-18')
    transaction17 = Transaction(user=stephano, sell=500, sell_quantity=2, coin=xrp, timestamp='2015-06-18')
    transaction8 = Transaction(user=stephano, sell=500, sell_quantity=1, coin=xrp, timestamp='2015-08-18')
    transaction4 = Transaction(user=stephano, sell=500, sell_quantity=3, coin=eth, timestamp='2015-04-18')
    transaction9 = Transaction(user=stephano, sell=500, buy_quantity=3, coin=ltc, timestamp='2015-09-18')
    transaction7 = Transaction(user=stephano, buy=1000, buy_quantity=8, coin=xrp, timestamp='2015-07-18')
    transaction10 = Transaction(user=stephano, sell=500, coin=ltc, timestamp='2015-10-18')
    transaction11 = Transaction(user=stephano, sell=500, coin=btc, timestamp='2015-11-18')
    transaction12 = Transaction(user=stephano, sell=500, sell_quantity=6, coin=btc, timestamp='2015-12-18')

    transaction20 = Transaction(user=sabo, buy=200, buy_quantity=6, coin=btc, timestamp='2016-12-18')
    transaction21 = Transaction(user=sabo, buy=2, buy_quantity=6, coin=ltc, timestamp='2015-12-18')
    transaction22 = Transaction(user=sabo, sell=10, sell_quantity=6, coin=eth, timestamp='2013-12-18')
    transaction23 = Transaction(user=sabo, sell=2, sell_quantity=3, coin=ltc, timestamp='2015-2-18')
    transaction24 = Transaction(user=sabo, buy=10, buy_quantity=6, coin=xrp, timestamp='2015-9-18')

    db.session.add_all([btc, eth, xrp, ltc, bch, eos, bnb, xlm, ada, usdt, transaction1,
     transaction2, transaction3, transaction4, transaction5, transaction6, transaction7,
     transaction8, transaction9, transaction10, transaction11, transaction12, transaction13, transaction14,
     transaction15, transaction16, transaction17, transaction20, transaction21, transaction22, transaction23, transaction24])

    db.session.commit()

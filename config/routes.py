from app import app
from controllers import coins, transactions, auth

app.register_blueprint(coins.api, url_prefix='/api')
app.register_blueprint(transactions.api, url_prefix='/api')
app.register_blueprint(auth.api, url_prefix='/api')

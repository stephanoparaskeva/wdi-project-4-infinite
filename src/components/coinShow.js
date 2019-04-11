import React from 'react'
import { Link } from 'react-router-dom'
import Candle from '../candle'

class Coin extends React.Component {
  constructor() {
    super()

    this.state = {}
  }

  render() {
    const coin = this.props.location.state.coin
    return(
      <div>
        <h1>{coin.currency}</h1>
        <Candle
          coin={coin.currency}
        />
        <span className="col-2">${parseFloat(coin.price).toFixed(2)}</span>
        <p>Price Change</p>
        <span>{coin['1d'].price_change_pct}%</span>
        <p>Market Cap</p>
        <span>${coin.market_cap}</span>
        <p>Circulating Supply</p>
        <p>{coin.circulating_supply} {coin.currency}</p>
        <Link to={
          {
            pathname: '/transactionform',
            state: { coin }
          }
        }>
          <button>Add Transaction</button>
        </Link>
      </div>
    )
  }
}

export default Coin

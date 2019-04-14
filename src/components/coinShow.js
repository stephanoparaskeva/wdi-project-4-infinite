import React from 'react'
import { Link } from 'react-router-dom'
import Candle from '../candle'

class Coin extends React.Component {
  constructor() {
    super()

    this.state = {
    }
  }

  render() {
    console.log('re-render')
    const coin = this.props.location.state.coin
    return(
      <div>
        <div className="row">
          <h1 className="">{coin.currency}</h1>
          <Link to={
            {
              pathname: '/transaction',
              state: { coin }
            }
          }><button className="">Add Transaction</button></Link>
        </div>
        <Candle
          coin={ coin.currency }
        />
        <div className="row">
        </div>
        <div className="row">
          <span>Price: ${parseFloat(coin.price).toFixed(2)}</span>
          <span>Price Change: {coin['1d'].price_change_pct}%</span>
          <span>Market Cap: ${coin.market_cap}</span>
          <span>Circulating Supply: {coin.circulating_supply} {coin.currency}</span>
        </div>
      </div>
    )
  }
}

export default Coin

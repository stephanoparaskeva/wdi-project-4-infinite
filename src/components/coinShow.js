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
    const coin = this.props.location.state.coin
    return(
      <div className="coin-show">
        <div className="row">
          <h1>{coin.currency}</h1>
        </div>
        <div className="row candle-graph">
          <Candle
            coin={ coin.currency }
          />
        </div>
        <div className="row coin-add">
          <Link to={
            {
              pathname: '/transaction',
              state: { coin }
            }
          }><i className="fas fa-plus-circle"></i></Link>
          <div className="row coin-info">
            <span>Price: ${parseFloat(coin.price).toFixed(2)}</span>
            <span>Price Change: {coin['1d'].price_change_pct}%</span>
            <span>Market Cap: ${coin.market_cap}</span>
            <span>Circulating Supply: {coin.circulating_supply} {coin.currency}</span>
          </div>
        </div>
      </div>
    )
  }
}

export default Coin

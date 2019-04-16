import React from 'react'
import { Link } from 'react-router-dom'
import Candle from '../candle'
import Common from '../lib/common'

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
          <div className="row coin-info">
            <span className="twelve columns">Price: ${parseFloat(coin.price).toFixed(2)}</span>
            <span className={`${Common.checkChange(coin)} twelve columns`}>Price Change: {coin['1d'].price_change_pct}%</span>
            <span className="twelve columns">Market Cap: ${coin.market_cap}</span>
            <span className="twelve columns">Circulating Supply: {coin.circulating_supply} {coin.currency}</span>
          </div>
        </div>
        <div className="row candle-graph">
          <Candle
            coin={ coin.currency }
          />
        </div>
        <Link to={
          {
            pathname: '/transaction',
            state: { coin }
          }
        }><i className="fas fa-plus-circle"></i></Link>
      </div>
    )
  }
}

export default Coin

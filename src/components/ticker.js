import React from 'react'
import axios from 'axios'

import Common from '../lib/common'

class Ticker extends React.Component {
  constructor() {
    super()

    this.state = {}
  }

  getCurrencies() {
    const tickerData = this.props.nomics.filter(coin => coin.rank <= 20)
    this.setState({tickerData})
  }

  componentDidMount() {
    this.getCurrencies()
  }

  render() {
    const coins = this.state.tickerData
    if (!coins) return null
    return(
      <div className="ticker-wrapper">
        <div className="ticker">
          {coins.map(coin =>
            <div key={coin.currency} className="ticker-item">
              <span><img src={coin.image_url} className="ticker-img"/></span>
              <span>  {coin.currency}</span>
              <span className={Common.checkChange(coin)}> {coin['1d'].price_change_pct}%</span>
            </div>
          )}
        </div>
      </div>
    )
  }
}

export default Ticker

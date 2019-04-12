import React from 'react'
import axios from 'axios'

import Common from '../lib/common'

class Ticker extends React.Component {
  constructor() {
    super()

    this.state = {}
  }

  getCurrencies() {
    this.setState({tickerData: this.props.nomics.filter(coin => {
      return coin.rank <= 20
    })
    })
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
              <span>{coin.currency}</span>
              <span className={Common.checkChange(coin)}> {coin['1d'].price_change_pct}%</span>
            </div>
          )}
        </div>
      </div>
    )
  }
}

export default Ticker

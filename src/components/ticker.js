import React from 'react'
import axios from 'axios'

class Ticker extends React.Component {
  constructor() {
    super()

    this.state = {}
  }

  getCurrencies() {
    axios.get('https://api.nomics.com/v1/currencies/ticker?key=cfa361e67a06d9209da08f36a340410b')
      .then(res => {
        this.setState({tickerData: res.data.filter(coin => {
          return coin.rank <= 20
        })
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
      <div className="col-1">
        <div className="ticker">
          {coins.map(coin =>
            <div key={coin.currency} className="ticker-item">
              <span>{coin.currency}</span>
              <span> {coin['1d'].price_change_pct}%</span>
            </div>
          )}
        </div>
      </div>
    )
  }
}

export default Ticker

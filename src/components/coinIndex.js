import React from 'react'
import axios from 'axios'

class CoinIndex extends React.Component {
  constructor() {
    super()

    this.state = {}
  }

  getCurrencies() {
    axios.get('https://api.nomics.com/v1/currencies/ticker?key=cfa361e67a06d9209da08f36a340410b')
      .then(res => {
        this.setState({tickerData: res.data.filter(coin => {
          return coin.rank < 100
        })})
      })
  }

  componentDidMount() {
    this.getCurrencies()
  }

  render() {
    const coins = this.state.tickerData
    if (!coins) return null
    return(
      <div>
        {coins.map(coin =>
          <div key={coin.rank}>
            <h2>{coin.rank}. {coin.currency}</h2>
            <p>Price</p>
            <span>${coin.price}</span>
            <br/>
            <p>Price Change</p>
            <span>{coin['1d'].price_change_pct}%</span>
            <br/>
            <p>Market Cap</p>
            <span>${coin.market_cap}</span>
            <p>Circulating Supply</p>
            <span>{coin.circulating_supply} {coin.currency}</span>
          </div>
        )}
      </div>
    )
  }
}

export default CoinIndex

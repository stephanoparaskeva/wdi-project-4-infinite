import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'

class CoinIndex extends React.Component {
  constructor() {
    super()

    this.state = {}
  }

  getCurrencies() {
    axios.get('https://api.nomics.com/v1/currencies/ticker?key=cfa361e67a06d9209da08f36a340410b')
      .then(res => {
        this.setState({tickerData: res.data.filter(coin => {
          return coin.rank <= 100
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
      <div className="container border">
        {coins.map(coin =>
          <Link key={coin.rank} to={
            {
              pathname: '/coin',
              state: { coin }
            }
          }>
            <div>
              <div className="row border">
                <h2 className="col-10">{coin.rank}. {coin.currency}</h2>
                <span className="col-2">${parseFloat(coin.price).toFixed(2)}</span>
              </div>
              <p>Price Change</p>
              <span>{coin['1d'].price_change_pct}%</span>
              <p>Market Cap</p>
              <span>${coin.market_cap}</span>
              <p>Circulating Supply</p>
              <span>{coin.circulating_supply} {coin.currency}</span>
            </div>
          </Link>
        )}
      </div>
    )
  }
}

export default CoinIndex

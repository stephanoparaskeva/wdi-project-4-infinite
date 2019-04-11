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

  checkChange(coin) {
    if(coin['1d'].price_change_pct >= 0) {
      return 'up'
    }
    return 'down'
  }

  componentDidMount() {
    this.getCurrencies()
  }

  render() {
    const coins = this.state.tickerData
    if (!coins) return null
    return(
      <table className="u-full-width">
        <thead>
          <tr>
            <th>Name</th>
            <th>Price</th>
            <th>Change</th>
            <th>ATH</th>
          </tr>
        </thead>
        {coins.map(coin =>
          <tbody key={coin.rank}>
            <tr>
              <td>{coin.rank}. {coin.currency}</td>
              <td>${parseFloat(coin.price).toFixed(2)}</td>
              <td className={this.checkChange(coin)}>{coin['1d'].price_change_pct || 0}%</td>
              <td>${parseFloat(coin.high).toFixed(2)}</td>
            </tr>
          </tbody>
        )}
      </table>
    )
  }
}

export default CoinIndex

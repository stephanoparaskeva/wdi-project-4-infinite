import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'

import Common from '../lib/common'

class CoinIndex extends React.Component {
  constructor() {
    super()

    this.state = {}
  }

  getCurrencies() {
    this.setState({tickerData: this.props.nomics.data.filter(coin => {
      return coin.rank <= 100
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
              <td><Link to={{
                pathname: '/coin',
                state: {coin}
              }}>{coin.rank}. {coin.currency}</Link></td>
              <td><Link to={{
                pathname: '/coin',
                state: {coin}
              }}>${parseFloat(coin.price).toFixed(2)}</Link></td>
              <td className={Common.checkChange(coin)}><Link to={{
                pathname: '/coin',
                state: {coin}
              }}>{coin['1d'].price_change_pct || 0}%</Link></td>
              <td><Link to={{
                pathname: '/coin',
                state: {coin}
              }}>${parseFloat(coin.high).toFixed(2)}</Link></td>
            </tr>
          </tbody>
        )}
      </table>
    )
  }
}

export default CoinIndex

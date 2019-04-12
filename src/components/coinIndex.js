import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'

import Common from '../lib/common'

class CoinIndex extends React.Component {
  constructor() {
    super()

    this.state = {
      search: ''
    }

    this.handleChange = this.handleChange.bind(this)
  }

  getCurrencies() {
    const tickerData = this.props.nomics.data.filter(coin => coin.rank <= 1000)
    this.setState({tickerData})
  }

  handleChange(e) {
    this.setState({ search: e.target.value })
  }

  filteredBySearch() {
    const regex = new RegExp(this.state.search, 'i')
    const arr = this.state.tickerData.filter(data => {
      return regex.test(data.currency)
    })
    return arr
  }

  componentDidMount() {
    this.getCurrencies()
  }

  render() {
    const coins = this.state.tickerData
    if (!coins) return null
    return(
      <div>
        <form>
          <input
            className="input"
            onChange={this.handleChange}
            value={this.state.search}
            name="search"
          >
          </input>
        </form>
        <table className="u-full-width">
          <thead>
            <tr>
              <th>Name</th>
              <th>Price</th>
              <th>Change</th>
              <th>ATH</th>
            </tr>
          </thead>
          {this.filteredBySearch().map(coin =>
            <tbody key={coin.rank}>
              <tr>
                <td><Link to={{
                  pathname: '/coin',
                  state: {coin}
                }}>{coin.rank}. {coin.currency}</Link></td>
                <td><Link to={{
                  pathname: '/coin',
                  state: {coin}
                }}>${parseFloat(coin.price).toFixed(2) || 0}</Link></td>
                <td className={Common.checkChange(coin)}><Link to={{
                  pathname: '/coin',
                  state: {coin}
                }}>{coin['1d'].price_change_pct || 0}%</Link></td>
                <td><Link to={{
                  pathname: '/coin',
                  state: {coin}
                }}>${parseFloat(coin.high).toFixed(2) || 0}</Link></td>
              </tr>
            </tbody>
          )}
        </table>
      </div>
    )
  }
}

export default CoinIndex

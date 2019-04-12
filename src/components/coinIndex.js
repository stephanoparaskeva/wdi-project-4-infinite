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

  handleChange(e) {
    this.setState({ search: e.target.value })
  }

  filteredBySearch(filterByRank) {
    const regex = new RegExp(this.state.search, 'i')
    const arr = this.props.nomics.filter(data => {
      return regex.test(data.currency) && data.rank <= filterByRank
    })
    return arr
  }



  render() {
    const coins = this.props.nomics
    const filterByRank = this.state.search !== '' ? 10000 : 50
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
          {this.filteredBySearch(filterByRank).map(coin =>
            <tbody key={coin.rank}>
              <tr>
                <td><Link to={{
                  pathname: '/coin',
                  state: {coin}
                }}><img className="imgimg" src={coin.image_url}></img>{coin.rank}. {coin.currency}</Link></td>
                <td>
                  <Link to={{
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

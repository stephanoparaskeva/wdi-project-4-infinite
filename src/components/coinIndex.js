import React from 'react'
import { Link } from 'react-router-dom'

import Common from '../lib/common'

class CoinIndex extends React.Component {
  constructor() {
    super()

    this.state = {
      search: '',
      time: '1d'
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleTime = this.handleTime.bind(this)
  }

  handleChange(e) {
    this.setState({ search: e.target.value })
  }

  handleTime(e) {
    this.setState({time: e.target.value})
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
    const filterByRank = this.state.search !== '' ? 10000 : 49
    if (!coins) return null
    return(
      <div>
        <form>SEARCH
          <input
            className="input"
            onChange={this.handleChange}
            value={this.state.search}
            name="search"
          >
          </input>
        </form>
        <button className="three columns" onClick={this.handleTime} value="1d">1d</button>
        <button className="three columns" onClick={this.handleTime} value="7d">1w</button>
        <button className="three columns" onClick={this.handleTime} value="30d">1m</button>
        <button className="three columns" onClick={this.handleTime} value="365d">1y</button>
        <table className="u-full-width">
          <thead>
            <tr>
              <th></th>
              <th></th>
              <th>Name</th>
              <th>Price</th>
              <th>Change</th>
              <th>ATH</th>
            </tr>
          </thead>
          {this.filteredBySearch(filterByRank).map(coin =>
            <tbody key={coin.rank}>
              <tr>
                <td>
                  <Link to={{
                    pathname: '/coin',
                    state: {coin}
                  }}><span>        </span>
                  </Link>
                </td>
                <td>
                  <Link to={{
                    pathname: '/coin',
                    state: {coin}
                  }}><img className="imgimg" src={coin.image_url}></img>
                  </Link>
                </td>
                <td>
                  <Link to={{
                    pathname: '/coin',
                    state: {coin}
                  }}>
                    {coin.rank}. {coin.currency}
                  </Link>
                </td>
                <td>
                  <Link to={{
                    pathname: '/coin',
                    state: {coin}
                  }}>
                    ${parseFloat(coin.price).toFixed(2) || 0}
                  </Link>
                </td>
                <td className={Common.checkChange(coin, this.state.time)}>
                  <Link to={{
                    pathname: '/coin',
                    state: {coin}
                  }}>
                    {coin[`${this.state.time}`].price_change_pct || 0}%
                  </Link>
                </td>
                <td>
                  <Link to={{
                    pathname: '/coin',
                    state: {coin}
                  }}>
                    ${parseFloat(coin.high).toFixed(2) || 0}
                  </Link>
                </td>
              </tr>
            </tbody>
          )}
        </table>
      </div>
    )
  }
}

export default CoinIndex

import React from 'react'
import { Link } from 'react-router-dom'
import numeral from 'numeral'

import Common from '../lib/common'
// <button className="three columns" onClick={this.handleTime} value="1d">1d</button>
// <button className="three columns" onClick={this.handleTime} value="7d">1w</button>
// <button className="three columns" onClick={this.handleTime} value="30d">1m</button>
// <button className="three columns" onClick={this.handleTime} value="365d">1y</button>

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

  stopSumbit(e) {
    e.preventDefault()
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
    const filterByRank = this.state.search !== '' ? 10000 : 50
    if (!coins) return null
    return(
      <div>
        <div className="row">
          <h2>Markets</h2>
          <div className="search">
            <form onSubmit={this.stopSumbit}>
              <input
                type="search"
                onChange={this.handleChange}
                value={this.state.search}
                name="search"
              >
              </input>
              <i className="fa fa-search"></i>
            </form>
          </div>
        </div>
        <div className="row">
          <div className="flex twelve columns">
            <div className="three columns">
              <table className="u-full-width">
                <thead>
                  <tr>
                    <th>#</th>
                    <th></th>
                    <th>Asset</th>
                  </tr>
                </thead>
                {this.filteredBySearch(filterByRank).map(coin =>
                  <tbody key={coin.rank} className="table-head">
                    <tr>
                      <td>
                        <Link to={{
                          pathname: '/coin',
                          state: {coin}
                        }}>
                          {coin.rank}
                        </Link>
                      </td>
                      <td>
                        <Link to={{
                          pathname: '/coin',
                          state: {coin}
                        }}>
                          <img className="imgimg" src={coin.image_url}></img>
                        </Link>
                      </td>
                      <td>
                        <div>
                          <Link to={{
                            pathname: '/coin',
                            state: {coin}
                          }}>
                            {coin.currency}
                          </Link>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                )}
              </table>
            </div>
            <div className="nine columns flow marg">
              <table className="u-full-width">
                <thead className="table-head">
                  <tr>
                    <th>Price</th>
                    <th>Change</th>
                    <th>ATH</th>
                    <th>Market Cap</th>
                    <th>Circulating Supply</th>
                    <th>Max Supply</th>
                  </tr>
                </thead>
                {this.filteredBySearch(filterByRank).map(coin =>
                  <tbody key={coin.rank} className="table-head">
                    <tr>
                      <td>
                        <Link to={{
                          pathname: '/coin',
                          state: {coin}
                        }}>
                          {numeral(parseFloat(coin.price)).format('$ 0,0.00') || 0}
                        </Link>
                      </td>
                      <td className={Common.checkChange(coin, this.state.time)}>
                        <Link to={{
                          pathname: '/coin',
                          state: {coin}
                        }}>
                          {coin['1d'].price_change_pct || 0}%
                        </Link>
                      </td>
                      <td>
                        <Link to={{
                          pathname: '/coin',
                          state: {coin}
                        }}>
                          {numeral(coin.high).format('$ 0,0.00') || 0}
                        </Link>
                      </td>
                      <td>
                        <Link to={{
                          pathname: '/coin',
                          state: {coin}
                        }}>
                          {numeral(coin.market_cap).format('($ 0.00 a)') || 0}
                        </Link>
                      </td>
                      <td>
                        <Link to={{
                          pathname: '/coin',
                          state: {coin}
                        }}>
                          {numeral(coin.circulating_supply).format('(0.00 a)') || 0}
                        </Link>
                      </td>
                      <td>
                        <Link to={{
                          pathname: '/coin',
                          state: {coin}
                        }}>
                          {coin.max_supply ? numeral(coin.max_supply).format('(0.00 a)') : '∞'}
                        </Link>
                      </td>
                    </tr>
                  </tbody>
                )}
              </table>
            </div>
          </div>
        </div>
      </div>
    )
  }
}

export default CoinIndex

import React from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'

class CoinList extends React.Component {
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
    const filterByRank = this.state.search !== '' ? 10000 : 0
    return(
      <div className="search">
        <div className="index-search">
          <form>
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
        <table className="u-full-width">
          {this.props.nomics && this.filteredBySearch(filterByRank).map(coin => (
            <tbody key={coin.rank}>
              <tr>
                <td><Link to={{
                  pathname: '/transaction',
                  state: {coin}
                }}><img className="imgimg" src={coin.image_url}></img></Link></td>
                <td><Link to={{
                  pathname: '/transaction',
                  state: {coin}
                }}>{coin.currency}</Link></td>
                <td><Link to={{
                  pathname: '/transaction',
                  state: {coin}
                }}>{coin.full_name}</Link></td>
              </tr>
            </tbody>
          )
          )}
        </table>
      </div>
    )
  }
}

export default CoinList

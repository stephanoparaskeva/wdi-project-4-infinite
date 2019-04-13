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
    const filterByRank = this.state.search !== '' ? 10000 : 10
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
        <table className="u-full-width">
          {this.props.nomics && this.filteredBySearch(filterByRank).map(coin => (
            <tbody key={coin.rank}>
              <tr>
                <td><Link to={{
                  pathname: '/transactionform',
                  state: {coin}
                }}><img className="imgimg" src={coin.image_url}></img></Link></td>
                <td><Link to={{
                  pathname: '/transactionform',
                  state: {coin}
                }}>{coin.currency}</Link></td>
                <td><Link to={{
                  pathname: '/transactionform',
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

import React from 'react'
import { Link } from 'react-router-dom'

class Holdings extends React.Component {
  constructor() {
    super()
    this.state = {}

    this.attachHoldingsToNomics = this.attachHoldingsToNomics.bind(this)
  }

  attachHoldingsToNomics(holdings, nomics) {
    const holdingsLookup = holdings.reduce((obj, current) => {
      obj[current.currency] = current.quantity
      return obj
    }, {})
    const filtered = nomics.filter(nomic => Object.keys(holdingsLookup).includes(nomic.currency))
    return filtered.map(item => ({...item, quantity: holdingsLookup[item.currency]}))
  }

  render() {
    const holdings = this.props.holdings
    const nomics = this.props.nomics
    return(
      <table className="u-full-width">
        <thead>
          <tr>
            <th></th>
            <th>Name</th>
            <th>Holdings</th>
            <th>Price</th>
          </tr>
        </thead>
        {this.attachHoldingsToNomics(holdings, nomics).map(coin => {
          if (coin.quantity > 0) {
            return  <tbody key={coin.rank}>
              <tr>
                <td><Link to={{
                  pathname: '/coin',
                  state: {coin}
                }}><img className="imgimg" src={coin.image_url}></img></Link></td>
                <td><Link to={{
                  pathname: '/coin',
                  state: {coin}
                }}>{coin.currency}</Link></td>
                <td><Link to={{
                  pathname: '/coin',
                  state: {coin}
                }}>{coin.quantity}</Link></td>
                <td><Link to={{
                  pathname: '/coin',
                  state: {coin}
                }}>{coin.price}</Link></td>
              </tr>
            </tbody>
          }
        }
        )}
      </table>
    )
  }
}
export default Holdings

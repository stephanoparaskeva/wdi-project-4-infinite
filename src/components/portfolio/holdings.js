import React from 'react'
import { Link } from 'react-router-dom'
import numeral from 'numeral'

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
      <table className="u-full-width holdings">
        <thead>
          <tr>
            <th></th>
            <th>Asseet</th>
            <th>Current Holdings</th>
            <th>Price</th>
            <th>% Change 24h</th>
          </tr>
        </thead>
        {this.attachHoldingsToNomics(holdings, nomics).map(coin => {
          if (coin.quantity > 0) {
            return  <tbody key={coin.rank}>
              <tr>
                <td>
                  <Link to={{
                    pathname: '/coin',
                    state: {coin}
                  }}>
                    <img className="imgimg" src={coin.image_url} />
                  </Link>
                </td>
                <td>
                  <Link to={{
                    pathname: '/coin',
                    state: {coin}
                  }}>{coin.currency}</Link>
                </td>
                <td><Link to={{
                  pathname: '/coin',
                  state: {coin}
                }}>{coin.quantity}</Link>
                </td>
                <td><Link to={{
                  pathname: '/coin',
                  state: {coin}
                }}>{numeral(parseFloat(coin.price)).format('$ 0,0.00') || 0}</Link></td>
                {coin['1d'].price_change_pct > 0 &&  <td className="positive"> <Link to={{
                  pathname: '/coin',
                  state: {coin}
                }}>+{coin['1d'].price_change_pct}%</Link></td>}
                {coin['1d'].price_change_pct < 0 && <td className="negative"><Link to={{
                  pathname: '/coin',
                  state: {coin}
                }}> {coin['1d'].price_change_pct}%/</Link></td>}
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

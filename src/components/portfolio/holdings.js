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
      <table className="u-full-width">
        <thead>
          <tr>
            <th className="th"></th>
            <th className="th"></th>
            <th className="th middle">Holdings</th>
            <th className="th far-right">Price</th>
          </tr>
        </thead>
        {this.attachHoldingsToNomics(holdings, nomics).map(coin => {
          if (coin.quantity > 0) {
            return  <tbody key={coin.rank}>
              <tr className="tr-style">
                <td className="img-holdings-td td"><Link to={{
                  pathname: '/coin',
                  state: {coin}
                }}><img className="img-holdings" src={coin.image_url}></img></Link></td>
                <td className="inner-td td"><ul><li className="inner-li">{coin.full_name}</li><li>{coin.currency}</li></ul><Link to={{
                  pathname: '/coin',
                  state: {coin}
                }}></Link>
                </td>
                <td className="middle td"><Link to={{
                  pathname: '/coin',
                  state: {coin}
                }}>{coin.quantity}</Link></td>
                <td className="inner-td td">
                  {coin['1d'].price_change_pct > 0 && <p className="positive inner-p">+{coin['1d'].price_change_pct}%</p>}
                  {coin['1d'].price_change_pct < 0 && <p className="negative inner-p">{coin['1d'].price_change_pct}%</p>}
                  <Link to={{
                    pathname: '/coin',
                    state: {coin}
                  }}>{numeral(parseFloat(coin.price)).format('$ 0,0.00') || 0}</Link></td>
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

import React from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'


class Transactions extends React.Component{
  constructor(){
    super()

    this.state = {}
  }

  setInitialState() {
    this.setState({transactionRequest: this.props.transactionRequest})
  }

  componentDidMount() {
    this.setInitialState()
  }

  render(){
    const transactionRequest = this.state.transactionRequest
    console.log(transactionRequest)
    return(
      <div>
        <table className="u-full-width">
          <thead>
            <tr>
              <th>Symbol</th>
              <th>Coin</th>
              <th>Time</th>
              <th>Buy Price</th>
              <th>Bought</th>
              <th>Sell Price</th>
              <th>Sold</th>
            </tr>
          </thead>
          {transactionRequest && transactionRequest.map(transaction => {
            {
              const route = transaction.buy > 0 ? '/transaction/edit/buy' : '/transaction/edit/sell'
              return <tbody key={transaction.id}>
                <tr>
                  <td><Link to={{
                    pathname: route,
                    state: {transaction}
                  }}>{transaction.coin.currency}</Link></td>
                  <td><Link to={{
                    pathname: route,
                    state: {transaction}
                  }}>{transaction.coin.full_name}</Link></td>
                  <td><Link to={{
                    pathname: route,
                    state: {transaction}
                  }}>{transaction.timestamp}</Link></td>
                  <td><Link to={{
                    pathname: route,
                    state: {transaction}
                  }}>{transaction.buy || '-'}</Link></td>
                  <td><Link to={{
                    pathname: route,
                    state: {transaction}
                  }}>{transaction.buy_quantity || '-'}</Link></td>
                  <td><Link to={{
                    pathname: route,
                    state: {transaction}
                  }}>{transaction.sell || '-'}</Link></td>
                  <td><Link to={{
                    pathname: route,
                    state: {transaction}
                  }}>{transaction.sell_quantity || '-'}</Link></td>
                </tr>
              </tbody>
            }
          }
          )
          }
        </table>
      </div>
    )
  }
}

export default Transactions

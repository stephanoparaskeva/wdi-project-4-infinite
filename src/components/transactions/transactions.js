import React from 'react'
import { Link } from 'react-router-dom'


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
              <th></th>
              <th></th>
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
              const changeBuy = transaction.buy > 0 ? true : false
              return <tbody key={transaction.id}>
                <tr>
                  <td><Link to={{
                    pathname: '/transaction',
                    state: {transaction, changeBuy, coin: transaction.coin}
                  }}>{changeBuy && <p className="positive">BUY</p> || <p className="negative">SELL</p> }</Link></td>
                  <td><Link to={{
                    pathname: '/transaction',
                    state: {transaction, changeBuy, coin: transaction.coin}
                  }}>{transaction.coin.currency}</Link></td>
                  <td><Link to={{
                    pathname: '/transaction',
                    state: {transaction, changeBuy, coin: transaction.coin}
                  }}>{transaction.coin.full_name}</Link></td>
                  <td><Link to={{
                    pathname: '/transaction',
                    state: {transaction, changeBuy, coin: transaction.coin}
                  }}>{transaction.timestamp}</Link></td>
                  <td><Link to={{
                    pathname: '/transaction',
                    state: {transaction, changeBuy, coin: transaction.coin}
                  }}>{transaction.buy || '-'}</Link></td>
                  <td><Link to={{
                    pathname: '/transaction',
                    state: {transaction, changeBuy, coin: transaction.coin}
                  }}>{transaction.buy_quantity || '-'}</Link></td>
                  <td><Link to={{
                    pathname: '/transaction',
                    state: {transaction, changeBuy, coin: transaction.coin}
                  }}>{transaction.sell || '-'}</Link></td>
                  <td><Link to={{
                    pathname: '/transaction',
                    state: {transaction, changeBuy, coin: transaction.coin}
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

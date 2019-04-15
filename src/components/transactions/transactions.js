import React from 'react'
import { Link } from 'react-router-dom'
import Auth from '../../lib/auth'
import axios from 'axios'
import moment from 'moment'


class Transactions extends React.Component{
  constructor(){
    super()

    this.state = {}

    this.handleDelete = this.handleDelete.bind(this)
  }

  componentDidMount() {
    this.sortByDate()
  }


  sortByDate() {
    const sorted = this.props.transactionRequest.sort((a, b) => {
      if (moment(a.timestamp) > moment(b.timestamp)) return -1
      return 1
    })
    this.setState({transactionRequest: sorted})
  }

  handleDelete(e, id) {
    console.log(this.props)
    e.preventDefault()
    axios.delete(`/api/transactions/${id}`, {
      headers: {Authorization: `Bearer ${Auth.getToken()}`}
    })
      .then(() => {
        const filterDeleted = this.state.transactionRequest.filter(transaction => transaction.id !== id)
        this.setState({transactionRequest: filterDeleted})
      }).then(() => this.props.getTransactionQuantities())
      .catch(err => console.log(err.message))
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
              <th>Symbol</th>
              <th>Coin</th>
              <th>Time</th>
              <th>Buy Price</th>
              <th>Bought</th>
              <th>Sell Price</th>
              <th>Sold</th>
              <th></th>
            </tr>
          </thead>
          {transactionRequest && transactionRequest.map(transaction => {
            {
              const changeBuy = transaction.buy > 0 ? true : false
              const edit = true
              return <tbody key={transaction.id}>
                <tr>
                  <td><Link to={{
                    pathname: '/transaction',
                    state: {transaction, changeBuy, coin: transaction.coin, edit}
                  }}>{changeBuy && <p className="positive">BUY</p> || <p className="negative">SELL</p> }</Link></td>
                  <td><Link to={{
                    pathname: '/transaction',
                    state: {transaction, changeBuy, coin: transaction.coin, edit}
                  }}>{transaction.coin.currency}</Link></td>
                  <td><Link to={{
                    pathname: '/transaction',
                    state: {transaction, changeBuy, coin: transaction.coin, edit}
                  }}>{transaction.coin.full_name}</Link></td>
                  <td><Link to={{
                    pathname: '/transaction',
                    state: {transaction, changeBuy, coin: transaction.coin, edit}
                  }}>{transaction.timestamp}</Link></td>
                  <td><Link to={{
                    pathname: '/transaction',
                    state: {transaction, changeBuy, coin: transaction.coin, edit}
                  }}>{transaction.buy || '-'}</Link></td>
                  <td><Link to={{
                    pathname: '/transaction',
                    state: {transaction, changeBuy, coin: transaction.coin, edit}
                  }}>{transaction.buy_quantity || '-'}</Link></td>
                  <td><Link to={{
                    pathname: '/transaction',
                    state: {transaction, changeBuy, coin: transaction.coin, edit}
                  }}>{transaction.sell || '-'}</Link></td>
                  <td><Link to={{
                    pathname: '/transaction',
                    state: {transaction, changeBuy, coin: transaction.coin, edit}
                  }}>{transaction.sell_quantity || '-'}</Link></td>
                  <td className="delete" onClick={(e) => this.handleDelete(e, transaction.id)}>delete</td>
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

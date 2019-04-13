import React from 'react'
import axios from 'axios'
import moment from 'moment'
import DatePicker from 'react-datepicker'
import 'react-datepicker/dist/react-datepicker.css'

import Auth from '../../lib/auth'

class TransactionForm extends React.Component {
  constructor() {
    super()

    this.state = {
      data: {
        coin_id: '',
        buy: '0',
        buy_quantity: '0',
        sell: '0',
        sell_quantity: '0',
        timestamp: moment().format()
      },
      isHidden: true,
      errors: {}
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleTime = this.handleTime.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.toggleBuy = this.toggleBuy.bind(this)
    this.toggleSell = this.toggleSell.bind(this)
    this.checkTransactions = this.checkTransactions.bind(this)
  }

  componentDidMount() {
    const coin = this.props.location.state.coin.currency
    const data = {...this.state.data}
    data.coin_id = coin
    this.setState({data})
  }

  toggleBuy(e) {
    e.preventDefault()
    const data = {...this.state.data}
    this.setState({isHidden: true, data})
  }

  toggleSell(e) {
    e.preventDefault()
    const data = {...this.state.data}
    this.setState({isHidden: false, data})
  }

  handleChange({ target: {name, value}}) {
    const data = {...this.state.data, [name]: parseFloat(value) || ''}
    const errors = {...this.state.errors, [name]: ''}
    this.setState({ data, errors })
  }

  handleTime(date) {
    const data = {...this.state.data, timestamp: date}
    this.setState({ data })
  }

  checkTransactions() {
    axios.get('/api/transactions')
      .then(res => res.data)
      .then(transactions => transactions.filter(transaction => transaction.coin.currency === this.props.location.state.coin.currency))
      .then(coins => coins.reduce((acc, curr) => acc += curr.buy_quantity - curr.sell_quantity, 0))
      .then(quan => quan > 0 ? true : false)
  }

  handleSubmit(e) {
    e.preventDefault()
    const data = {...this.state.data}
    if (this.checkTransactions()) {
      axios.post('/api/transactions', data, { headers: {Authorization: `Bearer ${Auth.getToken()}`}})
      this.props.history.push('/portfolio')
    }
  }

  render() {
    this.checkTransactions()
    console.log(this.state.data)
    const coin = this.props.location.state.coin
    console.log('coin', coin)
    return(
      <div>
        <p>{coin.currency}/USD</p>
        <button onClick={ this.toggleBuy }>BUY</button>
        <button onClick={ this.toggleSell }>SELL</button>
        {this.state.isHidden &&
        <form onSubmit={ this.handleSubmit } className="buy-form">
          <label>
            Buy Price in USD
            <input
              onChange={ this.handleChange }
              name="buy"
              type="number"
              value={ this.state.data.buy }
            />
          </label>
          <label>
            Amount Bought
            <input
              onChange={ this.handleChange }
              name="buy_quantity"
              type="number"
              value={ this.state.data.buy_quantity }
            />
          </label>
          <label>
            Date
            <DatePicker
              selected={this.state.data.timestamp}
              onChange={this.handleTime}
            />
          </label>
          <button>Add Transaction</button>
        </form>
        }
        {!this.state.isHidden &&
        <form onSubmit={ this.handleSubmit } className="sell-form">
          <label>
            Sell Price in USD
            <input
              onChange={ this.handleChange }
              name="sell"
              type="number"
              value={ this.state.data.sell }
            />
          </label>
          <label>
            Amount Sold
            <input
              onChange={ this.handleChange }
              name="sell_quantity"
              type="number"
              value={ this.state.data.sell_quantity }
            />
          </label>
          <label>
            Date
            <DatePicker
              selected={this.state.data.timestamp}
              onChange={this.handleTime}
            />
          </label>
          <button>Add Transaction</button>
        </form>
        }
      </div>
    )
  }
}

export default TransactionForm

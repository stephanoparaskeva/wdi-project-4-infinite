import React from 'react'
import axios from 'axios'
import moment from 'moment'
import DatePicker from 'react-datepicker'
import 'react-datepicker/dist/react-datepicker.css'

import Auth from '../../lib/auth'
import BuyForm from './buyForm'
import SellForm from './sellForm'

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
        timestamp: moment().format('YYYY-MM-DD')
      },
      date: new Date(),
      isHidden: true,
      errors: {}
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleDate = this.handleDate.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.toggleBuy = this.toggleBuy.bind(this)
    this.toggleSell = this.toggleSell.bind(this)
    this.checkTransactions = this.checkTransactions.bind(this)
  }

  componentDidMount() {
    axios.get('/api/transactions')
      .then(res => {
        return res.data.filter(transaction => {
          return transaction.user.id === Auth.getPayload().sub
        })
      }).then(transactions => this.setState({ transactions }))
    const coin = this.props.location.state.coin.currency
    const data = {...this.state.data}
    data.coin_id = coin
    this.setState({data})
  }

  toggleBuy(e) {
    e.preventDefault()
    const data = {coin_id: this.props.location.state.coin.currency, buy: '0', buy_quantity: '0', sell: '0', sell_quantity: '0', timestamp: moment().format()}
    this.setState({isHidden: true, data})
  }

  toggleSell(e) {
    e.preventDefault()
    const data = {coin_id: this.props.location.state.coin.currency, buy: '0', buy_quantity: '0', sell: '0', sell_quantity: '0', timestamp: moment().format()}
    this.setState({isHidden: false, data})
  }

  handleChange({ target: {name, value}}) {
    const data = {...this.state.data, [name]: parseFloat(value) || ''}
    const errors = {...this.state.errors, [name]: ''}
    this.setState({ data, errors })
  }

  handleDate(date) {
    const data = {...this.state.data, timestamp: moment(date).format('YYYY-MM-DD')}
    this.setState({
      data, date
    })
  }

  checkTransactions(sellQuantity) {
    const filtered = this.state.transactions.filter(transaction => transaction.coin !== null && transaction.coin.currency === this.props.location.state.coin.currency)
    const quantity = filtered.reduce((acc, curr) => acc += curr.buy_quantity - curr.sell_quantity, 0)
    return quantity >= sellQuantity ? true : false
  }

  handleSubmit(e) {
    e.preventDefault()
    const data = {...this.state.data}
    if (this.state.isHidden || this.checkTransactions(this.state.data.sell_quantity)) {
      axios.post('/api/transactions', data, { headers: {Authorization: `Bearer ${Auth.getToken()}`}})
        .then(() => this.props.history.push('/portfolio'))

    }
  }

  render() {
    const coin = this.props.location.state.coin
    const date = this.state.date
    return(
      <div>
        <p>{coin.currency}/USD</p>
        <button onClick={ this.toggleBuy }>BUY</button>
        <button onClick={ this.toggleSell }>SELL</button>
        {this.state.isHidden &&
          <BuyForm
            handleChange={this.handleChange}
            handleSubmit={this.handleSubmit}
            handleDate={this.handleDate}
            data={this.state.data}
            coin={coin}
            date={date}
          />
        }
        {!this.state.isHidden &&
        <SellForm
          handleChange={this.handleChange}
          handleSubmit={this.handleSubmit}
          handleDate={this.handleDate}
          data={this.state.data}
          coin={coin}
          date={date}
        />
        }
      </div>
    )
  }
}

export default TransactionForm

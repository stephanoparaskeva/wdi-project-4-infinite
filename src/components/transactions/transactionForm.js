import React from 'react'
import axios from 'axios'
import moment from 'moment'
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
    const coin = this.props.location.state.coin
    const changeBuy = this.props.location.state.changeBuy
    const edit = this.props.location.state.edit
    if (!changeBuy && edit) {
      this.setState({isHidden: false})
    }
    if (edit) {
      const transaction = this.props.location.state.transaction
      const data = {
        coin_id: transaction.coin.currency,
        buy: transaction.buy || 0,
        buy_quantity: transaction.buy_quantity || 0,
        sell: transaction.sell || 0,
        sell_quantity: transaction.sell_quantity || 0,
        timestamp: moment(transaction.timestamp).format('YYYY-MM-DD')
      }
      this.setState({data})
    } else if (!edit){
      const data = {...this.state.data, buy: coin.price}
      data.coin_id = coin.currency
      this.setState({data})
    }
  }


    getNomicsPrices() {
      return this.props.nomics
    }

    currencyConversion(prices, usersCoins) {
      return prices.reduce((arr, item) => {
        if (Object.keys(usersCoins).includes(item.currency)) {
          arr.push(usersCoins[item.currency] * item.price)
        }
        return arr
      }, []).reduce((acc, i) => acc + i, 0)
    }

    makeUserCoins(res) {
      const filtered = res.filter(coin => coin.coin !== null)
      const buyQuantites = filtered.map(data => ({
        buyQuantity: data.buy_quantity,
        currency: data.coin.currency
      }))
      const sellQuantities = filtered.map(data => ({
        sellQuantity: data.sell_quantity,
        currency: data.coin.currency
      }))

      const totalsArr = buyQuantites.map((transaction, i) => {

        return {
          total: transaction.buyQuantity - sellQuantities[i].sellQuantity,
          currency: transaction.currency
        }
      })

      return totalsArr.reduce((obj, item) => {
        obj[item.currency] = item.total + (obj[item.currency] || 0)
        return obj
      }, {})
    }

    getUserBalanceBuySell(res) {
      return res.reduce((acc, current) => {
        return acc += current.buy*current.buy_quantity - current.sell*current.sell_quantity
      }, 0)
    }

  getTransactionQuantities() {
    axios.get('/api/transactions')
      .then(res => {
        return res.data.filter(transaction => {
          return transaction.user.id === Auth.getPayload().sub
        })
      })
      .then(res => {
        this.setState({ transactionRequest: res })
        return res
      })
      .then(res => {
        const original = this.getUserBalanceBuySell(res)
        this.setState({ original })
        const data = this.makeUserCoins(res)
        const holdings = []
        for (const key in data) {
          const temp = {quantity: data[key], currency: key}
          holdings.push(temp)
        }
        this.setState({holdings})
        return this.makeUserCoins(res)
      })
      .then((userCoins) => {
        return Promise.all([userCoins, this.getNomicsPrices()])
      })
      .then(res => {
        const [ userCoins, prices ] = res
        const balance = this.currencyConversion(prices, userCoins)
        this.setState({ userCoins, balance})
        console.log(balance, 'bal')
        console.log(this.state.original, 'org')
        return balance
      }).then(balance => {
        this.setState({change: balance - this.state.original})
      })
      .then(() => console.log(this.state.change))
  }

  toggleBuy(e) {
    e.preventDefault()
    const coin = this.props.location.state.coin
    const data = {coin_id: coin.currency, buy: coin.price || '0', buy_quantity: '0', sell: '0', sell_quantity: '0', timestamp: moment().format()}
    this.setState({isHidden: true, data})
  }

  toggleSell(e) {
    e.preventDefault()
    const coin = this.props.location.state.coin
    const data = {coin_id: coin.currency, buy: '0', buy_quantity: '0', sell: coin.price || '0', sell_quantity: '0', timestamp: moment().format()}
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

  quantityCheck() {
    return this.state.data.buy_quantity > 0 || this.state.data.sell_quantity > 0
  }

  stopBuyToSell(data) {
    let num = 0
    if (this.state.isHidden && data.sell_quantity !== 0) {
      num ++
    }
    if (!this.state.isHidden && data.buy_quantity !== 0)  {
      num ++
    }
    return num
  }

  handleSubmit(e) {
    e.preventDefault()
    const edit = this.props.location.state.edit
    const transaction = this.props.location.state.transaction
    this.getTransactionQuantities()

    const data = {...this.state.data}
    if (this.stopBuyToSell(data) === 0 && this.quantityCheck() && edit && this.state.isHidden || this.stopBuyToSell(data) === 0 && this.quantityCheck() && edit && this.checkTransactions(this.state.data.sell_quantity)) {
      axios.put(`/api/transactions/${transaction.id}`, data, { headers: {Authorization: `Bearer ${Auth.getToken()}`}})
        .then(() => this.props.history.push('/portfolio'))
    } else if (this.quantityCheck() && !edit && this.state.isHidden || this.quantityCheck() && !edit && this.checkTransactions(this.state.data.sell_quantity)) {
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

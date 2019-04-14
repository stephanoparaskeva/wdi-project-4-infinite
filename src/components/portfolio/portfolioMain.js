import React from 'react'
import axios from 'axios'
import Holdings from './holdings'
import { Link } from 'react-router-dom'

import BalanceGraph from './balanceGraph'
import Pie from './pie'
import Auth from '../../lib/auth'
import numeral from 'numeral'

class Portfolio extends React.Component{
  constructor(){
    super()

    this.state = {}
    this.getNomicsPrices = this.getNomicsPrices.bind(this)
    this.getTransactionQuantities = this.getTransactionQuantities.bind(this)
    this.getUserBalanceBuySell = this.getUserBalanceBuySell.bind(this)
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
        console.log(res)
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
        return balance
      }).then(balance => {
        this.setState({change: balance - this.state.original})
      })
  }
  componentDidMount() {
    this.getTransactionQuantities()
  }

  render(){
    return(
      <div>
        <h3>MAIN PORTFOLIO BALANCE</h3>
        <p>{this.state.balance && numeral(parseFloat(this.state.balance)).format('$0,0.00') || 0}</p>
        <div>{
          this.state.change && this.state.change > 0 && <div className="positive">{numeral(parseFloat(this.state.change)).format('+ $0,0.00') || 0}</div> ||
          this.state.change && this.state.change < 0 && <div className="negative">{numeral(parseFloat(this.state.change)).format('- $0,0.00') || 0}</div>
        }</div>
        <Link to="/coins"><button className="">Add Transaction</button></Link>
        <Link to={'transactions'}><button className="">My Transactions</button></Link>
        {this.state.transactionRequest && <BalanceGraph transactionRequest={this.state.transactionRequest} /> }
        {this.state.holdings &&
          <Holdings nomics={this.props.nomics} holdings={this.state.holdings} />
        }
        <Pie holdings={this.state.holdings}/>
      </div>
    )
  }
}

export default Portfolio

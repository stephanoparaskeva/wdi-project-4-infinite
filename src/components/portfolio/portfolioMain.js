import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
import numeral from 'numeral'
import moment from 'moment'

import Holdings from './holdings'
import Transactions from '../transactions/transactions'
import BalanceGraph from './balanceGraph'
import Auth from '../../lib/auth'
import Common from'../../lib/common'


class Portfolio extends React.Component{
  constructor(){
    super()

    this.state = {
      holdingsToggle: true,
      graphToggle: true
    }

    this.getNomicsPrices = this.getNomicsPrices.bind(this)
    this.getTransactionQuantities = this.getTransactionQuantities.bind(this)
    this.getUserBalanceBuySell = this.getUserBalanceBuySell.bind(this)
    this.holdingsToggle = this.holdingsToggle.bind(this)
    this.checkGraph = this.checkGraph.bind(this)
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
        const sorted = res.sort((a, b) => {
          if (moment(a.timestamp) > moment(b.timestamp)) return 1
          return - 1
        })
        console.log(sorted[sorted.length-1])
        this.setState({ balance: sorted[sorted.length-1].end_of_day_balance})
        this.setState({ transactionRequest: sorted })
        return res
      })
      .then(res => {
        const actual = this.getUserBalanceBuySell(res)
        this.setState({ change: this.state.balance - actual })
        const data = this.makeUserCoins(res)
        const holdings = []
        for (const key in data) {
          const temp = {quantity: data[key], currency: key}
          holdings.push(temp)
        }
        this.setState({holdings})
      })
  }

  holdingsToggle() {
    this.setState({holdingsToggle: !this.state.holdingsToggle})
  }



  checkGraph() {
    const transactionRequest = this.state.transactionRequest
    if(transactionRequest.length >= 2 && !this.isDataOnSameDay() && this.state.holdings && this.state.holdings.length >= 2)
      return true
  }

  isDataOnSameDay() {
    const data = this.state.transactionRequest
    if (data.length === 2) {
      return moment(data[0].timestamp).isSame(moment(data[1].timestamp), 'minute')
    } else {
      return false
    }
  }

  componentDidMount() {
    this.getTransactionQuantities()
  }

  render(){
    const transactionRequest = this.state.transactionRequest
    const holdings = this.state.holdings
    console.log(holdings)
    return(
      <div className="portfolio">
        <div className="row balance">
          <h4>Balance</h4>
          <h3>{this.state.balance && numeral(this.state.balance).format('($ 0.00 a)') || 0}</h3>
          <p className={Common.checkBalanceChange(this.state.change)}>
            {this.state.change ? numeral(this.state.change).format('$ 0,0.00') : '∞'}
          </p>
          <Link to="/coins"><i className="fas fa-plus-circle"></i></Link>
        </div>
        <div className="row balance-graph">
          {transactionRequest && this.checkGraph() ? <BalanceGraph transactionRequest={transactionRequest}/> : null}
        </div>
        <div className="row">
          <div className="row holdings-toggle">
            <button onClick={this.holdingsToggle}>{this.state.holdingsToggle ? 'Transactions' : 'Holdings'}</button>
          </div>
          {holdings && holdings.length > 0 && this.state.holdingsToggle &&
            <div className="row">


              <Holdings nomics={this.props.nomics} holdings={holdings}/>




            </div>
          }
          {transactionRequest && !this.state.holdingsToggle &&
          <div className="row">
            <Transactions nomics={this.props.nomics} transactionRequest={transactionRequest} getTransactionQuantities={this.getTransactionQuantities} />
          </div>
          }
        </div>
      </div>
    )
  }
}

export default Portfolio

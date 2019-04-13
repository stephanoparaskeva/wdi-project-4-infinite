import React from 'react'
import axios from 'axios'
import Holdings from './holdings'
import { Link } from 'react-router-dom'
import BalanceGraph from './balanceGraph'
import Auth from '../../lib/auth'

class Portfolio extends React.Component{
  constructor(){
    super()

    this.state = {}
    this.getNomicsPrices = this.getNomicsPrices.bind(this)
    this.getTransactionQuantities = this.getTransactionQuantities.bind(this)
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
    const buyQuantites = res.map(data => ({
      buyQuantity: data.buy_quantity,
      currency: data.coin.currency
    }))
    const sellQuantities = res.map(data => ({
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

  getTransactionQuantities() {
    axios.get('/api/transactions')
      .then(res => {
        return res.data.filter(transaction => {
          return transaction.user.id === Auth.getPayload().sub
        })
      })
      .then(res => {
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
      })
  }
  componentDidMount() {
    this.getTransactionQuantities()
  }

  render(){
    return(
      <div>
        <h3>MAIN PORTFOLIO BALANCE</h3>
        <p>${this.state.balance && this.state.balance.toFixed(2)}</p>
        <Link to="/coins"><button className="">Add Transaction</button></Link>
        <BalanceGraph />
        {this.state.holdings &&
          <Holdings nomics={this.props.nomics} holdings={this.state.holdings} />
        }
      </div>
    )
  }
}

export default Portfolio

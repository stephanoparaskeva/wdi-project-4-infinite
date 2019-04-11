import React from 'react'
import axios from 'axios'
import Holdings from './holdings'
import BalanceGraph from './balanceGraph'
import Nomics from '../../lib/nomics'
import Auth from '../../lib/auth'


class Portfolio extends React.Component{
  constructor(){
    super()

    this.state = {}
    this.getNomicsPrices = this.getNomicsPrices.bind(this)
    this.getTransactionQuantities = this.getTransactionQuantities.bind(this)
  }

  getNomicsPrices() {
    return axios.get('https://api.nomics.com/v1/currencies/ticker?key=cfa361e67a06d9209da08f36a340410b')
  }

  currencyConversion(prices, usersCoins) {
    return prices.data.reduce((arr, item) => {
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
        console.log(res)
        return res.data
      })
      .then(res => {
        let data = this.makeUserCoins(res)
        var holdings = []
        for (let key in data) {
          let temp = {quantity: data[key], currency: [key]}
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
    console.log(this.state)
    return(
      <div>
        <h3>MAIN PORTFOLIO BALANCE</h3>
        <p>${this.state.balance && this.state.balance}</p>
        <BalanceGraph />
        {this.state.holdings &&
          <Holdings holdings={this.state.holdings} />
        }
      </div>
    )
  }
}

export default Portfolio

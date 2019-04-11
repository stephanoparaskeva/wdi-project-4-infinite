import React from 'react'
import axios from 'axios'

class Portfolio extends React.Component{
  constructor(){
    super()

    this.state = {}
    this.getNomicsPrices = this.getNomicsPrices.bind(this)
    this.getTransactionQuantities = this.getTransactionQuantities.bind(this)
  }

  getNomicsPrices() {
    axios.get('https://api.nomics.com/v1/currencies/ticker?key=cfa361e67a06d9209da08f36a340410b', {
    })
      .then(res => res.data.filter(tick => {
        return Object.keys(this.state.usersCoins).includes(tick.currency)
      }))
      .then(usersTicks => {
        return usersTicks.map(tick => {
          const { usersCoins } = this.state
          return usersCoins[tick.currency] * tick.price
        })
      }).then(currencyConversion => currencyConversion.reduce((acc, current) => {
        return acc + current
      }, 0))
      .then(balance => this.setState({ balance }))
  }

  getTransactionQuantities() {
    axios.get('/api/transactions')
      .then(res => res.data)
      .then(res => {
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
        const usersCoins = totalsArr.reduce((obj, item) => {
          obj[item.currency] = item.total + (obj[item.currency] || 0)
          return obj
        }, {})
        this.setState({usersCoins})
      })

  }
  componentDidMount() {
    this.getNomicsPrices()
    this.getTransactionQuantities()
  }

  render(){
    return(
      <div className="container">
        <div className="row">
          <div className="col-1 test">
            {`Balance $${this.state.balance && this.state.balance}`}
          </div>
        </div>
      </div>
    )
  }
}

export default Portfolio

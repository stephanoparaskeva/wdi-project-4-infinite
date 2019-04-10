import React from 'react'
import axios from 'axios'

class Portfolio extends React.Component{
  constructor(){
    super()

    this.state = {
      user: {
        buyQuantity: [],
        sellQuantity: []
      }
    }
    this.getNomicsPrices = this.getNomicsPrices.bind(this)
    this.getTransactionQuantities = this.getTransactionQuantities.bind(this)
  }

  getNomicsPrices() {
    axios.get('https://api.nomics.com/v1/prices?key=cfa361e67a06d9209da08f36a340410b', {
    })
      .then(res => console.log(res))
  }

  getTransactionQuantities() {
    axios.get('/api/transactions')
      .then(res => res.data)
      .then(res => {
        console.log(res)
        const buyQuantites = res.map(data => ({
          buyQuantity: data.buy_quantity,
          currency: data.coin.currency
        }))
        console.log('buyQuantity', buyQuantites)
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
        // const testArr = totalsArr.filter((item, i) => {
        //   if(item.currency === totalsArr[i].currency) {
        //     return item
        //   }
        // })
        // console.log('testarr', testArr)
        const reduced = totalsArr.reduce((obj, item) => {
          obj[item.currency] = item.total + (obj[item.currency] || 0)
          return obj
        }, {})
        console.log(reduced)
      })

  }
  componentDidMount() {
    this.getNomicsPrices()
    this.getTransactionQuantities()
  }

  render(){
    // console.log(this.state)
    return(
      <div className="container">
        <div className="row">
          <div className="col-1 test">
          hello world
          </div>
        </div>
      </div>
    )
  }
}

export default Portfolio

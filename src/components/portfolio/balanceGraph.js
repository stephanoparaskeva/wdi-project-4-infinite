import React from 'react'
import axios from 'axios'
import moment from 'moment'

class Test extends React.Component{
  constructor(){
    super()
    this.state = {}
    this.sortTransactionTimestamps = this.sortTransactionTimestamps.bind(this)
  }

  sortTransactionTimestamps() {
    axios.get('/api/transactions')
      .then(res => {
        console.log(res)
        return res.data.sort((a, b) => {
          if (moment(a.timestamp) > moment(b.timestamp)) return 1
          return - 1
        })
      })
      .then(sorted => {
        this.setState({dates: [...new Set(sorted.map(item => item.timestamp))]})
        return sorted.reduce((acc, obj) => {
          const key = obj['timestamp']
          if (!acc[key]) {
            acc[key] = []
          }
          acc[key].push(obj)
          return acc
        }, {})
      })
      .then(reduced => Object.values(reduced))
      .then(arrayGroupedByTime => {
        return arrayGroupedByTime.map(transactions => {
          console.log(transactions)
          return transactions.reduce((acc, current) => {
            return acc += current.buy - current.sell
          }, 0)
        })
      })
      .then(daysBalances => {
        return daysBalances.map((balance, i) => {
          if (!i) return balance
          const newBalance =  balance = balance + daysBalances[i - 1]
          daysBalances[i] = newBalance
          return newBalance
        })
      })
      .then(res => console.log(res))
  }

  componentDidMount() {
    this.sortTransactionTimestamps()
  }

  render(){
    console.log(this.state.dates)
    return(
      <div className="container">
        <div className="row">
          <div className="col-1 test">
          </div>
        </div>
      </div>
    )
  }
}

export default Test

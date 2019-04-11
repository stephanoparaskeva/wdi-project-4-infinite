import React from 'react'
import Plot from 'react-plotly.js'
import Auth from '../../lib/auth'
import axios from 'axios'
import moment from 'moment'

class BalanceGraph extends React.Component{
  constructor(){
    super()
    this.state = {
      type: 'scatter',
      mode: 'lines'
    }
    this.sortTransactionTimestamps = this.sortTransactionTimestamps.bind(this)
  }

  sortTransactionTimestamps() {
    axios.get('/api/transactions')
      .then(res => {
        return res.data.filter(transaction => {
          return transaction.user.id === Auth.getPayload().sub
        })
      })
      .then(res => {
        return res.sort((a, b) => {
          if (moment(a.timestamp) > moment(b.timestamp)) return 1
          return - 1
        })
      })
      .then(sorted => {
        this.setState({x: [...new Set(sorted.map(item => item.timestamp))]})
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
          return transactions.reduce((acc, current) => {
            return acc += current.buy - current.sell
          }, 0)
        })
      })
      .then(daysBalances => {
        console.log(daysBalances)
        return daysBalances.map((balance, i) => {
          if (!i) return balance
          const newBalance =  balance = balance + daysBalances[i - 1]
          daysBalances[i] = newBalance
          return newBalance
        })
      })
      .then(res => this.setState({y: res}))
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
            {this.state.x &&
          <Plot
            data={[this.state]}
            layout={this.layout}
          />
            }
          </div>
        </div>
      </div>
    )
  }
}

export default BalanceGraph

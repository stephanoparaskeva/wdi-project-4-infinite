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

    this.layout = {
      font: {
        family: 'Courier New, monospace',
        size: 10,
        color: 'white'
      },
      paper_bgcolor: 'black',
      plot_bgcolor: 'black',
      dragmode: 'zoom',
      margin: {
        r: 10,
        t: 15,
        b: 20,
        l: 15
      },
      showlegend: false,
      xaxis: {
        showgrid: false,
        autorange: true,
        domain: [0, 1],
        type: 'date'
      },
      yaxis: {
        showlegend: false,
        showgrid: false,
        autorange: true,
        domain: [0, 1],
        type: 'linear'
      },
      autosize: true
    }
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
    console.log(this.layout, 'layout')
    return(
      <div>
        <div>
          <div>
            {this.state.x &&
          <Plot
            useResizeHandler
            style={{height: '100%', width: '100%'}}
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

import React from 'react'
import Plot from 'react-plotly.js'
import moment from 'moment'

class BalanceGraph extends React.Component{
  constructor(){
    super()
    this.state = {
      type: 'scatter',
      mode: 'lines',
      fill: 'tonexty'
    }
    this.sortTransactionTimestamps = this.sortTransactionTimestamps.bind(this)

    this.layout = {
      font: {
        family: 'arial, monospace',
        size: 10,
        color: 'white'
      },
      paper_bgcolor: '#274060',
      plot_bgcolor: '#274060',
      dragmode: 'zoom',
      margin: {
        r: 15,
        t: 15,
        b: 35,
        l: 25
      },
      showlegend: false,
      xaxis: {
        showgrid: false,
        autorange: true,
        domain: [0, 1],
        type: 'date',
        zeroline: false
      },
      yaxis: {
        showlegend: false,
        showgrid: false,
        autorange: true,
        domain: [0, 1],
        type: 'linear',
        zeroline: false
      },
      autosize: true
    }
  }

  sortTransactionTimestamps() {
    const sorted = this.props.transactionRequest.sort((a, b) => {
      if (moment(a.timestamp) > moment(b.timestamp)) return 1
      return - 1
    })
    this.setState({x: [...new Set(sorted.map(item => item.timestamp))]})
    const reduced = sorted.reduce((acc, obj) => {
      const key = obj['timestamp']
      if (!acc[key]) {
        acc[key] = []
      }
      acc[key].push(obj)
      return acc
    }, {})
    const values = Object.values(reduced)
    const totalBalancePerDay = values.map(transactions => {
      return transactions.reduce((acc, current) => {
        return acc += current.buy*current.buy_quantity - current.sell*current.sell_quantity
      }, 0)
    })
    const y = totalBalancePerDay.map((balance, i) => {
      if (!i) return balance
      const newBalance =  balance = balance + totalBalancePerDay[i - 1]
      totalBalancePerDay[i] = newBalance
      return newBalance
    })
    this.setState({y})
  }

  componentDidMount() {
    this.sortTransactionTimestamps()
  }

  render(){
    console.log('rendered graph')
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

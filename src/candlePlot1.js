import React from 'react'
import Plot from 'react-plotly.js'
import axios from 'axios'
import moment from 'moment'

class CandlePlot1 extends React.Component {
  constructor() {
    super()

    this.state = {
      x: [],
      close: [],
      decreasing: {line: {color: 'red'}},
      increasing: {line: {color: 'green'}},
      high: [],
      low: [],
      open: [],
      type: 'candlestick',
      xaxis: 'x',
      yaxis: 'y'
    }

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
        b: 10,
        l: 35
      },
      showlegend: false,
      xaxis: {
        showgrid: false,
        autorange: true,
        domain: [0, 1],
        range: ['2017-01-03 12:00', '2017-02-15 12:00'],
        type: 'date'
      },
      yaxis: {
        showlegend: false,
        showgrid: false,
        autorange: true,
        domain: [0, 1],
        range: [114.609999778, 137.410004222],
        type: 'linear'
      }
    }
  }

  componentDidMount() {
    axios
      .get('/api/nomics/candles', {
        params: {
<<<<<<< HEAD
          currency: 'USDT',
          start: moment().subtract(365, 'days').format(),
=======
          currency: 'XRP',
          start: moment().subtract(1000, 'days').format(),
>>>>>>> development
          end: moment().format()
        }
      })
      .then(res => res.data.map(day => {
        this.setState({
          x: [...this.state.x, day.timestamp.slice(0, 10)],
          close: [...this.state.close, parseFloat(day.close)],
          high: [...this.state.high, parseFloat(day.high)],
          low: [...this.state.low, parseFloat(day.low)],
          open: [...this.state.open, parseFloat(day.open)]
        })
      }))
      .catch(err => console.log(err))
  }


  render() {
    return (
      <div>
        {this.state.x &&
        <Plot
          data={[this.state]}
          layout={this.layout}
        />
        }
      </div>
    )
  }
}

export default CandlePlot1

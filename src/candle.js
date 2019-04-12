import React from 'react'
import Plot from 'react-plotly.js'
import axios from 'axios'
import moment from 'moment'

class Candle extends React.Component {
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
    this.getCandleData = this.getCandleData.bind(this)
  }

  getCandleData() {
    axios
      .get('/api/nomics/candles', {
        params: {
          currency: this.props.coin,
          start: moment().subtract(parseInt(this.props.time), 'days').format(),
          end: moment().format()
        }
      })
      .then(res => res.data.map(day => {
        let data = {
          x: [],
          close: [],
          high: [],
          low: [],
          open: []
        }
        return data = {
          x: [...data.x, day.timestamp.slice(0, 10)],
          close: [...data.close, parseFloat(day.close)],
          high: [...data.high, parseFloat(day.high)],
          low: [...data.low, parseFloat(day.low)],
          open: [...data.open, parseFloat(day.open)],
          decreasing: {line: {color: 'red'}},
          increasing: {line: {color: 'green'}},
          type: 'candlestick',
          xaxis: 'x',
          yaxis: 'y'
        }
      })).then(data => this.setState({data}))
      .catch(err => console.log(err))
  }

  componentDidMount() {
    this.getCandleData()
  }



  render() {
    console.log('rerender')
    return (
      <div>
        {this.state.data &&
        <Plot
          data={this.state.data}
          layout={this.layout}
        />
        }
      </div>
    )
  }
}

export default Candle

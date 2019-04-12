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
      yaxis: 'y',
      time: '30'
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
    this.handleTime = this.handleTime.bind(this)
  }

  handleTime(e) {
    this.setState({time: e.target.value})
  }

  componentDidMount() {
    axios
      .get('/api/nomics/candles', {
        params: {
          currency: this.props.coin,
          start: moment().subtract(parseInt(this.state.time), 'days').format(),
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
        <div className="row">
          <button className="three columns" onClick={this.handleTime} value="7">1w</button>
          <button className="three columns" onClick={this.handleTime} value="30">1m</button>
          <button className="three columns" onClick={this.handleTime} value="365">1y</button>
        </div>
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

export default Candle

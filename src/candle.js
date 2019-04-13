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
        family: 'arial, monospace',
        size: 10,
        color: 'white'
      },
      paper_bgcolor: '#274060',
      plot_bgcolor: '#274060',
      dragmode: 'zoom',
      margin: {
        r: 10,
        t: 15,
        b: 35,
        l: 35
      },
      showlegend: false,
      xaxis: {
        showgrid: false,
        autorange: true,
        domain: [0, 1],
        rangeslider: {visible: false},
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
    this.handleTime = this.handleTime.bind(this)
    this.getCandleData = this.getCandleData.bind(this)
  }

  handleTime(e) {
    this.getCandleData(e.target.value)
  }


  getCandleData(time) {
    axios
      .get('/api/nomics/candles', {
        params: {
          currency: this.props.coin,
          start: moment().subtract(parseInt(time), 'days').format(),
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
    this.getCandleData('30')
  }



  render() {
    return (
      <div>
        <div className="row">
          <button className="three columns" onClick={this.handleTime} value="7">1w</button>
          <button className="three columns" onClick={this.handleTime} value="30">1m</button>
          <button className="three columns" onClick={this.handleTime} value="365">1y</button>
          <button className="three columns" onClick={this.handleTime} value="1825">5y</button>
        </div>
        {this.state.x &&
        <Plot
          useResizeHandler
          style={{height: '100%', width: '100%'}}
          data={this.state.data}
          layout={this.layout}
        />
        }
      </div>
    )
  }
}

export default Candle

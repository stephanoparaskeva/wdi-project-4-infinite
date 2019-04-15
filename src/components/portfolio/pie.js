import React from 'react'
import Plot from 'react-plotly.js'

class Pie extends React.Component {
  constructor(){
    super()

    this.state = {
      colors: []
    }
  }

  getQuantity() {
    const quantity = this.props.holdings.map(coin => {
      return coin.quantity
    })
    return quantity
  }

  getCurrency() {
    const currency = this.props.holdings.map(coin => {
      return coin.currency
    })
    return currency
  }

  render() {
    if(!this.props.holdings) return null
    return (
      <Plot
        useResizeHandler
        style={{height: '100%', width: '100%'}}
        data={[
          {
            values: this.getQuantity(),
            marker: {
              colors: [
                '#1f4c6c',
                '#929292',
                '#6f6666bf',
                '#212933',
                '#4e516fbf',
                '#929292',
                'rgb(0, 0, 0)',
                'rgb(0, 0, 0)'
              ]
            },
            labels: this.getCurrency(),
            type: 'pie',
            domain: {column: 0},
            name: 'Holdings',
            hoverinfo: 'label+value'
          }
        ]}
        layout={
          {
            width: 500,
            height: 500,
            font: {color: 'white'},
            paper_bgcolor: '#1e2125' }
        }
      />
    )
  }
}

export default Pie

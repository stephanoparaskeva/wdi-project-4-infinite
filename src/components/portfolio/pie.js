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
        data={[
          {
            values: this.getQuantity(),
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
            title: 'Holdings',
            font: {color: 'white'},
            paper_bgcolor: '#1e2125' }
        }
      />
    )
  }
}

export default Pie

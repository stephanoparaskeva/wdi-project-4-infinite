import React from 'react'
import Candle from './candle'

class Coin extends React.Component {
  constructor() {
    super()

    this.state = {}
  }

  render() {
    return(
      <div>
        <Candle />
      </div>
    )
  }
}

export default Coin

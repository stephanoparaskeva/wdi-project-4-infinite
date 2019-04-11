import React from 'react'
import { Link } from 'react-router-dom'
import Ticker from './ticker'

class Header extends React.Component {
  constructor() {
    super()

    this.state = {}
  }

  render(){
    return(
      <div>
        <Ticker />
        <h1>Crypto</h1>
      </div>
    )
  }
}

export default Header

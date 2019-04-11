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
        <h1>Crypto</h1>
        <Ticker />
      </div>
    )
  }
}

export default Header

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
      <div className="header">
        <Ticker nomics={this.props.nomics}/>
        <span><Link to='/'> index </Link></span>
        <span><Link to='/register'> register </Link></span>
        <span><Link to='/portfolio'> portfolio </Link></span>
      </div>
    )
  }
}

export default Header

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
        <h1><Link to='/'>Crypto</Link></h1>
        <Link to='/register'>Register</Link>
        <Link to='/portfolio'>Portfolio</Link>
      </div>
    )
  }
}

export default Header

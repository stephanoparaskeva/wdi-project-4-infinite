import React from 'react'
import { Link, withRouter } from 'react-router-dom'
import Ticker from './ticker'
import Auth from '../lib/auth'

class Header extends React.Component {
  constructor() {
    super()

    this.state = {}
    this.logout = this.logout.bind(this)
  }

  logout() {
    Auth.logout()
    this.props.history.push('/')
  }

  render(){
    return(
      <div className="header">
        <Ticker nomics={this.props.nomics}/>
        <h1><Link to='/'>INFINITY</Link></h1>
        {!Auth.isAuthenticated() && <Link to='/register'><h5>Register</h5></Link>}
        {!Auth.isAuthenticated() && <Link to='/login'><h5>Login</h5></Link>}
        {Auth.isAuthenticated() &&  <Link to='/portfolio'><h5>Portfolio</h5></Link>}
        {Auth.isAuthenticated() && <Link to='/' onClick={this.logout}><h5>Logout</h5></Link>}
      </div>
    )
  }
}

export default withRouter(Header)

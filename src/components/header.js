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
      <ul className="header">
        <li><Link to='/'><i className="fas fa-globe"></i></Link></li>
        {Auth.isAuthenticated() && <li><Link to='/portfolio'><i className="fas fa-chart-line"></i></Link></li>}
        <li className="logo"><Link to='/'><i className="fas fa-infinity"></i></Link></li>
        {!Auth.isAuthenticated() && <li><Link to='/register'><p>Register</p></Link></li>}
        {!Auth.isAuthenticated() && <li><Link to='/login'><p>Login</p></Link></li>}
        {Auth.isAuthenticated() && <Link to='/' onClick={this.logout}><p>Logout</p></Link>}
      </ul>
    )
  }
}

export default withRouter(Header)

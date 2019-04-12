import React from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'
import Auth from '../../lib/auth'

class Register extends React.Component {
  constructor() {
    super()

    this.state = {
      data: {
        username: '',
        email: '',
        password: '',
        password_confirmation: ''
      },
      errors: {}
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleChange({ target: {name, value}}) {
    const data ={...this.state.data, [name]: value}
    const errors = {...this.state.errors, [name]: ''}
    this.setState({ data, errors })
  }

  handleSubmit(e) {
    e.preventDefault()
    axios.post('/api/register', this.state.data)
      .then(res => {
        console.log(res)
        Auth.setToken(res.data.token)
        this.props.history.push('/login')
      })
      .catch(err => console.log(err))
  }

  render() {
    return(
      <div className="container">
        <h2>Register</h2>
        <form onSubmit={ this.handleSubmit }>
          <div className="row">
            <div className="six columns">
              <label htmlFor="username">Username</label>
              <input
                className="u-full-width"
                onChange={ this.handleChange }
                name="username"
                type="text"
                value={ this.state.data.username }
                id="username"
              />
              <label htmlFor="email">Email</label>
              <input
                className="u-full-width"
                onChange={ this.handleChange }
                name="email"
                type="text"
                value={ this.state.data.email }
                id="email"
              />
            </div>
            <div className="six columns">
              <label htmlFor="password">Password</label>
              <input
                className="u-full-width"
                onChange={ this.handleChange }
                type="password"
                name="password"
                value={ this.state.data.password }
                id="password"
              />
              <label htmlFor="passwordConfirmation">Password Confirmation</label>
              <input
                className="u-full-width"
                onChange={ this.handleChange }
                type="password"
                name="password_confirmation"
                value={ this.state.data.password_confirmation }
                id="passwordConfirmation"
              />
            </div>
            <div className="row">
              <button className="six columns">Register</button>
              <p className="six columns">Already Registered? <Link to='/login'>Login Here</Link></p>
            </div>
          </div>
        </form>
      </div>
    )
  }
}

export default Register

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
        passwordConfirmation: ''
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
        Auth.setToken(res.data.token)
        this.props.history.push('/login')
      })
      .catch(err => console.log(err))
  }

  render() {
    return(
      <div>
        <h2>Register</h2>
        <form onSubmit={ this.handleSubmit }>
          <label>
            <span>Username</span>
            <input
              onChange={ this.handleChange }
              name="username"
              value={ this.state.data.username }
            />
          </label>
          <label>
            <span>Email</span>
            <input
              onChange={ this.handleChange }
              name="email"
              value={ this.state.data.email }
            />
          </label>
          <label>
            <span>Password</span>
            <input
              onChange={ this.handleChange }
              type="password"
              name="password"
              value={ this.state.data.password }
            />
          </label>
          <label>
            <span>Password Confirmation</span>
            <input
              onChange={ this.handleChange }
              type="password"
              name="passwordConfirmation"
              value={ this.state.data.passwordConfirmation }
            />
          </label>
          <button className="button pad-top">Register</button>
        </form>
        <p>Already Registered? <Link to='/login'>Login Here</Link></p>
      </div>
    )
  }
}

export default Register

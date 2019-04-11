import React from 'react'

class TransactionForm extends React.Component {
  constructor() {
    super()

    this.state = {
      data: {
        coin: '',
        buy: '',
        buy_quantity: '',
        sell: '',
        sell_quantity: '',
        timestamp: ''
      },
      errors: {}
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  componentDidMount() {
    const theCoinCurrency = this.props.location.state.coin.currency
    const data = {...this.state.data}
    data.coin = theCoinCurrency
    this.setState({data})
  }

  handleChange({ target: {name, value}}) {
    const data = {...this.state.data, [name]: value}
    const errors = {...this.state.errors, [name]: ''}
    this.setState({ data, errors })
  }

  handleSubmit(e) {
    e.preventDefault()
    console.log(this.state.data)
  }

  render() {
    const coin = this.props.location.state.coin
    return(
      <div>
        <p>Add {coin.currency}</p>
        <form onSubmit={ this.handleSubmit }>
          <label>
            Buy Price in USD
            <input
              onChange={ this.handleChange }
              name="buy"
              type="number"
              value={ this.state.data.buy }
            />
          </label>
          <label>
            Amount Bought
            <input
              onChange={ this.handleChange }
              name="buy_quantity"
              type="number"
              value={ this.state.data.buy_quantity }
            />
          </label>
          <button>Add Transaction</button>
        </form>
      </div>
    )
  }
}

export default TransactionForm

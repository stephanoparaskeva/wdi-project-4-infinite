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
      isHidden: true,
      errors: {}
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.toggleBuy = this.toggleBuy.bind(this)
    this.toggleSell = this.toggleSell.bind(this)
  }

  componentDidMount() {
    const theCoinCurrency = this.props.location.state.coin.currency
    const data = {...this.state.data}
    data.coin = theCoinCurrency
    this.setState({data})
  }

  toggleBuy(e) {
    e.preventDefault()
    const data = {...this.state.data}
    this.setState({isHidden: true, data})
  }

  toggleSell(e) {
    e.preventDefault()
    const data = {...this.state.data}
    this.setState({isHidden: false, data})
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
        <p>{coin.currency}/USD</p>
        <button onClick={ this.toggleBuy }>BUY</button>
        <button onClick={ this.toggleSell }>SELL</button>
        {this.state.isHidden &&
        <form onSubmit={ this.handleSubmit } className="buy-form">
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
          <label>
            Time and Date
            <input
              onChange={ this.handleChange }
              name="timestamp"
              type="number"
              value={ this.state.data.timestamp }
            />
          </label>
          <button>Add Transaction</button>
        </form>
        }
        {!this.state.isHidden &&
        <form onSubmit={ this.handleSubmit } className="sell-form">
          <label>
            Sell Price in USD
            <input
              onChange={ this.handleChange }
              name="sell"
              type="number"
              value={ this.state.data.sell }
            />
          </label>
          <label>
            Amount Sold
            <input
              onChange={ this.handleChange }
              name="sell_quantity"
              type="number"
              value={ this.state.data.sell_quantity }
            />
          </label>
          <label>
            Time and Date
            <input
              onChange={ this.handleChange }
              name="timestamp"
              type="number"
              value={ this.state.data.timestamp }
            />
          </label>
          <button>Add Transaction</button>
        </form>
        }
      </div>
    )
  }
}

export default TransactionForm

import React from 'react'
import DatePicker from 'react-datepicker'

class BuyForm extends React.Component {
  constructor() {
    super()

    this.state = {}
  }

  render() {
    return(
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
          Date
          <DatePicker
            selected={this.state.date}
            onChange={this.handleDate}
            placeholderText="Date..."
          />
        </label>
        <button>Add Transaction</button>
      </form>
    )
  }
}

export default BuyForm

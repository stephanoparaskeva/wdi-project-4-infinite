import React from 'react'
import DatePicker from 'react-datepicker'

class SellForm extends React.Component {
  constructor() {
    super()

    this.state = {}
  }

  render() {
    return(
      <form onSubmit={ this.handleSubmit } className="sell-form">
        <label>
          Buy Price in USD
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

export default SellForm

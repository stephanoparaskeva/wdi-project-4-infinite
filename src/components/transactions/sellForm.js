import React from 'react'
import DatePicker from 'react-datepicker'

class SellForm extends React.Component {
  constructor() {
    super()

    this.state = {}
  }

  render() {
    return(
      <form onSubmit={ this.props.handleSubmit } className="sell-form">
        <label>
          Sell Price in USD
          <input
            onChange={ this.props.handleChange }
            name="sell"
            type="number"
            value={ this.props.data.sell || 0}
          />
        </label>
        <label>
          Amount Sold
          <input
            onChange={ this.props.handleChange }
            name="sell_quantity"
            type="number"
            value={ this.props.data.sell_quantity || 0}
          />
        </label>
        <label>
          Date
          <DatePicker
            selected={this.props.date}
            onChange={this.props.handleDate}
            placeholderText="Date..."
          />
        </label>
        <button>Add Transaction</button>
      </form>
    )
  }
}

export default SellForm

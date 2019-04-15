import React from 'react'
import DatePicker from 'react-datepicker'

class BuyForm extends React.Component {
  constructor() {
    super()

    this.state = {}
  }

  render() {
    return(
      <form onSubmit={ this.props.handleSubmit } className="buy-form">
        <label>
          Buy Price in USD
          <input
            onChange={ this.props.handleChange }
            name="buy"
            type="number"
            value={ this.props.data.buy || ''}
          />
        </label>
        <label>
          Amount Bought
          <input
            onChange={ this.props.handleChange }
            name="buy_quantity"
            type="number"
            value={ this.props.data.buy_quantity || '' }
          />
        </label>
        <label>
          Date
          <DatePicker
            selected={this.props.date}
            onChange={this.props.handleDate}
            placeholderText="Date..."
            value={ this.props.data.timestamp || '' }
          />
        </label>
        <button>Add Transaction</button>
      </form>
    )
  }
}

export default BuyForm

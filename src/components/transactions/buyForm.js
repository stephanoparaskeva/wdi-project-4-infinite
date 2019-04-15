import React from 'react'
import DatePicker from 'react-datepicker'

class BuyForm extends React.Component {
  constructor() {
    super()

    this.state = {}
  }

  render() {
    return(
      <div className="transaction">
        <form onSubmit={ this.props.handleSubmit }>
          <div className="row">
            <div className="six columns">
              <label htmlFor="buy">Buy Price</label>
              <input
                onChange={ this.props.handleChange }
                name="buy"
                type="number"
                value={ this.props.data.buy || 0}
              />
              <div className="six columns">
                <label htmlFor="number">Number of Coins</label>
                <input
                  onChange={ this.props.handleChange }
                  name="buy_quantity"
                  type="number"
                  value={ this.props.data.buy_quantity || 0 }
                />
              </div>
            </div>
            <label>
              Date
              <DatePicker
                selected={this.props.date}
                onChange={this.props.handleDate}
                placeholderText="Date..."
              />
            </label>
            <button>Add Transaction</button>
          </div>
        </form>
      </div>
    )
  }
}

export default BuyForm

import React from 'react'
import DatePicker from 'react-datepicker'

class BuyForm extends React.Component {
  constructor() {
    super()

    this.state = {}
  }

  render() {
    console.log(this.props.data, 'buy')
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
                value={ this.props.data.buy || ''}
              />
              <div className="six columns">
                <label htmlFor="number">Number of Coins</label>
                <input
                  onChange={ this.props.handleChange }
                  name="buy_quantity"
                  type="number"
                  value={ this.props.data.buy_quantity || '' }
                />
              </div>
            </div>
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
          </div>
        </form>
      </div>
    )
  }
}

export default BuyForm

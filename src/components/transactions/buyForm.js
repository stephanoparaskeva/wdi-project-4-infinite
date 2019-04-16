import React from 'react'
import DatePicker from 'react-datepicker'
import moment from 'moment'

class BuyForm extends React.Component {
  constructor() {
    super()

    this.state = {}
  }

  render() {
    console.log(this.props.data, 'buy')
    return(
      <div className="container transaction">
        <form onSubmit={ this.props.handleSubmit }>
          <div className="row">
            <div className="six columns">
              <label htmlFor="buy">Buy Price</label>
              <input
                className="u-full-width"
                onChange={ this.props.handleChange }
                name="buy"
                type="number"
                value={ parseFloat(this.props.data.buy) || ''}
              />
            </div>
            <div className="six columns">
              <label htmlFor="buy_quantity">Number of Coins</label>
              <input
                className="u-full-width"
                onChange={ this.props.handleChange }
                name="buy_quantity"
                type="number"
                value={ parseFloat(this.props.data.buy_quantity) || '' }
              />
            </div>
          </div>
          <div className="row">
            <label htmlFor="date">Date</label>
            <button
              className="twelve columns"
              onClick={this.props.toggleCalendar}>
              {moment(this.props.data.timestamp).format('DD-MM-YYYY')}
            </button>
            { this.props.calenderOpen && (
              <DatePicker
                name="date"
                selected={this.props.date}
                onChange={this.props.handleDate}
                value={ this.props.data.timestamp || '' }
                isClearable={true}
                timeIntervals={60}
                showTimeSelect
                onClickOutside={this.props.toggleCalendar}
                withPortal
                inline
              />
            )}
          </div>
          <div className="row">
            <div className="twelve columns">
              <button className="u-full-width">Add Transaction</button>
            </div>
          </div>
        </form>
      </div>
    )
  }
}

export default BuyForm

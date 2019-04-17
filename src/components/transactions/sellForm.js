import React from 'react'
import DatePicker from 'react-datepicker'
import moment from 'moment'

class SellForm extends React.Component {
  constructor() {
    super()

    this.state = {}
  }

  render() {
    return(
      <div className="container transactions">
        <form onSubmit={ this.props.handleSubmit }>
          <div className="row">
            <div className="six columns">
              <label htmlFor="sell">Sell Price</label>
              <input
                className="u-full-width"
                onChange={ this.props.handleChange }
                name="sell"
                type="number"
                value={ parseFloat(this.props.data.sell) || ''}
              />
            </div>
            <div className="six columns">
              <label htmlFor="sell_quantity">Number of Coins</label>
              <input
                className="u-full-width"
                onChange={ this.props.handleChange }
                name="sell_quantity"
                type="number"
                value={ parseFloat(this.props.data.sell_quantity) || '' }
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
                withPortal
                showTimeSelect
                onClickOutside={this.props.toggleCalendar}
                inline
                calendarClassName="calendar"
              />
            )}
          </div>
          <div className="row">
            <div className="twelve columns">
              <button className="u-full-width sell">Add Transaction</button>
            </div>
          </div>
        </form>
      </div>
    )
  }
}

export default SellForm

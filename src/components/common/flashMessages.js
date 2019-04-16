import React from 'react'
import Flash from '../../lib/flash'

class FlashMessages extends React.Component {
  constructor() {
    super()

    this.state = { messages: null }
  }

  componentDidUpdate() {
    const messages = Flash.getMessages()
    if (!messages) return false

    this.setState({ messages })

    setTimeout(() => this.setState({ messages: null}), 400)
  }

  render() {
    return (

      <div>
        {this.state.messages &&
          Object.keys(this.state.messages).map(type => (
            <div key={type} className={`notification is-${type}`}>
              <div className="container">
                {this.state.messages[type]}
              </div>
            </div>
          ))
        }
      </div>
    )
  }
}

export default FlashMessages

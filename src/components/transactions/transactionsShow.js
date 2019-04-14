import React from 'react'

class Transactions extends React.Component{
  constructor(){
    super()

    this.state = {}
  }

  getInitialState() {
    const data = this.props.data
    this.setState(data)
  }

  componentDidMount() {
    this.getInitialState()
  }

  render(){
    console.log(this.props)
    return(
      <div>
        <h2>Transactions</h2>
      </div>
    )
  }
}

export default Transactions

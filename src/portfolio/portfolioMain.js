import React from 'react'
import axios from 'axios'

class Portfolio extends React.Component{
  constructor(){
    super()

    this.state = {
      
    }

    this.getPrice = this.getPrice.bind(this)
  }

  getPrice() {
    axios.get('https://api.nomics.com/v1/prices?key=cfa361e67a06d9209da08f36a340410b', {
      params: {

      }
    })
      .then(res => console.log(res))
  }

  componentDidMount() {
    this.getPrice()
  }

  render(){
    return(
      <div>
          helloworld
      </div>
    )
  }
}

export default Portfolio

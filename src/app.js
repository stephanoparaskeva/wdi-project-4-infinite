import React from 'react'
import ReactDOM from 'react-dom'
import axios from 'axios'

import CandlePlot1 from './candlePlot1'


class App extends React.Component {
  constructor(){
    super()

    this.state = {}
  }
  componentDidMount() {
    axios
      .get('/api/transactions')
      .then(res => console.log(res))
  }

  render() {
    return(
      <div>
        <CandlePlot1 />
      </div>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)

export default App

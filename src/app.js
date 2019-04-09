import React from 'react'
import ReactDOM from 'react-dom'
import axios from 'axios'

import Graph2 from './graph2'


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
        <Graph2 />
      </div>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)

export default App

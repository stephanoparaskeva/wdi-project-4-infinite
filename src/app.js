import React from 'react'
import ReactDOM from 'react-dom'
import axios from 'axios'


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
      <div>Hello World</div>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)

export default App

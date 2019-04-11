import React from 'react'
import ReactDOM from 'react-dom'
import axios from 'axios'

import './styles/main.scss'

import CandlePlot1 from './candlePlot1'
import Ticker from './components/ticker'
import CoinIndex from './components/coinIndex'
import Portfolio from './components/portfolio/portfolioMain'
import Test from './components/portfolio/balanceGraph'


class App extends React.Component {
  constructor(){
    super()

    this.state = {}
  }
  // componentDidMount() {
  //   axios
  //     .get('/api/transactions')
  //     .then(res => console.log(res))
  // }

  render() {
    return(
      <div>
        <Portfolio />
        <CoinIndex />
        <Test />
      </div>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)

export default App

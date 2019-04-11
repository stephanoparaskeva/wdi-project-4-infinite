import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import axios from 'axios'
import Nomics from './lib/nomics'

import './styles/main.scss'

import Header from './components/header'
import Candle from './candle'
import CoinIndex from './components/coinIndex'
import Portfolio from './components/portfolio/portfolioMain'
import Test from './components/portfolio/balanceGraph'


class App extends React.Component {
  constructor(){
    super()

    this.state = {}
  }

  componentDidMount() {
  }

  render() {
    return(
      <BrowserRouter>
        <div className="container">
          <Header />
          <Candle />
          <Portfolio />
          <CoinIndex />
        </div>
      </BrowserRouter>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)

export default App

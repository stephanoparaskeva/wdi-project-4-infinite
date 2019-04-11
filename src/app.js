import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import axios from 'axios'

import './styles/main.scss'

import Header from './components/header'
import CandlePlot1 from './candlePlot1'
import CoinIndex from './components/coinIndex'
import Portfolio from './components/portfolio/portfolioMain'


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
        <Header />
        <CoinIndex />
      </div>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)

export default App

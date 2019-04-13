import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import axios from 'axios'
import Nomics from './lib/nomics'

import './styles/main.scss'

import Header from './components/header'
import Candle from './candle'
import CoinIndex from './components/coinIndex'
import CoinShow from './components/coinShow'
import Portfolio from './components/portfolio/portfolioMain'
import PortfolioTransaction from './components/portfolio/portfolioTransaction'
import TransactionForm from './components/transactions/transactionForm'
import Register from './components/user/register'
import Login from './components/user/login'
import Footer from './components/footer'
import About from './components/about'
import Test from './components/portfolio/balanceGraph'


class App extends React.Component {
  constructor(){
    super()

    this.state = {}

    this.attachCoinToNomics = this.attachCoinToNomics.bind(this)
  }

  componentDidMount() {
    axios.get('/api/nomics/tickers')
      .then(res => this.setState({nomics: res}))
      .then(() => {
        axios.get('/api/coins')
          .then(res => this.setState({coinData: res.data})).then(() => {
            const nomics = this.attachCoinToNomics()
            this.setState({nomics2: nomics})
          })
      })
  }

  attachCoinToNomics() {
    const coinLookup = this.state.coinData.reduce((obj, current) => {
      obj[current.currency] = current.url
      obj[`${current.currency}2`] = current.full_name
      return obj
    }, {})
    console.log(coinLookup)
    const filtered = this.state.nomics.data.filter(nomic => Object.keys(coinLookup).includes(nomic.currency))
    return filtered.map(item => ({...item, image_url: coinLookup[item.currency], full_name: coinLookup[`${item.currency}2`]}))
  }

  render() {
    return(
      <BrowserRouter>
        {this.state.nomics2 && <Header nomics={this.state.nomics2}/>}
        <div className="content container u-full-width">
          {this.state.nomics2 &&
          <Switch>
            <Route path="/portfolio" render={() => {
              return <Portfolio nomics={this.state.nomics2} coinData={this.state.coinData} />
            }} />
            <Route path='/coins' render={() => {
              return <PortfolioTransaction nomics={this.state.nomics2} />
            }} />
            <Route path='/coin' component={ CoinShow } />
            <Route path='/transactionform' component={ TransactionForm } />
            <Route path='/register' component={ Register } />
            <Route path='/login' component={ Login } />
            <Route path='/about' component={ About } />
            <Route path="/" render={() => {
              return <CoinIndex nomics={this.state.nomics2} />
            }} />
          </Switch>
          }
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

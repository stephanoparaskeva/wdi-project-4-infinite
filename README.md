# General Assembly WDI Project 4: Flask + React App
## Infinite
[Deployed project](https://crypto-infinite.herokuapp.com)

![](https://media.giphy.com/media/llCNvZSV4KK7NksgdQ/giphy.gif)
___
### Overview:
A cryptocurrency portfolio tracker with real-time price change data and candle graphs. The user can make transactions, see their balance and a graph of their balance over time based on the coins they own.
___
### Timeframe & Team:
    8 days, team of 2
### The Brief:

* **Build a full-stack application** by making your own backend and your own front-end.
* **Use a Python Flask API** to serve your data from a PostgreSQL database.
* **Consume your API with a separate front-end** built with React.
* **Be a complete product** which most likely means multiple relationships and CRUD functionality for at least a couple of models.
* **Implement thoughtful user stories/wireframes** that are significant enough to help you know which features are core MVP and which you can cut.
* **Have a visually impressive design** to kick your portfolio up a notch and have something to wow future clients & employers. **ALLOW** time for this.
* **Be deployed online** so it's publicly accessible.

### Technologies:

* JavaScript
* Python
* React
* Flask
* PostgreSQL
* CSS
* SASS
* Skeleton.css
* HTML
* Axios
* Plotly.js
* Slack
* Git
* GitHub
* Heroku
* Yarn
* pip3
* Bash


### Approach:

Previously I had worked on a financial data related [project](https://github.com/stephanoparaskeva/wdi-project-2-hackathon) in a two day hackathon. However there was not enough time to add a lot of the functionality I hoped to add. So myself and another developer decided to do so with Infinite. We derived inspiration from apps like Delta and approached Infinite from an external API focused perspective as the app requires a huge amount of data. We wanted to build the app mobile-first as it is something we were both very interested in using. Having invested in crypto ourselves we thus wanted to use the app on-the-go in our personal lives.

### Walkthrough:

1. The Markets page is an index of the top 50 cryptocurrencies by rank, it features a search bar that searches for over 1500 cryptocurrencies. The Markets page presents a table of the Rank, Symbol, Price, Change, ATH, Market Cap, Circulating Supply and Max Supply of each coin. On mobile, half of the table is scrollable on the X axis.

 ![](https://i.imgur.com/SWtIxZL.png?1)

2. Once a coin is clicked, a show page of the coin with its details magnified are rendered. A candle graph charted via Plotly.js is also rendered. To achieve this, the symbol of the coin the user has selected is transferred to the state of the linked component (show page) and then passed down via props to the candle graph component.
This is then used as part of the query in an Axios request to the external API (Nomics) in the graph component, where the data is then used for the axes of the graph.
    ```javascript
    getCandleData(time) {
        axios
          .get('/api/nomics/candles', {
            params: {
              currency: this.props.coin,
              start: moment().subtract(parseInt(time), 'days').format(),
              end: moment().format()
            }
          })
          .then(res => res.data.map(day => {
            let data = {
              x: [],
              close: [],
              high: [],
              low: [],
              open: []
            }
            return data = {
              x: [...data.x, day.timestamp.slice(0, 10)],
              close: [...data.close, parseFloat(day.close)],
              high: [...data.high, parseFloat(day.high)],
              low: [...data.low, parseFloat(day.low)],
              open: [...data.open, parseFloat(day.open)],
              decreasing: {line: {color: '#e81631'}},
              increasing: {line: {color: '#00b86c'}},
              type: 'candlestick',
              xaxis: 'x',
              yaxis: 'y'
            }
          }))
          .then(data => this.setState({data}))
          .catch(err => console.log(err))
     }
    ```
    And thus the coin show page is rendered. Additionally there are buttons to select timeframes for the historical data (1w, 1m, 1y, 5y) where each button selected sends a new request.

 ![](https://i.imgur.com/jka6FeJ.png?1)

3. Steps 1 and 2 are the limit of functionality for users that are not registered and logged in to the app. Login and register are both accessed via the door icon in the top right of the header. Once logged in, the user can access their personal portfolio via a new icon of a graph that appears.

 ![](https://i.imgur.com/j4QDdkM.png?1)

4. The user can then add their past transactions (buy/sell) via the 'plus' icon on the portfolio page or via the aforementioned coin show page that now has a new 'plus' icon. The user then sees their balance based on these transactions. Once two or more transactions are logged, the user also sees a graph of their balance over time.

    ##### Graph:

      ![](https://i.imgur.com/w2At725.png?1)

    ##### Transactions:

      ![](https://i.imgur.com/nAaIdSM.png)

    ##### Holdings:

      ![](https://i.imgur.com/zD0bisG.png


### Portfolio:
The aforementioned user portfolio page displays a graph of the user's transactions and said user's balance. To obtain the data for the graph, the balance of the user must be updated after each transaction. This is because the balance of the user depends on the current price of the user's holdings, at each moment in time, and thus must be updated every time a user makes a transaction. To do this, the price for all of the coins in the user's holdings must be requested every time a new transaction is made, and used to calculate a current balance. This balance is stored on the transaction model. As a the prices change, a new Axios request is made to the external API (Nomics), before every post to the infinite API. This is all built using the following code:
```javascript
  handleSubmit(e) {
    const timestamp = moment(this.state.data.timestamp).startOf('hour').format()
    e.preventDefault()
    const edit = this.props.location.state.edit
    const transaction = this.props.location.state.transaction
    const data = {...this.state.data}
    axios.get('/api/nomics/graph', {
      params: {
        start: timestamp,
        end: timestamp
      }
    })
      .then(res => {
        const lookupTable = res.data.reduce((obj, curr) => {
          obj[curr.currency] = curr.prices[0]
          return obj
        }, {})
        return this.setState({ lookupTable })
      }).then(() => {
        axios.get('/api/transactions')
          .then(res => {
            return res.data.filter(transaction => {
              return transaction.user.id === Auth.getPayload().sub
            })
          }).then(filteredByUser => {
            if (!edit) return filteredByUser
            return filteredByUser.sort((a, b) => {
              if (moment(a.timestamp) > moment(b.timestamp)) return 1
              return - 1
            })
          }).then(sorted => {
            return sorted.filter(item => {
              return moment(item.timestamp).format() < moment(timestamp).format()
            })
          }).then(filteredByDate => {
            return filteredByDate.reduce((obj, curr) => {
              obj[curr.coin.currency] = (obj[curr.coin.currency] || 0) + curr.buy_quantity - curr.sell_quantity
              return obj
            }, {})
          }).then(holdings => {
            holdings[this.state.coin1.currency] = (holdings[this.state.coin1.currency] || 0) + parseFloat(this.state.data.buy_quantity) - parseFloat(this.state.data.sell_quantity)
            return holdings
          }).then(newHoldings => {
            return Object.keys(newHoldings).map(holdingCurrency => {
              return parseFloat(this.state.lookupTable[holdingCurrency]) * newHoldings[holdingCurrency]
            })
          }).then(map => map.reduce((acc, curr) => {
            return acc += curr
          }, 0)).then(finalTransactionBalance => {
            data.end_of_day_balance = finalTransactionBalance
            if (this.stopBuyToSell(data) === 0 && this.quantityCheck() && edit && this.state.isHidden || this.stopBuyToSell(data) === 0 && this.quantityCheck() && edit && this.checkTransactions(this.state.data.sell_quantity)) {
              axios.put(`/api/transactions/${transaction.id}`, data, { headers: {Authorization: `Bearer ${Auth.getToken()}`}})
                .then(() => this.props.history.push('/portfolio'))
            } else if (this.quantityCheck() && !edit && this.state.isHidden || this.quantityCheck() && !edit && this.checkTransactions(this.state.data.sell_quantity)) {
              axios.post('/api/transactions', data, { headers: {Authorization: `Bearer ${Auth.getToken()}`}})
                .then(() => this.props.history.push('/portfolio'))
            }
          })
      })
  }
 ```
#### Step-by-step:
1. First the date that the user sets is stored as a variable `timestamp`. To be used to get the price data of all coins for that day.
2. Once the price data is returned, it is then reduced into a lookup-table object. The object has the symbol as a key and the price as a value for each coin.
3. Then, a request is made to the Infinite database for all transactions, and the response is filtered by the current user.
4. This response is then sorted by date.
5. Next the response is reduced into a holdings object for the user where each transaction is grouped based on coin with quantities are stored as values.
6. As the user is currently making a transaction, the holdings will change. Because of this, the previous holdings are then combined with the new holdings, just before the post. And depend on whether the transaction is a sell or buy.
7. Next the lookup-table (created from the price data of the external API) is used to give the price of each of the coins in the new holdings. And this is made into an array. The array is then reduced to form the user's balance at the time of the new transaction and added to the data object as `end_of_day_balance` ready to be posted.
8. A post is finally made to the Infinite API.

### Optimisation:
As the external API (Nomics) provided a huge amount of data on any one request, it meant that the site was originally very slow. Loading times were around 10 seconds on initial site load and persisted to be slow throughout the site. I therefore aimed to reduce this
time by finding ways to optimise the site. One particular way I acheived this was by
changing our multiple API requests into a single request in app.js during initial app load.

```javascript
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
```

This reduced initial app load time to around 5 seconds, as before there were multiple requests made on the index page, and now there is only one. This data is then passed down throughout the application to all components that require the data.

To reduce time taken further, I added queries to all of the requests made where the data response provided more data than what we used, this was done in the back-end external API calls. And reduced initial app load time to ~3 seconds.

The coin show page still requires a separate request as each coin requires full candle data for the graph.

### Styling:
From the beginning of the project we had decided to build mobile-first, and therefore chose to use a framework early on that was both lightweight and responsive. We decided to go with the Skeleton CSS framework. This early design choice benefited us later as it allowed for a very mobile responsive site that we could easily customise straight out of the box. We also liked the polish of the Delta app, so chose a similar layout. As we were dealing with very large numbers for example Market Cap, we wanted to display these numbers in a more friendly way and so utilised a library called Numeral, which changed how numbers were formatted. For example a number with 9 digits would be '1.5 b', for 1.5 billion. Lastly to really make our site stand out, we chose to pick a colour scheme that looked original and a logo design that reflected the cyclical nature of how the site was supposed to be navigated and thus chose an infinity symbol.

### Process:
This was a team based project where I worked with one other developer, [Stephen Sabo](https://github.com/SaboHimself). We worked together using Version-Control via Git on GitHub where Stephen was the Git master. Both of us would communicate on what we were doing at each point in time. We'd handle any Git conflicts together and discuss what we wanted to keep and what we didn't. Features were created on separate Git branches before being merged into the development branch.

I planned my models beforehand using an entity relationship diagram in order to construct the back-end. Originally had not included an `end_of_day_balance` on my models and in hindsight, this was a mistake.

![](https://i.imgur.com/AZFHDEj.png)

Going forward, I would have added this to my models originally.

Myself and my teammate used Slack messaging in order to communicate with each other about what tasks we were working on. We decided to play to our strengths, where he was great at implementing external components and frameworks, like the React Datepicker, Numeral, Skeleton and was strong at styling. I decided to focus on the back-end, graphs, interacting with the external API and the RESTful routes (index, show, edit, post, delete).

### Bugs:
*Below is a list of some of the known issues*:

---

**Problem**: The portfolio graph will work when the user follows a specific order of posting or editing their transactions in order of time. If however the user adds a transaction with a date that is in between the dates of other transactions, this causes a problem. The graph and balance will not take into this into account and become misrepresentative.

**Solution**: If the user adds a transaction in between their other transactions, all transactions after this point in time must change. If I were to build this app again I would instead add (add for a buy, subtract for a sell) the difference that this new transaction makes, to the `end_of_day_balance` of all transactions that the user has made with a date that is after that point.

---

**Problem**: The transaction form requires a date and time to be selected, thus if the user picks a date only, the resulting transaction will not have correct information associated with it.

**Solution**: Going forward, I would have made a more robust feature of defaulting any date picked without a time to a specific hour of that day.

---

### Wins and Blockers:

The biggest blocker for me was the portfolio graph. I had found it hard to graph the user balance over time as the balance depends on the price of multiple cryptocurrencies at once. Where each coin that the user holds will have a price that changes independently of another. This created much confusion in how to actually create the graph. It was not until later in the project where myself and my teammate broke the problem down step-by-step and arrived at possible solution.

A win for the app was the extensive seed file I managed to create. Utilising one-time-use temporary functions (not included in the app) I built a giant string of coins with images where each image was provided by a second API, in a seperate file. Then using keyboard commands I turned this string into multiple lines of code. I then combined these images into the response object of the API we were using (Nomics) for our data.

```python
  BTC = Coin(currency='BTC', full_name='Bitcoin', id='BTC', url='https://www.cryptocompare.com/media/19633/btc.png')
  ETH = Coin(currency='ETH', full_name='Ethereum', id='ETH', url='https://www.cryptocompare.com/media/20646/eth_logo.png')
  LTC = Coin(currency='LTC', full_name='Litecoin', id='LTC', url='https://www.cryptocompare.com/media/35309662/ltc.png')
  DASH = Coin(currency='DASH', full_name='Dash', id='DASH', url='https://www.cryptocompare.com/media/33842920/dash.png')
  XMR = Coin(currency='XMR', full_name='Monero', id='XMR', url='https://www.cryptocompare.com/media/19969/xmr.png')
  NXT = Coin(currency='NXT', full_name='Nxt', id='NXT', url='https://www.cryptocompare.com/media/20627/nxt.png')
  ETC = Coin(currency='ETC', full_name='Ethereum Classic', id='ETC', url='https://www.cryptocompare.com/media/33752295/etc_new.png')
  DOGE = Coin(currency='DOGE', full_name='Dogecoin', id='DOGE', url='https://www.cryptocompare.com/media/19684/doge.png')
  ZEC = Coin(currency='ZEC', full_name='ZCash', id='ZEC', url='https://www.cryptocompare.com/media/351360/zec.png')
```
There are some 3500 such lines of code.
These coins are combined with the data from the API we were actually using via the code below:

```javascript
attachCoinToNomics() {
  const coinLookup = this.state.coinData.reduce((obj, current) => {
    obj[current.currency] = current.url
    obj[`${current.currency}2`] = current.full_name
    return obj
  }, {})
  const filtered = this.state.nomics.data.filter(nomic => Object.keys(coinLookup).includes(nomic.currency))
  return filtered.map(item => ({...item, image_url: coinLookup[item.currency], full_name: coinLookup[`${item.currency}2`]}))
}
```

### Future Features:

*Features we would like to add, include:*

* More user feedback, as the site should let the user know if they successfully log in, register or if these things where unsuccessful and why. Whether a transaction was successful or why it was not.

* A more robust portfolio graph that works regardless of the order of transactions.

* Filters on the coin index as well as buttons that allow the user to see coin data with different timeframes.

* A coin index with data that updates more regularly, as currently it is the daily prices.

### Key Learnings:

This project was a very holistic learning experience for myself. Full of realisations on how to do things better in the future. It has taught me the necessity of a robust back-end architecture, as I learned fast that having a stronger foundation would have reduced and refactored a lot of work that should not have been required later on. It taught me further, how to truly utilise my basic programming tools. Dealing with such vast amounts of data meant that I repetitively got to use the stretch of my knowledge. Map, reduce, filter, sort. Constantly writing code and then re-writing after finding a better solution. And lastly this project put my team-working ability to the test. As the challenges were big, myself and my teammate had to become closer and really scrutinise each others work, while pushing each other to achieve more. Overall I enjoyed working on this project a lot and will carry what I learned over to what I work on next.

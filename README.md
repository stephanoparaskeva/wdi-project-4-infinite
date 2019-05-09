# General Assembly WDI Project 4
## Infinite
___
### Timeframe:
    9 days
### The Brief:

* **Build a full-stack application** by making your own backend and your own front-end
* **Use a Python Flask API** to serve your data from a Postgres database
* **Consume your API with a separate front-end** built with React
* **Be a complete product** which most likely means multiple relationships and CRUD functionality for at least a couple of models
* **Implement thoughtful user stories/wireframes** that are significant enough to help you know which features are core MVP and which you can cut
* **Have a visually impressive design** to kick your portfolio up a notch and have something to wow future clients & employers. **ALLOW** time for this.
* **Be deployed online** so it's publicly accessible.

### Technologies:

* JavaScript
* Python
* React
* Flask
* PostgreSQL
* CSS
* SCSS
* Skeleton
* HTML
* Axios
* Plotly.js


### App:
![](https://i.imgur.com/aKPHDuL.png?1)

### Overview:
A cryptocurrency portfolio tracker with real-time price change data and candle graphs. The user can make transactions, see their balance and a graph of their balance over time based on the coins they own.

### Step-by-step:

1. The Markets page is a permissionless index of the top 100 cryptocurrencies based on daily price. It presents a table of the Rank, Symbol, Price, Change, ATH, Market Cap, Circulating Supply and Max supply of each coin. On mobile, half of the table is scrollable on the X axis.
![](https://i.imgur.com/SWtIxZL.png?1)

2. Once a coin is clicked, a show page of the coin with it's details magnified is rendered. A candle graph charted via Plotly.js is also rendered. To acheive this, the symbol of the coin the user previously selected is transferred to the state of the linked component (show page) and then passed down via props to the candle graph component. 
![](https://i.imgur.com/LCASC4M.png) /newline
This is then used as part of the query in an Axios request to the external API (Nomics) in the graph component, where the data is then used for the axis of the graph.
![](https://i.imgur.com/uO9AeBz.png)
And finally the coin show page is rendered. Additionally there are buttons to select timeframes for the historical data (1w, 1m, 1y, 5y) where each button selected sends a new request.
![](https://i.imgur.com/jka6FeJ.png?1)
3. There draws the limit of functionality for users that are not registered and logged in to the app (both are accessed via the door icon in the top right of the header). Once logged in: ![](https://i.imgur.com/MtGS71t.png)
    (Passwords require at least 1 uppercase letter, 1 lowercase letter and 1 number)
The user can now access their personal portfolio via a new icon of a graph that appears in the header.
![](https://i.imgur.com/iajeTNc.png) 
4. The user can then add their past transactions (buy/sell) via the plus icon or via the coin show page navigated from the coin index. Which was unnavailable if not logged in, the user then see's their balance and change for these transactions. Once two or more transactions are logged, the user also see's a graph of their balance over time. 
    #### Graph: ![](https://i.imgur.com/4rt83tF.png)
    #### Transactions: ![](https://i.imgur.com/i9tehB7.png)
    #### Holdings: ![](https://i.imgur.com/8T5iL3X.png)

### Portfolio:
The aforementioned user portfolio page displays a graph of the users transactions and said users balance. To obtain the data for the graph, the balance of the user must be updated after each transaction, as the balance of the user depends on the price and quantity of coins they hold, where the price changes in time. As each transaction is made at a different time, the price for all of the coins in their holdings must be requested every time a new transaction is made and used to calculate a current balance relative to the time of the last transaction. This balance is stored on the transaction model. As a the prices change, a new axios request to the external API (Nomics) is made before every post to the infinite API. This post is built using the following code.
```
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
1. First the date the user sets the transaction as, is stored in a variable. And is used to get the price data of all coins for the chosen day.
2. This is then reduced into a lookup-table object with the symbol as a key and the price as a value for each coin.
3. Then a request to the Infinite database for all transactions is made and filtered by current user.
4. This response is then sorted by date.
5. Next it is reduced into a holdings object for the user where each coin is grouped together and their quantities are stored as values.
6. The holdings are then combined with what the current transaction (that the user is about to make) add or remove from their holdings. 
7. Then the lookup-table is used to give the value of each of their coins on the date set and this is made into an array. The array is then reduced to form their balance at the time of the new transaction and added to the data object as 'end_of_day_balance' ready to be posted.
8. A post is finally made to the infinite API.

### Process:
This was a team based project where I worked with one other developer. [Stephen Sabo](https://github.com/SaboHimself). We worked together using Version-Control via Git on GitHub where Stephen was the Git master. Both of us would communicate on what we were doing at each point in time. We'd handle any Git conflicts together and discuss what we wanted to keep and what we didn't. We both seperated responsibilites and gave eachother feedback. Where we were confused, we'd consult eachother for advice. Features were created on separate git branches before being merged into the development branch.



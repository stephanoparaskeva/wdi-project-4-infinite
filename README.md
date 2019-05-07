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

### Instructions:

1. The Markets page is a permissionless index of the top 100 cryptocurrencies based on daily price. It presents a table of the Rank, Symbol, Price, Change, ATH, Market Cap, Circulating Supply and Max supply of each coin. On mobile, half of the table is scrollable on the X axis.
![](https://i.imgur.com/SWtIxZL.png?1)

2. Once a coin is clicked, a show page of the coin with it's details magnified is rendered. A candle graph charted via Plotly.js is also rendered. To acheive this, the symbol of the coin the user previously selected is transferred to the state of the linked component (show page) and then passed down via props to the candle graph component. 
![](https://i.imgur.com/LCASC4M.png)
This is then used as part of the query in an Axios request to the external API (Nomics) in the graph component, where the data is then used for the axis of the graph.
![](https://i.imgur.com/uO9AeBz.png)
And finally the coin show page is rendered. Additionally there are buttons to select timeframes for the historical data (1w, 1m, 1y, 5y) where each button selected sends a new request.
![](https://i.imgur.com/jka6FeJ.png?1)
3. There draws the limit of the apps functionality for users that are not registered and logged in (both are accessed via the door icon in the top right of the header). Once logged in: ![](https://i.imgur.com/MtGS71t.png)
    (Passwords require at least 1 uppercase letter, 1 lowercase letter and 1 number)
The user can now access their personal portfolio via a new icon of a graph in the header.
![](https://i.imgur.com/iajeTNc.png) 

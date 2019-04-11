import React from 'react'

const Holdings = ({ holdings }) => {
  return(
    <ul>
      {holdings.map(coin => <li key={coin.currency}>{coin.currency} {coin.quantity}</li>)}
    </ul>
  )
}

export default Holdings

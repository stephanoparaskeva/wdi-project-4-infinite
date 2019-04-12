import React from 'react'

const Holdings = ({ holdings }) => {
  console.log(holdings)
  return(
    <table className="u-full-width">
      <thead>
        <tr>
          <th>Name</th>
          <th>Quantity</th>
        </tr>
      </thead>
      {holdings.map(coin =>
        <tbody key={coin.currency}>
          <tr>
            <td>{coin.currency}</td>
            <td>{coin.quantity}</td>
          </tr>
        </tbody>
      )}
    </table>
  )
}

export default Holdings

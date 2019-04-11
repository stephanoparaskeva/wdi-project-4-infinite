import React from 'react'

// class Holdings extends React.Component {
//   constructor() {
//     super()
//
//     this.state = {}
//   }
//
//   render() {
//     return(
//       <div>
//
//       </div>
//     )
//   }
//
// }
//
// export default Holdings

const Holdings = ({ userCoins }) => {
  return(
    <ul>
      {Object.keys(userCoins).map(item => <li key={item}>Hello</li>)}
    </ul>
  )
}

export default Holdings

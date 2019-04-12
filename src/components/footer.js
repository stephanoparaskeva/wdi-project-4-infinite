import React from 'react'
import { Link } from 'react-router-dom'

class Footer extends React.Component{
  constructor() {
    super()
  }

  render(){
    return(
      <footer className="footer">
        <Link to='/about'>About</Link>
      </footer>
    )
  }
}

export default Footer

import React, { Component } from 'react';
import '../stylesheets/cards.css';
import '../stylesheets/SubBar.css';
import AddMovie from './AddMovie';





class subBar extends Component {
    
  constructor(){
    super();
  }
  componentDidUpdate() { this.getData(this.props.location.pathname); }


  render(){
    return(
        <div className="subBar">
            <div>
            <input type="text" placeholder="Search . . ." required/>
            </div> 
           <AddMovie/>
        </div>
    );
}

  
}

export default subBar;
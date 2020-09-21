import React, { Component } from 'react';


class ActorsView extends Component{

    state = {
        reload: false
      };
    
      refreshPage = () => {
        this.setState(
          {reload: true},
          () => this.setState({reload: false})
        )
        window.location.reload(false);
      }
    

    
    render(){
        return(
            <li onClick={() => {this.navTo('/actors')}} class="menu__item menu__item--current"><a href="#" class="menu__link">Actors</a></li>
        );
    }

}

export default ActorsView;
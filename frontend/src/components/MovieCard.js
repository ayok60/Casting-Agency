import React, { Component } from 'react';
import '../stylesheets/cards.css';


class Card extends Component {
    
  constructor(){
    super();
  }

  render() {
    const { title, release_date} = this.props;
    return (
        <div class="profile-card-2"><img src="http://envato.jayasankarkr.in/code/profile/assets/img/profile-2.jpg" class="img img-responsive"/>
            <div class="profile-name">{ title }</div>
            <div class="profile-username">{ release_date }</div>
        </div>
    );
  }
}

export default Card;

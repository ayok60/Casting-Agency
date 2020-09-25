import React, { Component } from 'react';
import '../stylesheets/cards.css';
import Popup from 'reactjs-popup';
import ActorsForm from './ActorsForm'
import AssignActorsForm from './AssignActorsForm'






class Card extends Component {
    
  constructor(){
    super();
    
  }

  render() {
  
    const { name, age , gender , image_link, id,actor} = this.props;
    return (
      <div class="property-card">
        <div class="profile-card-2">
          <img src={image_link} class="img img-responsive"/>
          <div class="profile-name">{ name }</div>
          <div class="profile-username">{ age }</div>
        </div>
        <div class="property-description">
          <h5> { name } </h5>
          <h6> ID: { id } </h6>
          <h6> Age: { age } </h6>
          <h6> Gender: { gender } </h6>
          <p>Lorem Ipsum Dipsum hortata. Mixcall Horcho. Mixwell Chingo. More Bingo. Lorem Ipum doth be hard.</p>
          <div class="card-btns">
            <ActorsForm name={name} age={age} actor={id}/>
            <Popup trigger={open => ( <button>X</button> )} modal>
            {close => (
            <div className="modal">
            <div className="header"> { name } </div>
            <div className="content">
            {' '}
            Are you sure you want to delete  { name } ?

            </div>
            <div className="actions">
            <button className="button" onClick={() => { close(); window.location.reload(); this.props.deleteActor('DELETE')}}> Delete</button>
            <button className="button" onClick={() => { close(); }}> Cancel</button>
            </div>
            </div>
            )}
            </Popup>
          </div>
        </div>
      </div>
    );
  }
}

export default Card;


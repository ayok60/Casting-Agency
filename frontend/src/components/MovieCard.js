import React, { Component } from 'react';
import '../stylesheets/cards.css';
import Popup from 'reactjs-popup';
import MoviesForm from './MoviesForm';
import AssignActorsForm from './AssignActorsForm'
import Can from './Can';






class Card extends Component {
    
  constructor(){
    super();
    
  }

  render() {
  
    const { title, release_date,image_link, movie} = this.props;
    return (
      <div class="property-card">
        <div class="profile-card-2">
          <img src={image_link} class="img img-responsive"/>
          <div class="profile-name">{ title }</div>
          <div class="profile-username">{ release_date }</div>
        </div>
        <div class="property-description">
          <h5> { title } </h5>
          <h6> ID: { movie.id } </h6>
          <h6> Release Date: { release_date } </h6>
          <p>Lorem Ipsum Dipsum hortata. Mixcall Horcho. Mixwell Chingo. More Bingo. Lorem Ipum doth be hard.</p>
          <div class="card-btns">
          <MoviesForm title={title} release_date={release_date} movie={movie} />
          <Can
            permission="edit:movies"
            yes={() => (
              <AssignActorsForm title={title} movie={movie}/>
            )}
          />
          <Can
            permission="delete:movie"
            yes={() => (

              <Popup trigger={open => ( <button>X</button> )} modal>
                {close => (
                  <div className="modal">
                    <div className="header"> { title } </div>
                    <div className="content">
                      {' '}
                      Are you sure you want to delete  { title } ?
                      
                    </div>
                    <div className="actions">
                      <button className="button" onClick={() => { close(); window.location.reload(); this.props.deleteMovie('DELETE')}}> Delete</button>
                      <button className="button" onClick={() => { close(); }}> Cancel</button>
                    </div>
                  </div>
                )}
              </Popup>

            )}
          />
          
          </div>
        </div>
      </div>
    );
  }
}

export default Card;




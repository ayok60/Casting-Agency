import React, { Component } from 'react';

import '../stylesheets/App.css';
import '../stylesheets/cards.css';
import Card from './ActorsCard';
import $ from 'jquery';


const token = localStorage.getItem('JWTS_LOCAL_KEY');


class ActorsView extends Component{

    
  constructor(){
    super();
    this.state = {
      actors:[]
    }
}

componentDidMount() {
    this.getActors();
    
}
getActors = () => {
    $.ajax({
      url: `/actors`, 
      type: "GET",
      headers: {"Authorization": 'Bearer ' + token},
      success: (result) => {
        this.setState({
            actors: result.actors
        })
        return;
      },
      error: (error) => {
        alert('Unable to load questions. Please try your request again')
        return;
      }
    })
}

deleteActor = (id) => (action) => {
  if(action === 'DELETE') {
      $.ajax({
        url: `/actors/${id}`, 
        type: "DELETE",
        headers: {"Authorization": 'Bearer ' + token},
        error: (error) => {
          return;
        }
      })
    
  }
}
    
    render(){
        return(
          <section class="cards">
            <div class="container">
              <div class="card-list">
                        {this.state.actors.map((q, ind) => (
                            <Card
                                name={q.name}
                                age={q.age}
                                gender={q.gender}
                                deleteActor={this.deleteActor(q.id)}
                                id={q.id}
                                actor = {q}
                                image_link={q.image_link}
                            />
                        ))}
                    </div>
              </div>
          </section>
        );
    }

}

export default ActorsView;
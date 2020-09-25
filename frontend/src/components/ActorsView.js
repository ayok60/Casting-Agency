import React, { Component } from 'react';

import '../stylesheets/App.css';
import '../stylesheets/cards.css';
import Card from './ActorsCard';
import $ from 'jquery';

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
      url: `/actors`, //TODO: update request URL
      type: "GET",
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
        url: `/actors/${id}`, //TODO: update request URL
        type: "DELETE",
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
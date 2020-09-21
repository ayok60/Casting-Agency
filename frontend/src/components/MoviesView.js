import React, { Component } from 'react';

import '../stylesheets/App.css';
import '../stylesheets/cards.css';
import Card from './MovieCard';
import $ from 'jquery';

class MoviesView extends Component{

    constructor(){
        super();
        this.state = {
          movies:[],
          title: "",
          release_date: "",
        }
    }

    componentDidMount() {
        this.getMovies();
    }

    getMovies = () => {
        $.ajax({
          url: '/movies', //TODO: update request URL
          type: "GET",
          success: (result) => {
            this.setState({
              title: result.title,
              release_date: result.release_date,
            })
            return;
          },
          error: (error) => {
            alert('Unable to load questions. Please try your request again')
            return;
          }
        })
    }

    
    render(){
        return(
            <section class="cards">
		        <div class="container">
			        <div class="card-list">
                        {this.state.movies.map((q, ind) => (
                            <Card
                                key={q.id}
                                title={q.title}
                                release_date={q.release_date}
                            />
                        ))}
                    </div>
		        </div>
	        </section>
        );
    }

}

export default MoviesView;
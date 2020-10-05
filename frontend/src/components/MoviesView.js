import React, { Component } from 'react';

import '../stylesheets/App.css';
import '../stylesheets/cards.css';
import Card from './MovieCard';
import $ from 'jquery';



const token = localStorage.getItem('JWTS_LOCAL_KEY');


class MoviesView extends Component{

    constructor(){
        super();
        this.state = {
          movies:[]
        }
    }

    componentDidMount() {
        this.getMovies();
        
    }

    getMovies = () => {
        $.ajax({
          url: `/movies`, //TODO: update request URL
          type: "GET",
          headers: {"Authorization": 'Bearer ' + token},
          success: (result) => {
            this.setState({
                movies: result.movies
            })
            return;
          },
          error: (error) => {
            alert('error get movies')
            return;
          }
        })
    }

    deleteMovie = (id) => (action) => {
        if(action === 'DELETE') {
            $.ajax({
              url: `/movies/${id}`, //TODO: update request URL
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
            <section className="cards">
		        <div className="container">
			        <div className="card-list">
                        {this.state.movies.map((q, ind) => (
                            <Card
                                id={q.id}
                                title={q.title}
                                release_date={q.release_date}
                                image_link={q.image_link}
                                deleteMovie={this.deleteMovie(q.id)}
                                movie={q}
                            />
                        ))}
                    </div>
		        </div>
	        </section>
        );
    }

}

export default MoviesView;
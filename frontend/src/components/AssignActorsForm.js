import React, { Component } from 'react';
import '../stylesheets/cards.css';
import '../stylesheets/form.css';
import Popup from 'reactjs-popup';
import $, { get } from 'jquery';




class AssignActorsForm extends Component {
    
  constructor(props){
    super(props);
    this.state = {
      castings: [],
      actors: [],
      movie_id: "",
      actor_id: ""
      
    }

    this.getCasting(this.props.movie.id)
  }

  componentDidUpdate(){

  }

  
  getCasting = (id) => {
    $.ajax({
      url: `/castings/movies/${id}`, //TODO: update request URL
      type: "GET",
      success: (result) => {
        this.setState({
          castings: result.castings,
          actors: result.actors
        })
        return;
      },
      error: (error) => {
        alert('casting ' + id)
        return;
      }
    })
}

  

  AssignActors = (event) => {
    event.preventDefault();
    $.ajax({
      url: '/castings/movies', //TODO: update request URL
      type: "POST",
      dataType: 'json',
      contentType: 'application/json',
      data: JSON.stringify({
        movie_id: this.state.movie_id,
        actor_id: this.state.actor_id
      }),
      xhrFields: {
        withCredentials: true
      },
      crossDomain: true,
      success: (result) => {
        document.getElementById("assign-actors-form").reset();
        return;
      },
      error: (error) => {
          console.log(this.state.movie_id)
          console.log('aa')
          console.log(this.state.actor_id)
        return;
      }
    })
  }
  
  deleteActorCast = (movie_id, actor_id) => {
        $.ajax({
          url: `/movies/${movie_id}/${actor_id}`, //TODO: update request URL
          type: "DELETE",
          error: (error) => {
            console.log(error);
            return;
          }
        })
      
  }



  handleChange = (name, value) => (event) => {
    this.setState({[event.target.name]: parseInt(event.target.value)})
    console.log({[event.target.name]: (event.target.value)})
    this.setState({[name]: (parseInt(value))})
    console.log({[name]: (String(value))})
  }

  handleChangeTest = (name, value) => {
    this.setState({[name]: ((value))})
    console.log({[name]: ((value))})
  }
  
  render(){
    
    const { title , movie } = this.props;
    return(

        
        
        <Popup className="assign-actors" trigger={open => ( <button >Assign Actors</button> )} modal onOpen={() => {console.log( this.state.castings)}} >
            {close => (
              <div className="modal">
                <div>
                  <div className="header"> {title} </div>
                  <div className="content">
                    <h4>CAST</h4>
                    <ul className="cast-list">
                      {this.state.actors.map((q, ind) => (
                        <li className="cast-entities">
                          <p> ID.{q.id} </p> <p>{q.name }</p> 
                          
                          <button className="delete-cast" onClick= {() => 
                            {console.log('delete');  this.deleteActorCast(movie.id, q.id);
                          }}         
                            >X</button>
                        </li>
                      ))}
                    </ul>
                    <br></br>
                    <div id="form">
                      <form className="form-view" id="assign-actors-form" onSubmit={this.AssignActors}>
                        <label>Movie</label>
                        <input type="text" name="movie_id" value={movie.id} disabled/>
                        <label>Actors</label>
                        <input type="text" name="actor_id" placeholder='e.g.  Jhone Smith, Michel Zac' onChange={this.handleChange("movie_id",movie.id)}/>
                        <div className="actions">
                          <input type="submit" className="button" onClick={() => {  window.location.reload()   }} value="ASSIGN" />  
                          <button className="button" onClick={() => {  close(); console.log('aya')  }}> Cancel </button>
                        </div>   
                      </form>
                    </div>
                  </div>
                </div>
              </div>
            )}
        </Popup>
      
    );
}

  
}

export default AssignActorsForm;



import React, { Component } from 'react';
import '../stylesheets/cards.css';
import '../stylesheets/form.css';
import Popup from 'reactjs-popup';
import $ from 'jquery';






class MoviesForm extends Component {
    
  constructor(){
    super();
    this.state = {
      title: "",
      release_date: "",
      id: 0,
      image_link: ""
    }
    
  }

  componentDidMount(){
  }
  
  editMovie = (id) => (event) => {
    event.preventDefault();
    $.ajax({
      url: `/movies/${id}`, //TODO: update request URL
      type: "PATCH",
      dataType: 'json',
      contentType: 'application/json',
      data: JSON.stringify({
        title: this.state.title,
        release_date: this.state.release_date,
        image_link: this.state.image_link,
      }),
      xhrFields: {
        withCredentials: true
      },
      crossDomain: true,
      success: (result) => {
        this.setState({
          title: this.state.title,
          release_date: this.state.release_date,
          image_link: this.state.image_link,
        })
        document.getElementById("edit-movie-form").reset();
        return;
      },
      error: (error) => {
        alert('Unable to add question. Please try your request again')
        return;
      }
    })
  }

  handleChange = (event) => {
    this.setState({[event.target.name]: event.target.value})
    console.log({[event.target.name]: event.target.value})
  }


  render(){
    
    const { title, release_date , movie} = this.props;

    return(
        
        <Popup trigger={open => ( <button > Edit </button> )} modal>
            {close => (
                <div className="modal">
                    <div className="header"> {title} </div>
                    <div className="content">
                        {' '}
                        <div id="form">
                            <form className="form-view" id="edit-movie-form" onSubmit={this.editMovie(movie.id)}>
                                <label>Title</label>
                                <input type="text" name="title" placeholder={title} onChange={this.handleChange}/>
                                <label>Release Date</label>
                                <input type="text" name="release_date" placeholder={release_date} onChange={this.handleChange}/>
                                <label>Poster Image Link</label>
                                <input type="text" name="image_link" placeholder='http://' onChange={this.handleChange}/>
                                <div className="actions">
                                  <input type="submit" onClick={() => {window.location.reload();}} className="button" value="Edit" />  
                                  <button className="button" onClick={() => { close();}}> Cancel </button>
                                </div>   
                            </form>
                        </div>
                    </div>
                </div>
            )}
        </Popup>
      
    );
}

  
}

export default MoviesForm;



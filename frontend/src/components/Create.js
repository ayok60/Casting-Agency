import React, { Component } from 'react';
import '../stylesheets/cards.css';
import '../stylesheets/form.css';
import Popup from 'reactjs-popup';
import $ from 'jquery';
import Can from './Can'



const token = localStorage.getItem('JWTS_LOCAL_KEY');

class Create extends Component {
    
  constructor(){
    super();
    this.state = {
      title: "",
      release_date: "",
      image_link: "",
      name: "",
      age: 0,
      gender: "Male",
    }

    
  }



  addMovie = (event) => {
    event.preventDefault();
    $.ajax({
      url: '/movies', 
      type: "POST",
      headers: {"Authorization": 'Bearer ' + token},
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
        document.getElementById("add-movie-form").reset();
        window.location.reload();
        return;
      },
      error: (error) => {
        alert('Unable to add question. Please try your request again')
        return;
      }
    })
  }
  
  addActor = (event) => {
    event.preventDefault();
    $.ajax({
      url: '/actors', 
      type: "POST",
      headers: {"Authorization": 'Bearer ' + token},
      dataType: 'json',
      contentType: 'application/json',
      data: JSON.stringify({
        name: this.state.name,
        age: this.state.age,
        gender: this.state.gender,
        image_link: this.state.image_link,
      }),
      xhrFields: {
        withCredentials: true
      },
      crossDomain: true,
      success: (result) => {
        document.getElementById("add-actor-form").reset();
        window.location.reload();
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

  update() 
  { 
    
        if (window.location.pathname.indexOf("movies") > -1 ){
          return true
        }
        else{
          return false
        }
  
  }

  

  render(){
        
    return(
        
        <Popup trigger={open => ( <button>Create</button> )} modal>
            {close => (
              
                <div className="modal">
                  {this.update() ?
                  <Can
                  permission="add:movie"
                  yes={() => (
                    <div>
                    <div className="header"> Create New Movie </div>
                    <div className="content">
                        {' '}
                        <div id="form">
                            <form className="form-view" id="add-movie-form" onSubmit={this.addMovie}>
                                <label>Title</label>
                                <input type="text" name="title" placeholder='Movie' required onChange={this.handleChange}/>
                                <label>Release Date</label>
                                <input type="text" name="release_date" placeholder='DD.MM.YYY' required onChange={this.handleChange}/>
                                <label>Poster Image Link</label>
                                <input type="text" name="image_link" placeholder='http://' required onChange={this.handleChange}/>
                                <div className="actions">
                                  <input type="submit" className="button" onClick={() => {
                                    console.log('submit')}} value="Create" />  
                                  <button className="button" onClick={() => { close();}}> Cancel </button>
                                </div>   
                            </form>
                        </div>
                    </div>
                    </div>
                    )}
                  />
                  :
                  <div>
                  <div className="header"> Create New Actor </div>
                  <div className="content">
                      {' '}
                      <div id="form">
                              <form className="form-view" id="add-actor-form" onSubmit={this.addActor}>
                                <label>Name</label>
                                <input type="text" name="name" placeholder='Jhone Smith' onChange={this.handleChange}/>
                                <label>Age</label>
                                <input type="text" name="age" placeholder='25' onChange={this.handleChange}/>
                                <label>Gender</label>
                                <select id="gender" name="gender" onChange={this.handleChange}>
                                    <option  disabled hidden value="Male">Select</option>
                                    <option value="Male">Male</option>
                                    <option value="Female">Female</option>
                                </select>
                                <label>Image Link</label>
                                <input type="text" name="image_link" placeholder='http://' onChange={this.handleChange}/>
                                <div className="actions">
                                    <input type="submit" className="button" value="Create" />  
                                    <button className="button" onClick={() => { close(); }}> Cancel </button>
                                </div>   
                            </form>
                      </div>
                  </div>
                  </div>
                  }
                </div>

                
            )}
        </Popup>
      
    );
}

  
}

export default Create;


import React, { Component } from 'react';
import '../stylesheets/cards.css';
import '../stylesheets/form.css';
import Popup from 'reactjs-popup';
import $ from 'jquery';
import Can from './Can'



const token = localStorage.getItem('JWTS_LOCAL_KEY');


class ActorsForm extends Component {
    
  constructor(){
    super();
    this.state = {
        name: "",
        age: 0,
        gender: "",
        image_link: ""
    }
    
  }

    createActor = (id) => (event) => {
        event.preventDefault();
        $.ajax({
        url: `/actors/${id}`, 
        type: "PATCH",
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
            this.setState({
                name: this.state.name,
                age: this.state.age,
                gender: this.state.gender,
                image_link: this.state.image_link,
            })
            document.getElementById("add-actor-form").reset();
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
    
    const { name, age, actor } = this.props;

    return(
        <Can
            permission="edit:actors"
            yes={() => ( 
                <Popup trigger={open => ( <button>edit</button> )} modal>
                    {close => (
                        <div className="modal">
                            <div>
                            <div className="header"> {name} </div>
                            <div className="content">
                                {' '}
                                <div id="form">
                                    <form className="form-view" id="add-actor-form" onSubmit={this.createActor(actor)}>
                                        <label>Name</label>
                                        <input type="text" name="name" placeholder={name} onChange={this.handleChange}/>
                                        <label>Age</label>
                                        <input type="text" name="age" placeholder={age} onChange={this.handleChange}/>
                                        <label>Gender</label>
                                        <select id="gender" name="gender" onChange={this.handleChange}>
                                            <option  disabled hidden value="Male">Select</option>
                                            <option value="Male">Male</option>
                                            <option value="Female">Female</option>
                                        </select>
                                        <label>Image Link</label>
                                        <input type="text" name="image_link" placeholder='http://' onChange={this.handleChange}/>
                                        <div className="actions">
                                            <input type="submit" onClick={() => {window.location.reload();}} className="button" value="Edit" />  
                                            <button className="button" onClick={() => { close(); }}> Cancel </button>
                                        </div>   
                                    </form>
                                </div>
                            </div></div>
                        </div>
                    )}
                </Popup>
            )}
        />
      
    );
}

  
}

export default ActorsForm;


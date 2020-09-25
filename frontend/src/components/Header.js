import React, { Component } from 'react'

import '../stylesheets/Header.css';
import { Link } from 'react-router-dom';




class Header extends Component {
  

  navTo(uri){
    
    var currentID = (uri === "/actors") ? '#actors_nav' : '#movies_nav';
    var current = document.querySelector(currentID);

    var previousID = (uri !== "/actors") ? '#actors_nav' : '#movies_nav';
    var previous = document.querySelector(previousID);
    
    current.classList.add('menu__item--current');
    previous.classList.remove('menu__item--current');
  }

    activeBtn() {
    const pathname = window.location.pathname;
    var item = (pathname === "/actors") ? '#actors_nav' : '#movies_nav';
    item = document.querySelector(item)
    item.classList.add('menu__item--current');
  }

  componentDidMount() {
    this.activeBtn()
  }

  

  render() {

    return (
        
        <section className="section section--menu" id="Valentine">
            <h2 className="section__title">Casting Agency</h2>
            <nav className="menu menu--valentine">
                <ul className="menu__list">
                    <li id="actors_nav" onClick={(e) => {this.navTo('/actors')}} className="menu__item" ><Link to="/actors" className="menu__link">Actors</Link></li>
                    <li onClick={(e) => {this.navTo('/movies')}} className="menu__item" id="movies_nav"><Link to="/movies" className="menu__link">Movies</Link></li>
                </ul>
            </nav>
        </section>
        
    );
  }
}



export default Header;

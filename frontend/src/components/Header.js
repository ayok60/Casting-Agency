import React, { Component } from 'react';
import { Redirect } from 'react-router';

import '../stylesheets/Header.css';
import classie from  './classie';
import History from '../History'


class Header extends Component {
  
  navTo(uri){
    History.push(uri);
    (function() {
		[].slice.call(document.querySelectorAll('.menu')).forEach(function(menu) {
			var menuItems = menu.querySelectorAll('.menu__link'),
				setCurrent = function(ev) {
					ev.preventDefault();

					var item = ev.target.parentNode; // li

					// return if already current
					if (classie.has(item, 'menu__item--current')) {
						return false;
					}
					// remove current
					classie.remove(menu.querySelector('.menu__item--current'), 'menu__item--current');
					// set current
                    classie.add(item, 'menu__item--current');
				};

			[].slice.call(menuItems).forEach(function(el) {
                el.addEventListener('click', setCurrent);
            });
		});
    })(window);
  }

  activeBtn() {
    const pathname = window.location.pathname;
    var item;
    if (pathname == "/actors") {
      item = document.querySelector('#actors_nav')
    }
    else {
      item = document.querySelector('#movies_nav')
    }
    classie.add(item, 'menu__item--current');
  }

  componentDidMount() {
    const script = document.createElement("script");
    script.async = true;
    script.src = "./classie.js";
    document.body.appendChild(script);
    this.activeBtn()
  }

  

  render() {

    return (
        
        <section class="section section--menu" id="Valentine">
            <h2 class="section__title">Casting Agency</h2>
            <nav class="menu menu--valentine">
                <ul class="menu__list">
                    <li onClick={() => {this.navTo('/actors')}} class="menu__item" id="actors_nav"><a class="menu__link">Actors</a></li>
                    <li onClick={() => {this.navTo('/movies')}} class="menu__item" id="movies_nav"><a class="menu__link">Movies</a></li>
                </ul>
            </nav>
        </section>
        
    );
  }
}



export default Header;

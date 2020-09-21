import React, { Component } from 'react';
import History from './History'
import {
  BrowserRouter as Router,
  Route,
  Switch
} from 'react-router-dom'

import logo from './logo.svg';
import './stylesheets/App.css';
import Header from './components/Header';
import ActorsView from './components/ActorsView';
import MoviesView from './components/MoviesView';

function App() {
  return (
    <div className="App">
      <Header path />
      <Router History={History}>
        <Switch>
          <Route path="/actors" exact component={ActorsView}/>
          <Route path="/movies" component={MoviesView}/>
        </Switch>
      </Router>
    </div>
  );
}

export default App;

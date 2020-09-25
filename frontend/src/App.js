import React from 'react';
import History from './History'
import {
  BrowserRouter as Router,
  Route,
  Switch,
} from 'react-router-dom'

import './stylesheets/App.css';
import Header from './components/Header';
import ActorsView from './components/ActorsView';
import MoviesView from './components/MoviesView';
import SubBar from './components/SubBar';

function App() {
  
  return (
    
    <div className="App">
      
      <Router History={History}>
        <Header path />
        < SubBar/>
        <Switch>
          <Route path="/actors" exact component={ActorsView}/>
          <Route path="/movies" component={MoviesView}/>
          <Route component={ActorsView} />
        </Switch>
      </Router>
    </div>
    
  );
}

export default App;

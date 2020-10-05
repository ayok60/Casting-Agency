import React from 'react';
import History from './history'
import {
  BrowserRouter as Router,
  Route,
  Switch,
  Redirect
} from 'react-router-dom'

import './stylesheets/App.css';
import './stylesheets/SubBar.css';
import Header from './components/Header';
import ActorsView from './components/ActorsView';
import MoviesView from './components/MoviesView';
import Create from './components/Create';
import LoginButton from './components/login-button';
import LogoutButton from './components/logout-button';
import Auth from "./components/Auth";
import CallbackPage from './components/callback'
import { AuthConsumer } from "./authContext";
import Can from './components/Can';





function App() {

  
  return (
    
    <div className="App">
      <Auth>
        <Router History={History}>
          <Header path />     
          <AuthConsumer>
            {({ authenticated }) =>
              authenticated ? (
                <div className="subBar">
                  <Redirect to="/actors" />
                  <LogoutButton />
                  <Can
                    permission="add:actor"
                    yes={() => (
                      <Create/>
                    )}
                  />
                  
                </div> 
              ) : (
                <div className="subBar">
                  <LoginButton />
                </div>
              )
            }
          </AuthConsumer>     
          <Switch>
            <Route path="/actors" exact component={ActorsView}/>
            <Route path="/movies" component={MoviesView}/>
            <Route path="/callback" component={CallbackPage}/>
          </Switch>
        </Router>
      </Auth>
    </div>
    
  );
}

export default App;


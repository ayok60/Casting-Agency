import React, {Component} from "react";
import auth0 from "auth0-js";
import * as jwt_decode from "jwt-decode";


import {AUTH_CONFIG} from "../auth0-variables";
import {AuthProvider} from "../authContext";

const auth = new auth0.WebAuth({
  domain: AUTH_CONFIG.domain,
  clientID: AUTH_CONFIG.clientId,
  redirectUri: AUTH_CONFIG.callbackUrl,
  audience: AUTH_CONFIG.audience,
  responseType: "token id_token"
});

const JWTS_LOCAL_KEY = 'JWTS_LOCAL_KEY';
const JWTS_ACTIVE_INDEX_KEY = 'JWTS_ACTIVE_INDEX_KEY';

class Auth extends Component {
  
  token = ""
  payload;
  id_token = ""


  initiateLogin = () => {
    console.log('initiateLogin')
    auth.authorize();
    console.log('end initiateLogin')
  };

  logout = () => {
    console.log('logout')
    this.setState({
        authenticated: false,
        accessToken: ""
      });
      this.token = '';
      this.payload = null;
      this.set_jwt();
    console.log('end logout')
  };




  handleAuthentication = () => {
    console.log('handleAuthentication')
    auth.parseHash((error, authResult) => {
        if (error) {
          console.log(error);
          console.log(`Error ${error.error} occured`);
          return;
        }
        console.log('accessToken');
        this.token = authResult.accessToken;
        console.log(this.token);
        console.log('Payload');
        this.payload = this.parseJwt(this.token);
        console.log(this.payload);
        console.log('idTokenPayload');
        this.setSession(authResult.idTokenPayload,authResult.accessToken);
        this.set_jwt();
      });
      console.log('end handleAuthentication')

  };

  parseJwt = (token) => {
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));
    return JSON.parse(jsonPayload);
  };

  setSession(idTokenPayload,accessToken) {
    console.log('setSession')
    console.log(idTokenPayload)
    const user = {
        id: idTokenPayload.sub,
        email: idTokenPayload.email,
      };
      this.setState({
        authenticated: true,
        accessToken: accessToken,
        user
      });
      console.log(this.state)
      console.log('end setSession')
  }

  set_jwt = () => {
    localStorage.setItem(JWTS_LOCAL_KEY, this.token);
    if (this.token) {
      this.parseJwt(this.token);
    }
  }

  load_jwts = () => {
    this.token = localStorage.getItem(JWTS_LOCAL_KEY) || null;
    if (this.token) {
      this.parseJwt(this.token);
    }
  }

  activeJWT = () => {
    return this.token;
  }

  render() {
    const authProviderValue = {
      ...this.state,
      initiateLogin: this.initiateLogin,
      handleAuthentication: this.handleAuthentication,
      logout: this.logout
    };
    return (
      <AuthProvider value={authProviderValue}>
        {this.props.children}
      </AuthProvider>
      
    );
  }
}

export default Auth;


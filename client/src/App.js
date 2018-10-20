import React, { Component } from 'react';
import './App.css';
import User from './containers/users/UsersPage'

class App extends Component {
  render() {
    return (
      <div className="App">
        <User></User>
      </div>
    );
  }
}

export default App;

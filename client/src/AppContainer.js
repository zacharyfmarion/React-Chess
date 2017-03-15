import React, { Component, PropTypes } from 'react'
import { SocketProvider } from 'socket.io-react'
import io from 'socket.io-client'
import App from './App'

// default port for a flask app
const socket = io.connect('http://127.0.0.1:5000');
// socket.on('connect', () => console.log("Hello"));

/*
 * A wrapper component for the app which connects it to the socket
 */
export default class AppContainer extends Component {
  render() {
    return (
      <SocketProvider socket={socket}>
        <App />
      </SocketProvider>	
    )	
  }
}

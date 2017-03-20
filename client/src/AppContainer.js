import React, { Component, PropTypes } from 'react'
import { SocketProvider } from 'socket.io-react'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
import { Provider } from 'react-redux'
import { orangeA400 } from 'material-ui/styles/colors'
import getMuiTheme from 'material-ui/styles/getMuiTheme'
import io from 'socket.io-client'
import store from './redux/store'
import colors from './constants/colors'
import App from './App'

// default port for a flask app
const socket = io.connect('http://127.0.0.1:5000');

// Customize our MUI theme
const muiTheme = getMuiTheme({
  palette: {
    primary1Color: colors.primary,
    primary2Color: colors.primary,
    primary3Color: colors.primary,
  },
});

/*
 * A wrapper component for the app which connects it to the socket and to the material-ui
 * theme Provider
 */
export default class AppContainer extends Component {
  render() {
    return (
      <Provider store={store}>
        <SocketProvider socket={socket}>
          <MuiThemeProvider theme={muiTheme}>
            <App />
          </MuiThemeProvider>
        </SocketProvider>	
      </Provider>
    )	
  }
}

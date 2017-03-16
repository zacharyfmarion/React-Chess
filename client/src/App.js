import React, { Component } from 'react'
import AppBar from 'material-ui/AppBar'
import { socketConnect } from 'socket.io-react'
import FlatButton from 'material-ui/FlatButton'
import ChessGame from './ChessGame'
import colors from './constants/colors'
import './App.css'

class App extends Component {

  constructor(props) {
    super(props) 
    this.state = {
      playing: false 
    }
    this.toggleGame = this.toggleGame.bind(this)
  }

  toggleGame() {
    const playing = !this.state.playing
    this.setState({ playing })
    // request a move
    if (playing) {
      this.props.socket.emit('request-move')
    } else {
      this.props.socket.emit('reset-game')
    }
  }

  render() {
    return (
      <div className="App">
        <AppBar 
          title="Material Chess" 
          iconElementRight={
            <FlatButton 
              label={this.state.playing ? "Pause" : "Play"} 
              onTouchTap={this.toggleGame}
            />
          }
          style={{backgroundColor: colors.primary}}
        />
        <div className="App-intro">
          <ChessGame playing={this.state.playing}/>
        </div>
      </div>
    );
  }
}

export default socketConnect(App)

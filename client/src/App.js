import React, { Component } from 'react'
import { socketConnect } from 'socket.io-react'
import { ActionCreators } from 'redux-undo'
import { connect } from 'react-redux'
import Snackbar from 'material-ui/Snackbar'
import ChessGame from './ChessGame'
import CapturedPieces from './CapturedPieces'
import { changeGameState } from './redux/actions/gameActions'
import Header from './Header'
import './App.css'

class App extends Component {

  constructor(props) {
    super(props) 
    this.state = {
      snackbarOpen: false,
      snackbarMsg: '',
    }
    // binding instance methods
    this.toggleGame = this.toggleGame.bind(this)
    this.moveBackward = this.moveBackward.bind(this)
    this.moveForward = this.moveForward.bind(this)
    this.showSnackbar = this.showSnackbar.bind(this)
    this.handleRequestClose = this.handleRequestClose.bind(this)
  }

  componentDidMount() {
    this.props.socket.on('server-ready', () => this.showSnackbar('Server Connected')) 
  }

  moveBackward() {
    if (!this.props.playing) {
      this.props.dispatch(ActionCreators.undo()) 
    }
  }

  moveForward() {
    if (!this.props.playing) {
      this.props.dispatch(ActionCreators.redo()) 
    }
  }

  toggleGame() {
    const playing = !this.props.playing
    this.props.dispatch(changeGameState(playing))
    // request a move
    if (playing) {
      this.props.socket.emit('request-move')
    }
  }

  /* Method to show the snackbar */
  showSnackbar(message) {
    this.setState({ 
      snackbarMsg: message, 
      snackbarOpen: true 
    }) 
  }

  handleRequestClose() {
    this.setState({ snackbarOpen: false }) 
  }

  render() {
    return (
      <div className="App">
        <Header 
          playing={this.props.playing}
          moveForward={this.moveForward} 
          moveBackward={this.moveBackward}
          toggleGame={this.toggleGame}
        />
        <div className="App-intro">
          <ChessGame playing={this.props.playing}></ChessGame>
          <div className="captured-pieces-wrapper">
            <CapturedPieces capturedColor="white" pieces={this.props.captured.black}/>
            <CapturedPieces capturedColor="black" pieces={this.props.captured.white}/>
          </div>
          <Snackbar 
            open={this.state.snackbarOpen}
            message={this.state.snackbarMsg}
            action="Close"
            onActionTouchTap={this.handleRequestClose}
            autoHideDuration={4000}
            onRequestClose={this.handleRequestClose}
          />
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  playing: state.game.present.playing,
  captured: state.game.present.captured,
})

export default connect(
  mapStateToProps
)(socketConnect(App))

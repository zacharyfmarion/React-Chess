import React, { Component, PropTypes } from 'react'
import FlatButton from 'material-ui/FlatButton'

/*
 * A set of controls for the game
 */
export default class GameControls extends Component {

  static propTypes = {
    playing: PropTypes.bool.isRequired,
    toggleGame: PropTypes.func.isRequired,
    resetGame: PropTypes.func.isRequired,
  }

  render() {
    return (
      <FlatButton 
        label={this.props.playing ? "Stop" : "Play"} 
        onTouchTap={this.props.toggleGame}
      />
    )	
  }
}

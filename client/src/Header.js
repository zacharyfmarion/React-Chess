import React, { Component, PropTypes } from 'react'
import IconButton from 'material-ui/IconButton'
import FlatButton from 'material-ui/FlatButton'
import RaisedButton from 'material-ui/RaisedButton'
import { 
  Toolbar, 
  ToolbarGroup, 
  ToolbarSeparator, 
  ToolbarTitle 
} from 'material-ui/Toolbar'
import colors from './constants/colors'

/*
 * Header component for the application
 */
export default class Header extends Component {

  static propTypes = {
    playing: PropTypes.bool.isRequired,
    moveForward: PropTypes.func.isRequired,
    moveBackward: PropTypes.func.isRequired,
    toggleGame: PropTypes.func.isRequired,
  }

  render() {
    return (
      <Toolbar style={{backgroundColor: colors.primary}} >
        <ToolbarTitle text="Material Chess"/>
        <ToolbarGroup lastChild={true}>
          <IconButton 
            iconClassName="material-icons"
            onTouchTap={this.props.moveBackward}
          >
            keyboard_arrow_left
          </IconButton>
          <IconButton 
            iconClassName="material-icons"
            onTouchTap={this.props.moveForward}
          >
            keyboard_arrow_right
          </IconButton>
          <RaisedButton 
            label={this.props.playing ? "Pause" : "Play"} 
            onTouchTap={this.props.toggleGame}
          />
        </ToolbarGroup>
      </Toolbar>
    )	
  }
}

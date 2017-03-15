import React, { Component, PropTypes } from 'react'
import "./tile.css"

/*
 * A single tile on the chessboard - can hold a chesspiece or
 * can be empty. Is either black or white
 */
export default class ChessTile extends Component {

  static propTypes = {
    /* Color is a string - either 'white', or 'black' */
    color: PropTypes.string,
    piece: PropTypes.object,
  }

  static defaultProps = {
    color: 'white',
    piece: null,
  }

  render() {
    const tileClass = 'tile tile-' + this.props.color
    return (
      <div className={tileClass}> {this.props.piece} </div>
    )	
  }
}

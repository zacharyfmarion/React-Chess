import React, { Component, PropTypes } from 'react'
import ChessPiece from './ChessPiece'
import "./tile.css"

/*
 * A single tile on the chessboard - can hold a chesspiece or
 * can be empty. Is either black or white
 */
export default class ChessTile extends Component {

  static propTypes = {
    /* Color is a string - either 'white', or 'black' */
    tileClicked: PropTypes.func.isRequired,
    color: PropTypes.string,
    piece: PropTypes.object,
    highlighted: PropTypes.bool.isRequired,
  }

  static defaultProps = {
    color: 'white',
    piece: null,
  }

  render() {
    const { piece, color } = this.props
    const tileClass = 'tile tile-' + color + (this.props.highlighted ? ' tile-highlighted' : '')
    const tileContents = piece == null ? null : <ChessPiece {...piece}/>
    return (
      <div className={tileClass} onClick={this.props.tileClicked}> 
        {tileContents}
      </div>
    )	
  }
}

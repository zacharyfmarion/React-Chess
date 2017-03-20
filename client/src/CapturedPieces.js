import React, { Component, PropTypes } from 'react'
import ChessPiece from './ChessPiece'

/*
 * Component to hold all the captured pieces for a given color
 */
export default class CapturedPieces extends Component {

  static propTypes = {
    /*
     * The color of the pieces that were captured (so the opposite color of whoever
     * captured the pieces)
     */
    capturedColor: PropTypes.string.isRequired, 
    /*
     * Array of captured pieces, in the from of { color, type }
     */
    pieces: PropTypes.array.isRequired,
  }

  render() {
    const pieces = this.props.pieces.map((piece, i) => {
      return <ChessPiece color={piece.color} type={piece.type} />
    })
    const myColor = this.props.capturedColor == "white" ? "Black's" : "White's"
    return (
      <div className="captured-pieces">
        <h3>{myColor} Captured</h3>
        {pieces} 
      </div>
    )	
  }
}

import React, { Component, PropTypes } from 'react'
import ChessTile from './ChessTile'
import './board.css'

/*
 * A chessboard component
 */
export default class ChessBoard extends Component {

  static propTypes = {
    /*
     * A 2d array of pieces
     */
    pieces: PropTypes.arrayOf(
      PropTypes.arrayOf(
        PropTypes.shape({
          color: PropTypes.string,
          type: PropTypes.string,
        })
      )
    )
  }

  /*
   *  We create the tiles and the initial chess pieces
   */
  setupBoard() {
    let rows = []
    for (let i = 0; i < 8; i++) {
      let row = []
      for (let j = 0; j < 8; j++) {
        const tileColor = ((i + j) % 2 === 0) ? 'white' : 'black'
        row.push(<ChessTile key={[i, j]} color={tileColor} piece={this.props.pieces[i][j]}/>)
      }
      rows.push((<div key={i} className="board-row">{row}</div>))
    }
    return rows
  }

  render() {
    return (
      <div className="board-wrapper">
        <div className="board">{this.setupBoard()}</div>
        <div>Icons made by <a href="http://www.flaticon.com/authors/madebyoliver" title="Madebyoliver">Madebyoliver</a> from <a href="http://www.flaticon.com" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
      </div>
    )	
  }
}

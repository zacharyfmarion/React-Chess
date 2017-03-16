import React, { Component, PropTypes } from 'react'
import { socketConnect } from 'socket.io-react'
import ChessBoard from './ChessBoard'

/*
 * Generate the minimal representation of a chess piece
 */
const Piece = (type, color) => {
  return { type, color }
}

/*
 * A game of chess...maps the board to pieces and updates the state
 * of the board based on the server
 */
class ChessGame extends Component {

  static propTypes = {
    playing: PropTypes.bool.isRequired, 
  }

  constructor(props) {
    super(props)
    this.state = {
      pieces: null, 
    }
    this._executeMove = this._executeMove.bind(this)
    this.getInitialLocations = this.getInitialLocations.bind(this)
  }

  componentWillMount() {
    // initialize the locations of the chess pieces
    this.getInitialLocations()
  }

  componentDidMount() {
    const { socket } = this.props
    // wait for any move that is made to be passed back to the client
    socket.on('move', this._executeMove)
  }

  /*
   * Function called when a move is made to the by the server
   * @param {Object} state - An object containing the start indices
   * @param {Object} end - An object containing the end indices
   */
  _executeMove(start, end) {
    // start and end are both objects with { row: 2, col: 6 }
    const pieces = this.state.pieces.slice()
    const piece = this.state.pieces[start.row][start.col]
    pieces[end.row][end.col] = piece
    pieces[start.row][start.col] = null
    this.setState({ pieces })
    // request the next move as soon as we finish with this one
    if (this.props.playing) {
      this.props.socket.emit('request-move')
    }
  }

  /*
   * Get the initial piece associated with a square on the board
   * @param {Number} i - The row of the piece
   * @param {Number} j - The column of the piece
   * @return {Renderable} A ChessPiece component or null
   */
  getInitialPiece(i, j, key) {
    let piece = null
    const color = i < 2 ? 'white' : 'black'
    if (i === 0 || i === 7) {
      if (j === 0 || j === 7) piece = Piece('rook', color)
      else if (j === 1 || j === 6) piece = Piece('knight', color)
      else if (j === 2 || j === 5) piece = Piece('bishop', color)
      else if (j === 3) {
        const type = color === 'white' ? 'king' : 'queen' 
        piece = Piece(type, color) 
      }
      else if (j === 4) {
        const type = color === 'white' ? 'queen' : 'king' 
        piece = Piece(type, color) 
      }
    } else if (i === 1 || i === 6) {
      piece = Piece('pawn', color) 
    }
    return piece 
  }

  /*
   * Get the initial locations for all of the peices
   */
  getInitialLocations() {
    const pieces = [...new Array(8)].map((x, i) => {
      return [...new Array(8)].map((y, j) => {
        return this.getInitialPiece(i, j, [i, j])
      })
    })
    this.setState({ pieces })
  }


  render() {
    return (
      <ChessBoard pieces={this.state.pieces}/>      	
    )	
  }
}

export default socketConnect(ChessGame)

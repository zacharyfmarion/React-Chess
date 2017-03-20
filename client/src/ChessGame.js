import React, { Component, PropTypes } from 'react'
import { socketConnect } from 'socket.io-react'
import { connect } from 'react-redux'
import { 
  updateCaptured, 
  addMove, 
  updatePieces 
} from './redux/actions/gameActions'
import ChessBoard from './ChessBoard'

/*
 * A game of chess...maps the board to pieces and updates the state
 * of the board based on the server
 */
class ChessGame extends Component {

  static propTypes = {
    playing: PropTypes.bool.isRequired, 
    updateCaptured: PropTypes.func.isRequired,
  }

  constructor(props) {
    super(props)
    this.state = {
      // currently highlighted moves
      highlighted: [] 
    }
    // binding instance methods
    this._executeMove = this._executeMove.bind(this)
    this.getValidMoves = this.getValidMoves.bind(this)
  }

  componentDidMount() {
    const { socket } = this.props
    // wait for any move that is made to be passed back to the client
    socket.on('move', this._executeMove)
  }

  /*
   * Make a call to the server to get the valid moves associated with a 
   * given piece.
   */
  getValidMoves(row, col) {
    this.props.socket.emit('valid-moves', {row, col}, (highlighted) => {
      // console.log(highlighted)
      this.setState({ highlighted })
    })
  }

  /*
   * Function called when a move is made to the by the server
   * @param {Object} state - An object containing the start indices
   * @param {Object} end - An object containing the end indices
   *
   * TODO: THIS SHOULD ALL BE ENCAPSULATED IN REDUX...playing should be a variable
   * in the redux state
   */
  _executeMove(start, end, captured) {
    // console.log("Captured: ", captured)
    this.props.dispatch(addMove({start, end, captured}))
    this.props.dispatch(updateCaptured(captured))
    // start and end are both objects with { row: 2, col: 6 }
    const pieces = this.props.pieces.slice()
    const piece = pieces[start.row][start.col]
    pieces[end.row][end.col] = piece
    pieces[start.row][start.col] = null
    this.props.dispatch(updatePieces(pieces))
    // request the next move as soon as we finish with this one
    if (this.props.playing) {
      this.props.socket.emit('request-move')
    }
  }

  render() {
    return (
      <ChessBoard 
        getValidMoves={this.getValidMoves} 
        highlighted={this.state.highlighted}
        pieces={this.props.pieces}
      />
    )
  }
}

const mapStateToProps = (state) => {
  return {
    pieces: state.game.present.pieces,
  }
}

export default connect(
  mapStateToProps
)(socketConnect(ChessGame))

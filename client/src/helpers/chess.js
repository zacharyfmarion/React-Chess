/*
 * Generate the minimal representation of a chess piece
 */
const Piece = (type, color) => {
  return { type, color }
}

/*
 * Get the initial piece associated with a square on the board
 * @param {Number} i - The row of the piece
 * @param {Number} j - The column of the piece
 * @return {Renderable} A ChessPiece component or null
 */
function getInitialPiece(i, j, key) {
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
export function initializeBoard() {
  return [...new Array(8)].map((x, i) => {
    return [...new Array(8)].map((y, j) => {
      return getInitialPiece(i, j, [i, j])
    })
  })
}

import React, { Component, PropTypes } from 'react'
import './piece.css'

/*
 * A chess piece
 */
export default function ChessPiece({color, type}) {
  const src = `./img/${color}_${type}.png`
  return (
    <img className="piece-img" src={src} alt={type} />
  )
}

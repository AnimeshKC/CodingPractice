import React from "react"
import "./OffsetButton.css"
export default function OffsetButton(props) {
  const { offset, offsetFunction } = props
  let buttonSign = ""
  if (offset > 0) buttonSign = "+"

  function handleClick() {
    offsetFunction(offset)
  }
  const buttonString = `${buttonSign} ${offset}`
  return <button onClick={handleClick}>{buttonString}</button>
}

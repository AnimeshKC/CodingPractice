import React from "react"

export default function OffsetButton(props) {
  const { offset, offsetFunction } = props
  let buttonSign = ""
  if (offset > 0) buttonSign = "+"
  else if (offset < 0) buttonSign = "-"

  function handleClick() {
    offsetFunction(offset)
  }
  const buttonString = `${buttonSign} ${offset}`
  return <button onClick={handleClick}>{buttonString}</button>
}

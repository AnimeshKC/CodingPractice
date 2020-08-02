import React, { useState } from "react"
import "./App.css"
import OffsetButton from "./components/OffsetButton"
function App() {
  const [count, setCount] = useState(0)

  function handleOffset(offsetValue) {
    setCount(count + offsetValue)
  }
  /*
  have state for count and a set count function

  have an increment function that will be passed to the respective buttons


  */
  return (
    <div className="App">
      <div className="buttonContainer">
        <OffsetButton offset={1} offsetFunction={handleOffset}></OffsetButton>
        <OffsetButton offset={-1} offsetFunction={handleOffset}></OffsetButton>
        <OffsetButton offset={10} offsetFunction={handleOffset}></OffsetButton>
        <OffsetButton offset={100} offsetFunction={handleOffset}></OffsetButton>
      </div>
      <div>{count}</div>
    </div>
  )
}

export default App

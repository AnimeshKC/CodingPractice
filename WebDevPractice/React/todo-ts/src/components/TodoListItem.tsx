import React from "react"

interface itemProps {
  text: string
  isComplete: boolean
}
export default function TodoListItem({ text, isComplete }: itemProps) {
  return <div>{`{text}: is {"not" && !isComplete} complete`}</div>
}

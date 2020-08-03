import React from "react"
import Card from "./Card"

export default function CardList(props) {
  const { cards } = props
  return (
    <div id="container" className="mt-10">
      {cards.map((card) => (
        <Card {...card} key={card.id} />
      ))}
    </div>
  )
}

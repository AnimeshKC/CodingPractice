import React, { useState, useRef, useCallback } from "react"
import useBookSearch from "./useBookSearch"

export default function App() {
  const [query, setQuery] = useState("")
  const [pageNumber, setPageNumber] = useState(1)

  const { books, hasMore, loading, error } = useBookSearch(query, pageNumber)

  const observer = useRef()
  const lastBookElementRef = useCallback(
    //node corresponds to the element this is referencing to
    (node) => {
      if (loading) return //don't trigger infinite scrolling while loading
      if (observer.current) observer.current.disconnect() //disconnect the previous observer
      observer.current = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting && hasMore) {
          setPageNumber((prevPageNumber) => prevPageNumber + 1)
        }
      })
      if (node) observer.current.observe(node)
    },
    [loading, hasMore]
  )

  function handleSearch(e) {
    setQuery(e.target.value)
    //data results start at the first page every time a query happens
    setPageNumber(1)
  }

  return (
    <>
      <input type="text" value={query} onChange={handleSearch}></input>
      {books.map((book, index) => {
        //the book works as a key, since useBookSearch uses a set to guarentee each title is unique

        if (books.length === index + 1) {
          return (
            //if last book, set the lastBookElementRef to this element
            <div ref={lastBookElementRef} key={book}>
              {book}
            </div>
          )
        } else {
          return <div key={book}>{book}</div>
        }
      })}
      <div>{loading && "Loading..."}</div>
      <div>{error && "Error"}</div>
    </>
  )
}

import { useEffect, useState } from "react"
import axios from "axios"

export default function useBookSearch(query, pageNumber) {
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(false)
  const [books, setBooks] = useState([])
  const [hasMore, setHasMore] = useState(false)

  useEffect(() => {
    //reset books array with each query.
    setBooks([])
  }, [query])

  useEffect(() => {
    setLoading(true)
    setError(false)
    let cancel //used for axios' cancelling requests
    axios({
      method: "GET",
      url: "http://openlibrary.org/search.json",
      params: { q: query, page: pageNumber },
      cancelToken: new axios.CancelToken((c) => (cancel = c)),
    })
      .then((res) => {
        setBooks((prevBooks) => {
          //use a set to make titles unique; then destructure
          return [
            ...new Set([...prevBooks, ...res.data.docs.map((b) => b.title)]),
          ]
        })
        setHasMore(res.data.docs.length > 0)
        setLoading(false)
      })
      .catch((e) => {
        if (axios.isCancel(e)) return
        setError(true)
      })
    return () => cancel()
  }, [query, pageNumber])

  return { loading, error, books, hasMore }
}

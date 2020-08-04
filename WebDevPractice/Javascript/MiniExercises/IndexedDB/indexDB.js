;(() => {
  "use strict"

  if (!("indexedDB" in window)) {
    console.warn("IndexedDB not supported")
    return
  }

  //...we can safely run IndexedDB code
})()

const express = require("express");
const app = express();
const port = 3000;

app.get("/", (req, res) => {
  res.json([{ name: "Jim", authority: 10 }]);
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});

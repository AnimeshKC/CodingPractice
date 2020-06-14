const io = require("socket.io")(3000)

const users = {}

io.on("connection", (socket) => {
  socket.on("new-user", (name) => {
    //socket.id is unique for each user
    users[socket.id] = name
    socket.broadcast.emit("user-connected", name)
  })
  socket.on("send-chat-message", (message) => {
    //broadcast.emit sends the message to all users except for the user who sent it
    socket.broadcast.emit("chat-message", {
      message: message,
      name: users[socket.id],
    })
  })
  socket.on("disconnect", () => {
    socket.broadcast.emit("user-disconnected", users[socket.id])
    delete users[socket.id]
  })
})

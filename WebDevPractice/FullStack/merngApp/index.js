if (!process.env.NODE_ENV || process.env.NODE_ENV === "development")
  require("dotenv").config()

const { ApolloServer } = require("apollo-server")
const mongoose = require("mongoose")

const typeDefs = require("./graphql/typeDefs")
const resolvers = require("./graphql/resolvers")
const MONGODB = process.env.MONGO_CONNECTION_STRING

const server = new ApolloServer({
  typeDefs,
  resolvers,
})

mongoose
  .connect(MONGODB, { useNewUrlParser: true })
  .then(() => {
    console.log("MongoDB Connected")
    return server.listen({ port: 5000 })
  })
  .then((res) => {
    console.log(`Server running at ${res.url}`)
  })

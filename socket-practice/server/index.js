const {Server} = require('socket.io');

const io = new Server(3000);

io.on('connection', (socket) => {
    //send messages to client
    socket.emit("event1", "message from event 1");

    // receive a message from the client
  socket.on("hello from client", (...args) => {
    console.log('Client -> '+args);
  });
});
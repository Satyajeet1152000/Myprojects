const WebSocket = require('ws');

const PORT = 5000;

const wsServer = new WebSocket.Server({
    port: PORT
});

var appliance_status = {
  Tubelight : "OFF",
  Bulb : "OFF",
  Fan : "OFF",
  Socket1 : "OFF",
}
wsServer.on('connection', function(socket){
    //send feedback to the console
    console.log('A Client just Connected');
    // socket.send("Hiiiiiiii from server.");
    //---------------------send appliance status when client connect 1st-----
          for (const ap_name in appliance_status)
          {
            let sendData = {	
              from : "SERVER",
              room_name :  "Room 1",
              appliance : ap_name,
              status : appliance_status[ap_name], //send saved status
            }
            socket.send(JSON.stringify(sendData));
          }
    //-----------------------------------------------------------------------
  
  
  
    //Attach some behaviour to the incoming socket
    socket.on('message',function(msg){
        console.log("Received from Client:" +msg); 
      
        //broadcast that massage to all connected clients
        wsServer.clients.forEach(function(client)
        {
          var recData = JSON.parse(msg);

          //update appliance status 
          for (const ap_name in appliance_status)
          {
            if(ap_name==recData.appliance){
              appliance_status[ap_name] = recData.status;                  
            }
          }

          let sendData = {	
            from : "SERVER",
            room_name :  recData.room_name,
            appliance : recData.appliance,
            status : appliance_status[recData.appliance], //send saved status
          }
          client.send(JSON.stringify(sendData));
          
        });
      console.log("Appliance Status: "+JSON.stringify(appliance_status))
    });
});
console.log("Server is listining at port:"+PORT);

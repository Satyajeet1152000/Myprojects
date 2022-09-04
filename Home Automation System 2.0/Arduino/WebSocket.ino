#include <ArduinoWebsockets.h>
#include <WiFi.h>
#include <ArduinoJson.h>

#define ESP_NAME "Room 1"
//-----------------Appliances/Relay pins declaration or OUTPUT PINS------------------
#define Tubelight 22
#define Bulb 23
#define Fan 18
#define Socket1 19

//---------------Switches pin declaration or INPUT PINS-------------------
#define switch1 32
#define switch2 33
#define switch3 25
#define switch4 26

//--------------------Network Credentials------------------------------
const char* ssid = "Satyajeet"; //Enter SSID
const char* password = "2334445556"; //Enter Password
const char* websockets_connection_string = "wss://ots-websocket-server.glitch.me"; //Enter server adress

//------------------Eliminate Switch buttons debounce effect--------------------
unsigned long lastDebounceTime = 0;
int debounceDelay = 600;

//------------------------Switches Previous state---------------------
bool switch1_prev_state = HIGH; //here HIGH work as LOW in INPUT_PULLUP pinMode
bool switch2_prev_state = HIGH;
bool switch3_prev_state = HIGH;
bool switch4_prev_state = HIGH;

bool wb_config_state = false;

//------------------------Websocket Variables------------------------------
using namespace websockets;
WebsocketsClient clientt;
StaticJsonDocument<200> doc; //for parsing data sent from server

// This certificate was updated 15.04.2021, issues on Mar 15th 2021, expired on June 13th 2021
const char echo_org_ssl_ca_cert[] PROGMEM = \
"-----BEGIN CERTIFICATE-----\n" \
"MIIEZTCCA02gAwIBAgIQQAF1BIMUpMghjISpDBbN3zANBgkqhkiG9w0BAQsFADA/\n" \
"MSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\n" \
"DkRTVCBSb290IENBIFgzMB4XDTIwMTAwNzE5MjE0MFoXDTIxMDkyOTE5MjE0MFow\n" \
"MjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxCzAJBgNVBAMT\n" \
"AlIzMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuwIVKMz2oJTTDxLs\n" \
"jVWSw/iC8ZmmekKIp10mqrUrucVMsa+Oa/l1yKPXD0eUFFU1V4yeqKI5GfWCPEKp\n" \
"Tm71O8Mu243AsFzzWTjn7c9p8FoLG77AlCQlh/o3cbMT5xys4Zvv2+Q7RVJFlqnB\n" \
"U840yFLuta7tj95gcOKlVKu2bQ6XpUA0ayvTvGbrZjR8+muLj1cpmfgwF126cm/7\n" \
"gcWt0oZYPRfH5wm78Sv3htzB2nFd1EbjzK0lwYi8YGd1ZrPxGPeiXOZT/zqItkel\n" \
"/xMY6pgJdz+dU/nPAeX1pnAXFK9jpP+Zs5Od3FOnBv5IhR2haa4ldbsTzFID9e1R\n" \
"oYvbFQIDAQABo4IBaDCCAWQwEgYDVR0TAQH/BAgwBgEB/wIBADAOBgNVHQ8BAf8E\n" \
"BAMCAYYwSwYIKwYBBQUHAQEEPzA9MDsGCCsGAQUFBzAChi9odHRwOi8vYXBwcy5p\n" \
"ZGVudHJ1c3QuY29tL3Jvb3RzL2RzdHJvb3RjYXgzLnA3YzAfBgNVHSMEGDAWgBTE\n" \
"p7Gkeyxx+tvhS5B1/8QVYIWJEDBUBgNVHSAETTBLMAgGBmeBDAECATA/BgsrBgEE\n" \
"AYLfEwEBATAwMC4GCCsGAQUFBwIBFiJodHRwOi8vY3BzLnJvb3QteDEubGV0c2Vu\n" \
"Y3J5cHQub3JnMDwGA1UdHwQ1MDMwMaAvoC2GK2h0dHA6Ly9jcmwuaWRlbnRydXN0\n" \
"LmNvbS9EU1RST09UQ0FYM0NSTC5jcmwwHQYDVR0OBBYEFBQusxe3WFbLrlAJQOYf\n" \
"r52LFMLGMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjANBgkqhkiG9w0B\n" \
"AQsFAAOCAQEA2UzgyfWEiDcx27sT4rP8i2tiEmxYt0l+PAK3qB8oYevO4C5z70kH\n" \
"ejWEHx2taPDY/laBL21/WKZuNTYQHHPD5b1tXgHXbnL7KqC401dk5VvCadTQsvd8\n" \
"S8MXjohyc9z9/G2948kLjmE6Flh9dDYrVYA9x2O+hEPGOaEOa1eePynBgPayvUfL\n" \
"qjBstzLhWVQLGAkXXmNs+5ZnPBxzDJOLxhF2JIbeQAcH5H0tZrUlo5ZYyOqA7s9p\n" \
"O5b85o3AM/OJ+CktFBQtfvBhcJVd9wvlwPsk+uyOy2HI7mNxKKgsBTt375teA2Tw\n" \
"UdHkhVNcsAKX1H7GNNLOEADksd86wuoXvg==\n" \
"-----END CERTIFICATE-----\n";

void onMessageCallback(WebsocketsMessage message)//get messages From server
{
    Serial.print("Got Message: ");
    Serial.println(message.data());

    // Deserialize the JSON document
    DeserializationError error = deserializeJson(doc, message.data());
  
    // Test if parsing succeeds.
    if (error){
      Serial.print(F("deserializeJson() failed: "));
      Serial.println(error.f_str());
      return;
    }

    //store status of appliance
    bool sts = doc["status"]=="ON"?LOW:HIGH; //here relay work in reverse
    if(doc["room_name"] == ESP_NAME)
    {
      if(doc["appliance"] == "Tubelight")
      {
        digitalWrite(Tubelight, sts);
      }
      else if(doc["appliance"] == "Bulb")
      {
        digitalWrite(Bulb, sts);
      }
      else if(doc["appliance"] == "Fan")
      {
        digitalWrite(Fan, sts);
      }
      else if(doc["appliance"] == "Socket1")
      {
        digitalWrite(Socket1, sts);
      }
    }
    else
    {
      Serial.println("False Room Name");
    }
}

void onEventsCallback(WebsocketsEvent event, String data) {
    if(event == WebsocketsEvent::ConnectionOpened) {
        Serial.println("Connnection Opened");
    } else if(event == WebsocketsEvent::ConnectionClosed) {
        Serial.println("Connnection Closed");
        wb_config_state = false;
//        clientt.connect(websockets_connection_string);
    } else if(event == WebsocketsEvent::GotPing) {
        Serial.println("Got a Ping!");
    } else if(event == WebsocketsEvent::GotPong) {
        Serial.println("Got a Pong!");
    }
}
void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password); //Connecting to wifi
    while(WiFi.status() != WL_CONNECTED)
    {
      Serial.print(".");
      delay(200);
    }
    Serial.println("\nSuccessfully Connected with WiFi.");
     
    //-------------------Pinmode Setup----------------------
    //for relay or output
    pinMode(Tubelight, OUTPUT);
    pinMode(Bulb, OUTPUT);
    pinMode(Fan, OUTPUT);
    pinMode(Socket1, OUTPUT);

    //pinMode for Switches
    pinMode(switch1, INPUT_PULLUP);
    pinMode(switch2, INPUT_PULLUP);
    pinMode(switch3, INPUT_PULLUP);
    pinMode(switch4, INPUT_PULLUP);

    //-----------Prevent relay from jump start----------------
    digitalWrite(Tubelight, HIGH);
    digitalWrite(Bulb, HIGH);
    digitalWrite(Fan, HIGH);
    digitalWrite(Socket1, HIGH);
}

void loop() 
{
  if(WiFi.status() == WL_CONNECTED)
  {
    if(wb_config_state==false){
      wb_config();
      wb_config_state = true;
    }else{clientt.poll();}
  }
  else{
    WiFi.reconnect();
  }
    mannual(); 
}
void wb_config()
{
  //--------------------Websocket communication establishment-------------------
    clientt.onMessage(onMessageCallback);// run callback when messages are received
    clientt.onEvent(onEventsCallback);// run callback when events are occuring
    clientt.setCACert(echo_org_ssl_ca_cert);// Before connecting, set the ssl fingerprint of the server
    clientt.addHeader("User-Agent", "Satya");//Add header
    clientt.connect(websockets_connection_string);// Connect to server
    clientt.ping();// Send a ping
}
void mannual()
{
  //--------------------------------Switch 1----------------------------------
  if((digitalRead(switch1)==HIGH)&& switch1_prev_state==LOW && debounce())
  {
//    Serial.println("Switch 1 / Tubelight --> OFF");
    build_send_data("Tubelight", "OFF");
    digitalWrite(Tubelight, HIGH);
    switch1_prev_state = HIGH;
    lastDebounceTime = millis();
  }
  if(digitalRead(switch1)==LOW && switch1_prev_state==HIGH && debounce())
  {
//    Serial.println("Switch 1 / Tubelight --> ON");
    build_send_data("Tubelight", "ON");
    digitalWrite(Tubelight, LOW);
    switch1_prev_state = LOW;
    lastDebounceTime = millis();
  }
  
  //--------------------------------Switch 2----------------------------------
  if((digitalRead(switch2)==HIGH)&& switch2_prev_state==LOW && debounce())
  {
//    Serial.println("Switch 2 / Bulb --> OFF");
    build_send_data("Bulb", "OFF");
    digitalWrite(Bulb, HIGH);
    switch2_prev_state = HIGH;
    lastDebounceTime = millis();
  }
  if(digitalRead(switch2)==LOW && switch2_prev_state==HIGH && debounce())
  {
//    Serial.println("Switch 2 / Bulb --> ON");
    build_send_data("Bulb", "ON");
    digitalWrite(Bulb, LOW);
    switch2_prev_state = LOW;
    lastDebounceTime = millis();
  }

  //--------------------------------Switch 3----------------------------------
  if((digitalRead(switch3)==HIGH)&& switch3_prev_state==LOW && debounce())
  {
//    Serial.println("Switch 3 / Fan --> OFF");
    build_send_data("Fan", "OFF");
    digitalWrite(Fan, HIGH);
    switch3_prev_state = HIGH;
    lastDebounceTime = millis();
  }
  if(digitalRead(switch3)==LOW && switch3_prev_state==HIGH && debounce())
  {
//    Serial.println("Switch 3 / Fan --> ON");
    build_send_data("Fan", "ON");
    digitalWrite(Fan, LOW);
    switch3_prev_state = LOW;
    lastDebounceTime = millis();
  }

  //--------------------------------Switch 4----------------------------------
  if((digitalRead(switch4)==HIGH)&& switch4_prev_state==LOW && debounce())
  {
//    Serial.println("Switch 4 / Socket1 --> OFF");
    build_send_data("Socket1", "OFF");
    digitalWrite(Socket1, HIGH);
    switch4_prev_state = HIGH;
    lastDebounceTime = millis();
  }
  if(digitalRead(switch4)==LOW && switch4_prev_state==HIGH && debounce())
  {
//    Serial.println("Switch 4 / Socket1 --> ON");
    build_send_data("Socket1", "ON");
    digitalWrite(Socket1, LOW);
    switch4_prev_state = LOW;
    lastDebounceTime = millis();
  }
}
void build_send_data(String appliance, String sts)
{
  if(WiFi.status() == WL_CONNECTED)
  {
    doc["from"] = "ESP32";
    doc["client_name"] = ESP_NAME;
    doc["room_name"] = "Room 1";
    doc["appliance"] = appliance;
    doc["status"] = sts; 
  
    String send_data;
    serializeJson(doc, send_data);
  
    Serial.print("Send Message : ");
    Serial.println(send_data);
  
    clientt.send(send_data);
  }
}
bool debounce()
{
  return ((millis() - lastDebounceTime)> debounceDelay);
}



#include <HTTPClient.h>
#include <WiFi.h> 

//-------------------Access point credentials-------------------------
const char* ssid = "xxxxxxxxxxxxx";
const char* pwd = "xxxxxxxxxxxxx";
const char* host = "https://onetouchsolutions.000webhostapp.com/database/get_status.php/";
// const char* send_data = "dbupdate.php/";
// const char* receive_data = "get_status.php/"


//-------------------Structure declaration----------------
struct btn_dtl
{
  int bt;  //touchpad or input pin
  int lt;  //led or output pin

  String btn_name;
  int state;
  int reading;
  int previous;
  unsigned long timer;
};

//---------------------initial values---------------------------
btn_dtl button[4] = {
  {12, 32, "switch1", LOW, LOW, LOW, 0}, //1st switch dtl
  {13, 33, "switch2", LOW, LOW, LOW, 0}, //2n switch dtl
  {14, 22, "switch3", LOW, LOW, LOW, 0}, //3rd switch dtl
  {15, 23, "switch4", LOW, LOW, LOW, 0} //4th switch dtl
};
//------------------------------------------------------------
long debounce = 350;
String room = "room1";
 HTTPClient http;

//----------------------SETUP------------------------------
void setup()
{

  Serial.begin(115200);
  delay(20);

  //------PinMode declaration--------
  pinMode(button[0].bt, INPUT);
  pinMode(button[0].lt, OUTPUT);

  pinMode(button[1].bt, INPUT);
  pinMode(button[1].lt, OUTPUT);

  pinMode(button[2].bt, INPUT);
  pinMode(button[2].lt, OUTPUT);

  pinMode(button[3].bt, INPUT);
  pinMode(button[3].lt, OUTPUT);

  //----------Connect to Internet/WiFi----------------
  WiFi.mode(WIFI_OFF);        //Prevents reconnection issue (taking too long to connect)
  delay(1000);
  WiFi.mode(WIFI_STA);        //This line hides the viewing of ESP as wifi hotspot

  WiFi.begin(ssid, pwd);
  Serial.println("");
  Serial.println("Connecting");
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
}

//---------------------------LOOP-----------------------------
void loop()
{
  //call_test();
  get_device_status(0);
  delay(50);  
  get_device_status(1);
  delay(50);  
  get_device_status(2);
  delay(50);  
  get_device_status(3); 
  delay(50);      
} 
void get_device_status(int n)
{
  http.begin(host);
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");

  String httpRequestData = "room=" + room + "&device=" + button[n].btn_name;
  String payload;
 

   int httpResponseCode = http.POST(httpRequestData);

  Serial.println("request ->>  "+httpRequestData);
  
  payload = http.getString();
  
  Serial.println(payload+"<--response");
  if(payload=="1  ")
  {
    Serial.println(button[n].btn_name+" is ON");
    button[n].state = HIGH;
    digitalWrite(button[n].lt, HIGH);
  }
  else if(payload=="0  ")
  {
    Serial.println(button[n].btn_name+" is Off");
    button[n].state = LOW;
    digitalWrite(button[n].lt, LOW);
  }
//  else 
//  {
//    Serial.println("cantttttttt");
//  }
  http.end(); 
}

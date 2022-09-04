#include <HTTPClient.h>
#include <WiFi.h>

//-------------------Access point credentials-------------------------
const char* ssid = "xxxxxxx";
const char* pwd = "xxxxxxxx";
const char* host = "https://onetouchsolutions.000webhostapp.com/database/dbupdate.php/";
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

//----------------------SETUP-----------------------------------------------------------------------------
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
    delay(300);
    Serial.print(".");
  }
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
}

//---------------------------LOOP-----------------------------
void loop()
{
  for (int i = 0; i < 4; i++)
  {
    btn_control(i);
  }
  delay(100);
}

//-----------------------*************----------------------------
//-------------------****  FUNCTIONS  ****------------------------
//-----------------------*************----------------------------

void btn_control(int n)		//<--------------Button Control Function-------------
{
  button[n].reading = digitalRead(button[n].bt);
  if (button[n].reading == HIGH && button[n].previous == LOW && millis() - button[n].timer > debounce)
  {
    if (button[n].state == HIGH)
    {
      button[n].state = LOW;
      digitalWrite(button[n].lt, button[n].state);
      send_to_db(n);
      Serial.print("Button ");
      Serial.print(n + 1);
      Serial.println("  Off");
    }
    else
    {
      button[n].state = HIGH;
      digitalWrite(button[n].lt, button[n].state);
      send_to_db(n);
      Serial.print("Button ");
      Serial.print(n + 1);
      Serial.println("  On");
    }
    button[n].timer = millis();
  }
  digitalWrite(button[n].lt, button[n].state);
  button[n].previous = button[n].reading;
}

void send_to_db(int n)		//<-----------Send values to Database---------------
{
  http.begin(host);
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");

  String httpRequestData = "room=" + room + "&device=" + button[n].btn_name + "&value=" + String(button[n].state);

  Serial.print("httpRequestData: ");
  Serial.println(httpRequestData);

  int httpResponseCode = http.POST(httpRequestData);
  
  String payload = http.getString();

  if (httpResponseCode > 0)
  {
    Serial.println(payload);
  }
  else {
    Serial.println(payload);
  }
  delay(100);
  http.end();
}

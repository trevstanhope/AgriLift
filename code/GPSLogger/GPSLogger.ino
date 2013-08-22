/* --- Header --- */
#include <SoftwareSerial.h>
#include <SD.h>
#define SD_PIN 10
#define GPS_TX_PIN 2 // TxD jumper position on shield
#define GPS_RX_PIN 3 // RxD jumper position on shield
#define BAUD 9600

/* --- Declarations --- */
SoftwareSerial gps(GPS_TX_PIN, GPS_RX_PIN);

/* --- Setup --- */
void setup() {
  Serial.begin(BAUD);
  pinMode(SD_PIN, OUTPUT);
  SD.begin(SD_PIN);
  gps.begin(BAUD);
}

/* --- Loop --- */
void loop() {
  char index = 0;
  char temp = 0;
  String dataString = "";
  File dataFile = SD.open("datalog.txt", FILE_WRITE);
  if (true) {
    while(gps.available()) {
      temp = gps.read();
      dataString += String(temp);
      index++;
      if (index > 200) {
        break;
      }
    }
  }
  if (dataString != "") {
    Serial.println(dataString);
  }
  dataFile.print(dataString);
  dataFile.close();
}


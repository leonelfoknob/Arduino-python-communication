#include <Wire.h>
#include <Adafruit_BMP085.h>
#define seaLevelPressure_hPa 1013.25

   float Temperature;
   float Pressure;
   float Altitude;
   float ReadSealevelPressure;
   float Real_altitude;
   float data[6];

Adafruit_BMP085 bmp;
  
void setup() {
  Serial.begin(9600);
  if (!bmp.begin()) {
  Serial.println("Could not find a valid BMP085 sensor, check wiring!");
  while (1) {}
  }
}
  
void loop() {
   //check sensor value
   
   Temperature =bmp.readTemperature();
   Pressure =bmp.readPressure();
   Altitude=bmp.readAltitude();
   ReadSealevelPressure =bmp.readSealevelPressure();
   Real_altitude =bmp.readAltitude(seaLevelPressure_hPa * 100);
   
   //save data in table
   
   data[0] = Temperature;
   data[1] = Pressure;
   data[2] = Altitude;
   data[3] = ReadSealevelPressure;
   data[4] = Real_altitude;
   
    /*Serial.print(bmp.readTemperature());
    Serial.println(" *C");
    
    Serial.print("Pressure = ");
    Serial.print(bmp.readPressure());
    Serial.println(" Pa");

    Serial.print("Altitude = ");
    Serial.print(bmp.readAltitude());
    Serial.println(" meters");

    Serial.print("Pressure at sealevel (calculated) = ");
    Serial.print(bmp.readSealevelPressure());
    Serial.println(" Pa");

    Serial.print("Real altitude = ");
    Serial.print(bmp.readAltitude(seaLevelPressure_hPa * 100));
    Serial.println(" meters");
    
    Serial.println();*/
    /*Serial.print(data[0]);
    Serial.print(" ");
    Serial.print(data[1]);
    Serial.print(" ");*/
    Serial.print(data[2]);
    /*Serial.print(" ");
    Serial.print(data[3]);
    Serial.print(" ");
    Serial.print(data[4]);*/
    delay(1000);
}

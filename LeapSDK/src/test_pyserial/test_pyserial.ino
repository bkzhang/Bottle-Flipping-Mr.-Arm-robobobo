// piserial to arduino
// intermediate forward to bt

#include <SoftwareSerial.h>

SoftwareSerial bluetooth(2,3);


char c;

void setup() {
  Serial.begin(9600); 
  
}

void loop() {
  
 if (Serial.available() > 0){
   c = Serial.read();
   Serial.println(c);
   
   int i = c;
   Serial.println("conversion");
   Serial.println(i);
   
   // forward to other arduino
   bluetooth.write(c);
 } 
  
}

// Intermediate forwarding arduino from PC to RobotArm controller


// piserial to arduino
// intermediate forward to bt

#include <SoftwareSerial.h>

SoftwareSerial bluetooth(2,3);

char c;

void setup() {
  Serial.begin(9600); 
  bluetooth.begin(38400);
}

void loop() {
  
 // Receive byte from pyserial
 if (Serial.available() > 0){
   c = Serial.read();
   // forward to the other arduino
   bluetooth.write(c);
 } 
  
}

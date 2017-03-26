// arduino to arduino via bt
// receiveing bt


#include <SoftwareSerial.h>

SoftwareSerial bluetooth(2,3);

char c;

int array[5];

void setup() {
  Serial.begin(9600);
  
}



void loop() {
  
  if (bluetooth.available() > 0) {
    c = bluetooth.read();  
  }
  
}

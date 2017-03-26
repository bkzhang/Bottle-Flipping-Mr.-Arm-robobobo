#include <Servo.h>

Servo servo;

void setup() {
  Serial.begin(9600);
  servo.attach(9); 

}

void loop() {
  
  servo.write(50);
  delay(1000);
  servo.write(0);
  delay(1000);
  //delay(1000);
  //servo.write(50);
  
}

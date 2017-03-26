#include <Servo.h>

Servo servo;

void setup() {
  Serial.begin(9600);
  servo.attach(7); 

}

void loop() {
  
  servo.write(0);
  delay(1000);
  //delay(1000);
  //servo.write(150);
  //delay(1000);
  
  for (int i = 0; i < 180; i++) {
    //servo.write(i);
    delay(30);
  }
}

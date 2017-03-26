#include <Servo.h>

const int NUM_SERVOS = 6;

Servo servo_array[NUM_SERVOS];

void setup() {
  
  for (int i = 0; i < NUM_SERVOS; i++) {
    servo_array[i].attach(9);
  }
  
}

void loop() {
  
  // Read in string from bluetooth serial
  
  // Parse the string with Bao's code
  
  for (int i = 0; i < NUM_SERVOS; i++) {
    
  }
    
}

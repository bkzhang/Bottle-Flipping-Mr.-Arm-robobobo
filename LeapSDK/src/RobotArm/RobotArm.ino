#include <Servo.h>
#include <SoftwareSerial.h>

#define SERIAL 1



// Arduino RX = 2 to HC TX
// Arduino TX = 3 to HC RX
//SoftwareSerial bluetooth(2,3);

const int NUM_SERVOS = 6;
const int servo_pin_nums[NUM_SERVOS] = {4,5,6,7,8,9}; // pwm on mega
Servo servo_array[NUM_SERVOS];
// Default values to be determined
const int default_servo_angles[NUM_SERVOS] = {0,0,0,0,0,0};
int servo_angles[NUM_SERVOS];

char c;

void reset_servos() {
  for (int i = 0; i < NUM_SERVOS; i++) {
    servo_array[i].write(default_servo_angles[i]);
  }
}

void setup() {
  
  Serial.begin(9600);
  //bluetooth.begin(38400);
  
  for (int i = 0; i < NUM_SERVOS; i++) {
    servo_array[i].attach(servo_pin_nums[i]);
  }
  reset_servos();
}

int byte_counter = 0;
  
void loop() {
  
  // Read in bytes from pyserial
  byte_counter = 0;
  while (Serial.available() > 0) {
      c = Serial.read();
      int i = c;
      Serial.print("Converted: ");
      Serial.println(i);
      servo_angles[byte_counter] = c;
      byte_counter++;   
  }
  
  // Read in bytes from bluetooth serial
  
  /*
  byte_counter = 0;
  while(bluetooth.available() > 0) {
      c = bluetooth.read();
      int i = 0;
      servo_angles[byte_counter] = c;
      byte_counter++;
  }
  */
  
  for (int i = 0; i < NUM_SERVOS; i++) {
    servo_array[i].write(servo_angles[i]); 
  }
    
}

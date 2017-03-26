#include <Servo.h>
#include <SoftwareSerial.h>

const int NUM_SERVOS = 6;
const int servo_pin_nums[NUM_SERVOS] = {4,5,6,7,8,9};
const int default_servo_angles[NUM_SERVOS] = {0,0,0,0,0,0};
Servo servo_array[NUM_SERVOS];
int servo_angles[NUM_SERVOS];

void reset_servos() {
	for (int i = 0; i < NUM_SERVOS; i++) {
		servo_array[i].write(0);
	}
}

void setup() {
	Serial.begin(9600);
	for (int i = 0; i < NUM_SERVOS; i++) {
		servo_array[i].attach(servo_pin_nums[i]);
	}
	reset_servos();
}

void loop() {
	if (Serial.available() > 0) {
		int input = Serial.parseInt();
		for (int i = 0; i < NUM_SERVOS; i++) {
			servo_array[i].write(input);	
			Serial.print(servo_angles[i]);
		}
	}
}

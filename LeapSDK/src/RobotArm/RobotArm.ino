#include <Servo.h>
#include <SoftwareSerial.h>

const int NUM_SERVOS = 6;
const int servo_pin_nums[NUM_SERVOS] = {4,5,6,7,8,9};
const int default_servo_angles[NUM_SERVOS] = {0,0,0,0,0,0};
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;
int servo_angles[NUM_SERVOS];

void reset_servos() {
        /*
	for (int i = 0; i < NUM_SERVOS; i++) {
		servo_array[i].write(0);
	}*/
}

void setup() {
	Serial.begin(9600);
	/*
        for (int i = 0; i < NUM_SERVOS; i++) {
		servo_array[i].attach(servo_pin_nums[i]);
	}*/
        servo1.attach(4);
        servo2.attach(5);
        servo3.attach(6);
        servo4.attach(7);
        servo5.attach(8);
        servo6.attach(9);
	reset_servos();
}

void loop() {
	if (Serial.available() > 0) {
		int input = Serial.parseInt();
     
		for (int i = 0; i < NUM_SERVOS; i++) {
                        Serial.print(input);
                        if (i = 0) servo1.write(input);
                        else if (i = 1) servo2.write(input);
                        else if (i = 2) servo3.write(input);
                        else if (i = 3) servo4.write(input);
                        else if (i = 4) servo5.write(input);
                        else if (i = 5) servo6.write(input);
			//servo_array[i].write(input);	
			//Serial.print(servo_angles[i]);
		}
	}
}

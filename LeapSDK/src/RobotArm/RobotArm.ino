#include <Servo.h>
#include <SoftwareSerial.h>

const int NUM_SERVOS = 6;
const int servo_pin_nums[NUM_SERVOS] = {4,5,6,7,8,9};
const int default_servo_angles[NUM_SERVOS] = {0,0,20,0,0,0};
Servo servo_array[NUM_SERVOS];
int servo_angles[NUM_SERVOS];

Servo servo0;
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;


int pos = 1;
String getValue(String data, char separator, int index){    //Credits: http://stackoverflow.com/questions/9072320/split-string-into-string-array. Return a substring at index separated by separator
  int found = 0;
  int strIndex[] = {0, -1};
  int maxIndex = data.length()-1;

  for(int i=0; i<=maxIndex && found<=index; i++){
    if(data.charAt(i)==separator || i==maxIndex){
        found++;
        strIndex[0] = strIndex[1]+1;
        strIndex[1] = (i == maxIndex) ? i+1 : i;
    }
  }

  return found>index ? data.substring(strIndex[0], strIndex[1]) : "";
}

void setup() {
  Serial.begin(9600);

  servo0.attach(4);
  servo1.attach(5);
  servo2.attach(6);
  servo3.attach(7);
  servo4.attach(8);
  servo5.attach(9);
  
  servo0.write(0);
  servo1.write(0);
  servo2.write(20);
  servo3.write(0);
  servo4.write(0);
  servo5.write(0);
  

}

void loop() {
  
	if (Serial.available() > 0) {
		String input = Serial.readString();
                int angle = 0;
                Serial.print(input);

                angle = getValue(input, ' ', 0).toInt();     
                servo0.write(angle);
                
                angle = getValue(input, ' ', 1).toInt();     
                servo1.write(angle);
                
                angle = getValue(input, ' ', 2).toInt();     
                servo2.write(angle);
                
                angle = getValue(input, ' ', 3).toInt();     
                servo3.write(angle);
                
                angle = getValue(input, ' ', 4).toInt();     
                servo4.write(angle);
                
                angle = getValue(input, ' ', 5).toInt();     
                servo5.write(angle);
                
                delay(20);
               
    }
    
}

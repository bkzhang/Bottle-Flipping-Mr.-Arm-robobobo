SpaceArm
========

Made during McGill's Robohacks, the SpaceArm project is a scaled down and simplified prototype of a robotic arm designed to simplify object manipulation in outerspace.

### Team members
[Henry Wang](https://github.com/h397wang "Github") - Waterloo University **_Computer Engineering_**  
[Haowie Zhao](https://github.com/HaoyiZhao "Github") - McGill University **_Computer Science_**  
[Brian Zhang](https://github.com/bkzhang "Github") - Carleton University **_Software Engineering_**  
[Richard Salas](https://github.com/richard-salaschavez "Github") - University of Toronto **_Mechanical Engineering_**  
Mike Zhang - University of Toronto **_Mechanical Engineering_**  
Duy-Bao Nguyen - McGill University  

### Specifications
###### Software
1. Leap Motion V2
2. Ino (Arduino) 
3. Python
4. Jupyter Notebook
5. SolidWorks
###### Hardware
1. Mega Arduino 2560
2. 5 Servo Motors
3. Leap Motion Sensor
4. Acrylic
5. Bread Board

### Design and Build 
The robot arm was designed on SolidWorks and assembled by hand. The arm mostly composed of laser cut acrylic glass. The base of the arm has two servo motors, the body has two more and the pincers has the remaining one. The microcontroller used to control the robot arm is the Mega Arduino 2560 where pints 5 through 9 were used to rotate the motors. 

Leap Motion was used to gather the wrist and finger positional data and feed it to the Arduino via python scripts where it would then use the gathered data to rotate the motors in relation to the wrist and finger movements using inverse kinematics calculations. The information was fed through a serial connection. SpaceArm's pincers close and open when the right fist closes or opens and when the left hand is presented, SpaceArm resets all it's motor positions to 0 - where its two major parts are perpendicular to each other.

### Testing
The movement of SpaceArm was made through various test scripts that automated motor movement. After the arm properly moved accordingly, it was connected to Leap Motion. The desired movement of the Arm compared to the user's arm was tested by printing out the data into a csv file to then graph using matplotlib and Jupyter Notebooks. Using this data, the inverse kinematics calculations were adjusted accordingly.

### Problems encountered
We encountered a LOT of problems, and most of them near demo.
1. Leap Motion Orion is Windows only and we were more or less developing exclusively in Unix environments and had to resort to using a previous version of Leap Motion (V2).
2. The only laptop that could pair with the bluetooth shield of the Arduino could not actually connect to it so we resorted to using serial as time constraint would not permit an extensive fix for this.
3. The Arduino only properly processed inputs with a delay of 1.6 seconds so we fixed the python script to sleep 1.6 seconds after every output. 
###### One hour till demo
4. The batteries could not handle the volts required to run the motors so we switched to a power adaptor.
5. The lower body became unglued so we drilled a hole to more securely attach it.
6. The servo motor died so we reassembled the pieces to replace the servo motor.
7. The adaptor wires weren't functioning. We confirmed it by testing out its output voltage so we cut the wires before reattaching them.
###### Yay it works

[Devpost](https://devpost.com/software/roboarm-b73mkp)

<a href="https://github.com/bkzhang/SpaceArm/blob/master/img/moving.gif"><img src="https://github.com/bkzhang/SpaceArm/blob/master/img/moving.gif" align="left" width="200" ></a><a href="https://github.com/bkzhang/SpaceArm/blob/master/img/open.jpeg"><img src="https://github.com/bkzhang/SpaceArm/blob/master/img/open.jpeg" align="left" width="200" ></a><a href="https://github.com/bkzhang/SpaceArm/blob/master/img/closed-arm.jpeg"><img src="https://github.com/bkzhang/SpaceArm/blob/master/img/closed-arm.jpeg" align="left" width="200" ></a><a href="https://github.com/bkzhang/SpaceArm/blob/master/img/robo1.jpeg"><img src="https://github.com/bkzhang/SpaceArm/blob/master/img/robo1.jpeg" align="left" width="48" ></a>

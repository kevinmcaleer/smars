/*
This is a sketch for the Adafruit assembled Motor Shield for Arduino v2
It won't work with v1.x motor shields! Only for the v2's with built in PWM
control

For use with the Adafruit Motor Shield v2
---->  http://www.adafruit.com/products/1438
*/

#include <Wire.h>
#include <Adafruit_MotorShield.h>

// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMS = Adafruit_MotorShield();
// Or, create it with a different I2C address (say for stacking)
// Adafruit_MotorShield AFMS = Adafruit_MotorShield(0x61);

// Select which 'port' M1, M2, M3 or M4. In this case, M1 and M2
Adafruit_DCMotor *MotorL = AFMS.getMotor(1);
Adafruit_DCMotor *MotorR = AFMS.getMotor(2);
// You can also make another motor on port M3
//Adafruit_DCMotor *myOtherMotor = AFMS.getMotor(3);

//ultrasonic setup:
 int distancecm=0;
 const int trigPin = 10; // trig pin connected to Arduino's pin 10
 const int echoPin = 11; // echo pin connected to Arduino's pin 11
// defines variables
long duration;
int distance;

void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Adafruit Motorshield v2 - DC Motor with ultrasonic sensor!");
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  AFMS.begin();  // create with the default frequency 1.6KHz
  //AFMS.begin(1000);  // OR with a different frequency, say 1KHz

  // Set the speed to start, from 0 (off) to 255 (max speed)
  // sometimes the motors don't have the same speed, so use these values tomake your SMARS move straight
  MotorL->setSpeed(150);
  MotorR->setSpeed(150);
  MotorL->run(FORWARD);
  MotorR->run(FORWARD);
  // turn on motor
  MotorL->run(RELEASE);
  MotorR->run(RELEASE);
}

// main program loop
void loop() {

 distancecm=mdistance();   //if the distance is less than 5cm, SMARS will go backward for 1 second, and turn right for 1 second
  if(distance<5){
    MotorL->run(BACKWARD);
    MotorR->run(BACKWARD);
    delay(1000);
    MotorL->run(FORWARD);
    MotorR->run(BACKWARD);
    delay(1000);
  }
  else {
    MotorL->run(FORWARD); //otherwise it will continue forward
    MotorR->run(FORWARD);
  }
}

//ultrasonic distance mesurement function
int mdistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance= duration*0.034/2;
  // Prints the distance on the Serial Monitor
  Serial.print("Distance: ");
}

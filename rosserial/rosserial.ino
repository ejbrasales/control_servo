#if (ARDUINO >= 100)
 #include <Arduino.h>
#else
 #include <WProgram.h>
#endif

#include <Servo.h> 
#include <ros.h>
#include <std_msgs/UInt16.h>
#include <std_msgs/String.h>

ros::NodeHandle  nh;

Servo servo;

const int pinSensor = A0;
const int pin13 = 13;
const int pin8 = 8;

int ValorSensor = 0;
int temperatura = 0;


std_msgs::UInt16 str_msg;
ros::Publisher pub("sensor", &str_msg);


void servo_cb( const std_msgs::UInt16& cmd_msg){
  servo.write(cmd_msg.data); //set servo angle, should be from 0-180  
}


ros::Subscriber<std_msgs::UInt16> sub("servo_control", servo_cb);

void setup(){
  
  pinMode(pin13, OUTPUT);
  pinMode(pin8, OUTPUT);

  nh.initNode();
  nh.subscribe(sub);
  nh.advertise(pub);
  
  servo.attach(9); //attach it to pin 9
}

void loop(){
  ValorSensor = analogRead (pinSensor);
  int milivolts = (ValorSensor / 1023.0) * 5000;
  temperatura = milivolts/ 10;
  str_msg.data = temperatura;
  pub.publish( &str_msg );
  nh.spinOnce();
  delay(1000);
}

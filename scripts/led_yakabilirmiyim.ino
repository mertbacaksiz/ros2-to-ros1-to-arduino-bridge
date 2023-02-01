#include <ros.h>
#include <std_msgs/Float64.h> 
ros::NodeHandle nh;


void led_yak(){
 digitalWrite(10,HIGH);
  
}

void led_callback( const std_msgs::Float64& led){
  
  
  int led_yaniyorum = led.data;
  if (led_yaniyorum == 1){
    led_yak();
  }
}

ros::Subscriber<std_msgs::Float64> led_yakabilirmiyim("led_yakabilirmiyim", &led_callback );

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(10,OUTPUT);
  nh.initNode();
}

void loop() {
  // put your main code here, to run repeatedly:


  nh.subscribe(led_yakabilirmiyim);
  nh.spinOnce();
}

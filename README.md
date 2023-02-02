# Installing ros2-to-ros1-to-arduino-bridge 
* Tested on for Arduino Mega ros2-galactic and ros1-noetic 

Building Bridge
--------------
Installing Noetic
* First you have to download noetic from here: (http://wiki.ros.org/noetic/Installation/Ubuntu)
* "source /opt/ros/noetic/setup.bash" should not be included in bashrc
* You have to download galactic from here: (https://docs.ros.org/en/galactic/Installation/Ubuntu-Install-Debians.html)
```sh
sudo apt install ros-galactic-ros1-bridge
sudo apt install ros-galactic-performance-test-fixture
sudo apt install ros-galactic-test-interface-files

mkdir -p ~/ros2to1_bridge/src
cd ros2to1_bridge/src/

git clone https://github.com/mertbacaksiz/ros2-to-ros1-to-arduino-bridge.git
cd ..
colcon build


sudo apt-get install ros-noetic-rosserial-arduino
sudo apt-get install ros-noetic-rosserial
```
Adding required components on .bashrc
--------------
```sh
gedit ~/.bashrc 
export ROS_MASTER_URI=http://localhost:11311
source ~/ros2to1_bridge/install/setup.bash
source /opt/ros/galactic/setup.bash
```
Run
--------------
* Firs Terminal
```sh
source /opt/ros/noetic/setup.bash
roscore
```
* Second Terminal
```sh
ros2 run ros1_bridge dynamic_bridge --bridge-all-2to1-topics
```
* Third Terminal
```sh
sudo chmod 777 /dev/ttyACM0
* #The following code is uploaded to the Arduino: led_yakabilirmiyim.ino
rosrun rosserial_python serial_node.py /dev/ttyACM0  # example: ttyACM1, ttyACM0
```
* Fourth Terminal
```sh
python3 led_publisher.py   # file is in scripts
```

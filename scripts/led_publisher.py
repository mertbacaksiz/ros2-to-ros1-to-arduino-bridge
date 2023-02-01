#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class RobotNewsStationNode(Node):
    def __init__(self):
        super().__init__("ampul")
         
        self.robot_name_ = "Ecotron4"
        self.publisher_ = self.create_publisher(Float64,"led_yakabilirmiyim",10)
        self.timer_ = self.create_timer(0.1, self.publish_news)  
        self.get_logger().info("Robot News Station has been started")

    def publish_news(self):
        msg = Float64()
        msg.data = 1.0
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

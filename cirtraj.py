import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys

class Rotating_node(Node):
    def __init__(self):
        super().__init__('rotating_node')
        self.publisher=self.create_publisher(Twist,'/turtle1/cmd_vel', 10)
        self.timer=self.create_timer(1,self.timer_callback)
   
    def timer_callback(self):
        msg = Twist()
        linear_velo=float(sys.argv[1])
        radius=float(sys.argv[2])
        msg.linear.x=linear_velo
        msg.linear.y=0.0
        msg.angular.z=linear_velo/radius
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    mini_publisher = Rotating_node()
    rclpy.spin(mini_publisher)
    mini_publisher.destroy_node()
    rclpy.shutdown()

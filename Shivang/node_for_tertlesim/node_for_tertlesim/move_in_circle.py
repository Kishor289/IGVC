import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute
from geometry_msgs.msg import Twist
import time
import math

class RotateTurtleNode(Node):
    def __init__(self,x,y,z,a):
        super().__init__('teleport_turtle_node')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.x=x
        self.y=y
        self.z=z
        self.a=a
        self.timer=self.create_timer(1,self.move_in_circle)  #for maintaining continuous movement

    def move_in_circle(self):
        message=Twist()
        message.linear.x=self.x
        message.linear.y=self.y
        message.linear.z=self.z
        message.angular.z=self.a 
        self.publisher.publish(message)
 

def main(args=None):
    speed_x = float(input("Enter speed in x: "))
    speed_z = float(input("Enter speed in z: "))
    speed_y = float(input("Enter speed in y: "))
    radius = float(input("Enter radius: "))
    rclpy.init(args=args)
    rotate_turtle_node = RotateTurtleNode(speed_x,speed_y,speed_z,(speed_x**2+speed_y**2+speed_z**2)**(1/2)/radius)

    
    rclpy.spin(rotate_turtle_node)
    
    rotate_turtle_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
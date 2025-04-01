import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class CircularTrajectory(Node):

    def __init__(self):
        super().__init__('CircularTrajectory')
        # topic name as per created turtlesim in launch file
        self.publisher_ = self.create_publisher(Twist, '/turtlesim1/turtle1/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.declare_parameter('r,s', "1,1") #radius,speed

    def timer_callback(self):
        self.r, self.s = map(float,self.get_parameter('r,s').get_parameter_value().string_value.split(','))
        msg = Twist()
        msg.linear.x = self.s # linear speed
        msg.angular.z = self.s/self.r # angular velocity
        self.publisher_.publish(msg) # publishing msg
        self.get_logger().info(f'Radius : {self.r}, Speed : {self.s}') # printing current radius and speed

def main(args=None):
    rclpy.init(args=args)
    circle = CircularTrajectory()
    rclpy.spin(circle)
    circle.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
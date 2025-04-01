import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class CircularTrajectory(Node):

    def __init__(self):
        super().__init__('CircularTrajectory')
        self.publisher_ = self.create_publisher(Twist, '/turtlesim1/turtle1/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.declare_parameter('r,s', "1,1") #r s

    def timer_callback(self):
        self.r, self.s = map(float,self.get_parameter('r,s').get_parameter_value().string_value.split(','))
        msg = Twist()
        msg.linear.x = self.s
        msg.angular.z = self.s/self.r
        self.publisher_.publish(msg)
        self.get_logger().info(f'Radius : {self.r}, Speed : {self.s}')

def main(args=None):
    rclpy.init(args=args)
    circle = CircularTrajectory()
    rclpy.spin(circle)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    circle.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
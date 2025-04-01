import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class CircleMotion(Node):
    def __init__(self):
        super().__init__('circle_motion')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        
        # Default values
        self.radius = 2.0  # meters
        self.speed = 1.0   # meters/second
        
        # Get user input
        self.get_parameters()
        
        # Calculate angular velocity based on v = r * ω
        self.angular_velocity = self.speed / self.radius
        
        self.get_logger().info(f'Starting circular motion with radius: {self.radius}m, speed: {self.speed}m/s')
        self.get_logger().info(f'Angular velocity: {self.angular_velocity} rad/s')
        
    def get_parameters(self):
        try:
            self.radius = float(input("Enter radius of the circle (meters): "))
            self.speed = float(input("Enter speed of the turtle (meters/second): "))
            
            # Validate inputs
            if self.radius <= 0 or self.speed <= 0:
                self.get_logger().error('Radius and speed must be positive values')
                self.radius = 2.0
                self.speed = 1.0
                self.get_logger().info(f'Using default values: radius={self.radius}, speed={self.speed}')
        except ValueError:
            self.get_logger().error('Invalid input. Using default values')
    
    def timer_callback(self):
        msg = Twist()
        msg.linear.x = self.speed
        msg.angular.z = self.angular_velocity
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    circle_motion = CircleMotion()
    
    try:
        rclpy.spin(circle_motion)
    except KeyboardInterrupt:
        circle_motion.get_logger().info('Stopping the turtle')
    finally:
        # Cleanup
        circle_motion.destroy_node()

if __name__ == '__main__':
    main()


import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CirclePublisher(Node):
    def __init__(self, velocity, radius, node_name, *, context = None, cli_args = None, namespace = None, use_global_arguments = True, enable_rosout = True, start_parameter_services = True, parameter_overrides = None, allow_undeclared_parameters = False, automatically_declare_parameters_from_overrides = False):
        super().__init__(node_name, context=context, cli_args=cli_args, namespace=namespace, use_global_arguments=use_global_arguments, enable_rosout=enable_rosout, start_parameter_services=start_parameter_services, parameter_overrides=parameter_overrides, allow_undeclared_parameters=allow_undeclared_parameters, automatically_declare_parameters_from_overrides=automatically_declare_parameters_from_overrides)
        
        self.velocity = velocity
        self.angular_velocity = velocity/radius

        self.publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.timer = self.create_timer(0.01/self.angular_velocity, self.publish_callback)
    
    def publish_callback(self):
        msg = Twist()
        msg.linear.x = self.velocity
        msg.angular.z = self.angular_velocity
        self.publisher.publish(msg)
        self.get_logger().info(f'Sent {msg}')

def main(args = None):
    rclpy.init()
    velocity = float(input("Enter velocity: "))
    radius = float(input("Enter radius: "))
    publisher = CirclePublisher(velocity, radius, "circle_publisher")
    rclpy.spin(publisher)
    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
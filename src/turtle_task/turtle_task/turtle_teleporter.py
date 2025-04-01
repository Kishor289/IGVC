import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute

class TeleportingClientNode(Node):
    def __init__(self, node_name, *, context = None, cli_args = None, namespace = None, use_global_arguments = True, enable_rosout = True, start_parameter_services = True, parameter_overrides = None, allow_undeclared_parameters = False, automatically_declare_parameters_from_overrides = False):
        super().__init__(node_name, context=context, cli_args=cli_args, namespace=namespace, use_global_arguments=use_global_arguments, enable_rosout=enable_rosout, start_parameter_services=start_parameter_services, parameter_overrides=parameter_overrides, allow_undeclared_parameters=allow_undeclared_parameters, automatically_declare_parameters_from_overrides=automatically_declare_parameters_from_overrides)
        self.client = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for service to become available")
        self.request = TeleportAbsolute.Request()

    def send_request(self, x, y, theta):
        self.request.x = x
        self.request.y = y
        self.request.theta = theta
        self.client.call_async(self.request).add_done_callback(self.callback)

    def callback(self, future):
        try:
            if(future.done()):
                self.get_logger().info("Teleportation succeeded")
            else:
                self.get_logger().info("Teleportation failed")
        except Exception as e:
            self.get_logger().error(f'Service call field: {e}')

def main():
    rclpy.init()
    node = TeleportingClientNode('teleporter_node')
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    theta = float(input("Enter theta: "))
    node.send_request(x, y, theta)
    rclpy.spin(node)
    rclpy.shutdown()


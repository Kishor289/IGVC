import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute

class TeleportNode(Node):
    def __init__(self):
        super().__init__('teleport_node')
        # Create a client for the teleport service
        self.cli = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')
        # Wait until the service is available
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')
        self.request = TeleportAbsolute.Request()
    
    def send_request(self, x, y, theta=0.0):
        # Set the request parameters
        self.request.x = float(x)
        self.request.y = float(y)
        self.request.theta = float(theta)  # theta is in radians
        # Send the request asynchronously
        future = self.cli.call_async(self.request)
        future.add_done_callback(self.callback)
        return future
    
    def callback(self, future):
        # Handle the response
        try:
            response = future.result()
            self.get_logger().info(f'Teleportation successful!')
        except Exception as e:
            self.get_logger().error(f'Service call failed: {e}')

def main():
    # Initialize ROS
    rclpy.init()
    
    # Get user input for position and orientation
    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))
    theta = float(input("Enter orientation (theta) in radians: "))
    
    # Create and use the client node
    node = TeleportNode()
    future = node.send_request(x, y, theta)
    
    # Wait for the response
    rclpy.spin_until_future_complete(node, future)
    
    # Clean up before exiting
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

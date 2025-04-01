import rclpy  # Import ROS 2 client library
from rclpy.node import Node  # Import Node class for creating a ROS 2 node
from turtlesim.srv import TeleportAbsolute  # Import the service definition for teleporting the turtle


class TeleportClient(Node):  # Define a class that inherits from Node
    def __init__(self):
        super().__init__('teleport_client')  # Initialize the node with a name
        # Create a service client for the TeleportAbsolute service
        self.cli = self.create_client(
            TeleportAbsolute, '/turtle1/teleport_absolute')

    def send_request(self, x, y, theta):
        # Create a request object for the TeleportAbsolute service
        request = TeleportAbsolute.Request()
        request.x = float(x)  # Set x-coordinate
        request.y = float(y)  # Set y-coordinate
        request.theta = float(theta)  # Set orientation (theta)

        # Send an asynchronous service request
        future = self.cli.call_async(request)
        rclpy.spin_until_future_complete(self, future)  # Wait for the response

        # Check if the service call was successful
        if future.result() is not None:
            self.get_logger().info("Turtle Teleported successfully")  # Log success message


def main():  # Define the main function
    rclpy.init()  # Initialize the ROS 2 communication

    teleport_client = TeleportClient()  # Create an instance of the client node

    # Take user input for teleportation coordinates and orientation
    x = input("Enter x : ")
    y = input("Enter y : ")
    theta = input("Enter theta : ")

    # Send request with the user-provided values
    teleport_client.send_request(x, y, theta)

    teleport_client.destroy_node()  # Destroy the node after execution
    rclpy.shutdown()  # Shut down ROS 2 properly


if __name__ == '__main__':  # Entry point of the script
    main()

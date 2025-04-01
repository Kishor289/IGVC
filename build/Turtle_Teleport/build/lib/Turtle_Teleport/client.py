import rclpy  
from rclpy.node import Node 
from turtlesim.srv import TeleportAbsolute # as given in Task , imported turtlesim services


class TeleportClient(Node):
    def __init__(self):
        super().__init__('teleport_client')
        self.cli = self.create_client(
            TeleportAbsolute, '/turtle1/teleport_absolute')

    def send_request(self, x, y, theta):
        request = TeleportAbsolute.Request()
        request.x = float(x)  # Set x-coordinate
        request.y = float(y)  # Set y-coordinate
        request.theta = float(theta)  # Set orientation (theta)

        # Send an asynchronous service request
        future = self.cli.call_async(request)
        rclpy.spin_until_future_complete(self, future)  # Wait for the response

        # Checking if the service call was successful
        if future.result() is not None:
            self.get_logger().info("Turtle Teleported successfully")  # Log success message


def main():
    rclpy.init()
    teleport_client = TeleportClient()  # Creating an instance

    # Take user input
    x = input("Enter x : ")
    y = input("Enter y : ")
    theta = input("Enter theta : ")

    teleport_client.send_request(x, y, theta)  # calling send_request

    teleport_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

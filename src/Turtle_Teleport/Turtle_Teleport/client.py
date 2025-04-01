import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute


class TeleportClient(Node):
    def __init__(self):
        super().__init__('teleport_client')
        self.cli = self.create_client(
            TeleportAbsolute, '/turtle1/teleport_absolute')

    def send_request(self, x, y, theta):
        request = TeleportAbsolute.Request()
        request.x = float(x)
        request.y = float(y)
        request.theta = float(theta)

        future = self.cli.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None:
            self.get_logger().info("Turtle Teleported successfully")


def main():
    rclpy.init()

    teleport_client = TeleportClient()

    x = input("Enter x : ")
    y = input("Enter y : ")
    theta = input("Enter theta : ")

    teleport_client.send_request(x, y, theta)

    teleport_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

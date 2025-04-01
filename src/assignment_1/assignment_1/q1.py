import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute


class TeleportClient(Node):
    def __init__(self):
        super().__init__('teleport_client')
        self.client = self.create_client(TeleportAbsolute, '/turtlesim2/turtle1/teleport_absolute')
        self.request = TeleportAbsolute.Request()
        self.declare_parameter('x,y,theta', '5.544445,5.544445,0')

    def teleport_turtle(self):
        x,y,theta = map(float,self.get_parameter('x,y,theta').get_parameter_value().string_value.split(','))
        self.request.x = x
        self.request.y = y
        self.request.theta = theta
        future = self.client.call_async(self.request)
        rclpy.spin_until_future_complete(self, future)
        return future.result()


def main():
    rclpy.init()
    client = TeleportClient()
    client.teleport_turtle()
    client.get_logger().info('Turtle teleported successfully')
    client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
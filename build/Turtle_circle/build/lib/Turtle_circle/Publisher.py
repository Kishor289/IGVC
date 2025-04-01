import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class CircularMotion(Node):
    def __init__(self):
        super().__init__('circular_motion')
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def move(self, r, v):
        msg = Twist()
        msg.linear.x = float(v)
        msg.angular.z = float(v) / float(r)

        while 1:
            self.pub.publish(msg)
            self.get_logger().info(
                f'Moving in circle: radius={r}, velocity={v}, angular={msg.angular.z}')


def main(args=None):
    rclpy.init(args=args)
    node = CircularMotion()

    r = float(input("Enter radius: "))
    v = float(input("Enter velocity: "))

    node.move(r, v)

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

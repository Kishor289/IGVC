# import rclpy
# from rclpy.node import Node
# from turtlesim.srv import TeleportAbsolute
# from turtlesim.msg import Pose
# import math

# class TeleportTurtleNode(Node):
#     def __init__(self):
#         super().__init__('teleport_turtle_node')
#         self.teleport_client = self.create_client(TeleportAbsolute, 'turtle1/teleport_absolute')
#         self.pose_subscription = self.create_subscription(Pose, 'turtle1/pose', self.pose_callback, 10)
#         self.teleported_pose = None

#     def teleport_turtle(self, x, y, theta):
#         """Teleports the turtle to the given position and orientation."""
#         while not self.teleport_client.wait_for_service(timeout_sec=1.0):
#             self.get_logger().info('service not available, waiting again...')
        
#         request = TeleportAbsolute.Request()
#         request.x = float(x)
#         request.y = float(y)
#         request.theta = float(theta)
        
#         future = self.teleport_client.call_async(request)
#         rclpy.spin_until_future_complete(self, future)
        
#         if future.result() is not None:
#             self.get_logger().info('Turtle teleported successfully!')
#             self.teleported_pose = Pose()
#             self.teleported_pose.x = float(x)
#             self.teleported_pose.y = float(y)
#             self.teleported_pose.theta = float(theta)
#             return True
#         else:
#             self.get_logger().error('Failed to call service teleport_absolute: %r' % future.exception())
#             return False

#     def pose_callback(self, pose_msg):
#         """Callback function to verify the turtle's pose."""
#         if self.teleported_pose is not None:
#             if (abs(pose_msg.x - self.teleported_pose.x) < 0.01 and 
#                abs(pose_msg.y - self.teleported_pose.y) < 0.01 and 
#                abs(pose_msg.theta - self.teleported_pose.theta) < 0.01):
#                 self.get_logger().info('Turtle pose verified!')
#                 rclpy.shutdown()  # Stop the node
#             else:

#                 self.get_logger().warn(f'Turtle pose does not match teleported pose.\ndelta_x={pose_msg.x - self.teleported_pose.x}\ndelta_y={pose_msg.y - self.teleported_pose.y}\ndelta_theta={pose_msg.theta - self.teleported_pose.theta}\n{pose_msg.theta}')

# def main(args=None):
#     rclpy.init(args=args)
#     teleport_turtle_node = TeleportTurtleNode()

#     x = float(input("Enter x coordinate: "))
#     y = float(input("Enter y coordinate: "))
#     theta = float(input("Enter theta (orientation): "))

#     if teleport_turtle_node.teleport_turtle(x, y, theta):
#         # rclpy.spin(teleport_turtle_node)
#         teleport_turtle_node.get_logger().info("Taken the node")

#     teleport_turtle_node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()









import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute
from turtlesim.msg import Pose
import math

class TeleportTurtleNode(Node):
    def __init__(self):
        super().__init__('teleport_turtle_node')
        self.teleport_client = self.create_client(TeleportAbsolute, 'turtle1/teleport_absolute')
        # self.pose_subscription = self.create_subscription(Pose, 'turtle1/pose', self.pose_callback, 10)
        self.teleported_pose = None

    def teleport_turtle(self, x, y, theta):
        """Teleports the turtle to the given position and orientation."""
        while not self.teleport_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        
        request = TeleportAbsolute.Request()
        request.x = float(x)
        request.y = float(y)
        request.theta = float(theta)
        
        future = self.teleport_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        
        if future.result() is not None:
            self.get_logger().info('Turtle teleported successfully!')
            self.teleported_pose = Pose()
            self.teleported_pose.x = float(x)
            self.teleported_pose.y = float(y)
            self.teleported_pose.theta = float(theta)
            return True
        else:
            self.get_logger().error('Failed to call service teleport_absolute: %r' % future.exception())
            return False

    

def main(args=None):
    rclpy.init(args=args)
    teleport_turtle_node = TeleportTurtleNode()

    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))
    theta = float(input("Enter theta (orientation): "))

    is_moved_succesfully=teleport_turtle_node.teleport_turtle(x, y, theta)
    
    while is_moved_succesfully:
        # rclpy.spin(teleport_turtle_node)
        x = float(input("Enter x coordinate: "))
        y = float(input("Enter y coordinate: "))
        theta = float(input("Enter theta (orientation): "))

        is_moved_succesfully=teleport_turtle_node.teleport_turtle(x, y, theta)


    teleport_turtle_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
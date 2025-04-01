import rclpy  
from rclpy.node import Node  
from geometry_msgs.msg import Twist  # as given in Task, imported Twist message for velocity control


class CircularMotion(Node):  # Define a class that inherits from Node
    def __init__(self):
        super().__init__('circular_motion')  
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10) # Create a publisher for the /turtle1/cmd_vel topic

    def move(self, r, v):
        
        a = Twist()
        a.linear.x = float(v)  # Set linear velocity
        a.angular.z = float(v) / float(r)  # Compute angular velocity

        while True:  # Infinite loop to keep the turtle moving
            self.pub.publish(a)  # Publish the velocity command
            self.get_logger().info(f'Moving in circle: radius={r}, velocity={v}, angular={a.angular.z}') # This output a message that showes the values that user has feed 


def main(args=None):  
    rclpy.init(args=args) 
    node = CircularMotion()  # Create an instance of the CircularMotion node

    # Take user input for radius and velocity
    r = float(input("Enter radius: "))
    v = float(input("Enter velocity: "))

    node.move(r, v)  # Call the move function with user-provided values

    rclpy.spin(node) 
    node.destroy_node()  
    rclpy.shutdown() 


if __name__ == '__main__':  # Entry point of the script
    main()

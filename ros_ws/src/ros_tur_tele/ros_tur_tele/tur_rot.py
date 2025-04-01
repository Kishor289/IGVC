import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleCircle(Node):
	def __init__(self,speed,radius):
		super().__init__('tur_rot')
		self.publisher=self.create_publisher(Twist,'/turtle1/cmd_vel',10)
		
		self.twist = Twist()
		self.twist.linear.x=speed
		self.twist.angular.z=speed/radius
		
		self.timer = self.create_timer(0.01,self.publish_velocity)
		
	def publish_velocity(self):
		self.publisher.publish(self.twist)
		self.get_logger().info("Moving")
		
def main():
	rclpy.init()
	radius=float(input("Enter the value of radius : "))
	speed=float(input("Enter the value of speed : "))
	#timer=float(input("Enter the value of timer : "))
	
	tur_cir=TurtleCircle(radius,speed)
	rclpy.spin(tur_cir)
	
	tur_cir.destroy_node
	rclpy.shutdown()
	
if __name__=='__main__':
	main()

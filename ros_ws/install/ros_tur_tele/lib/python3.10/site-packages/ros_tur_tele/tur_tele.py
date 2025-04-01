import rclpy
import sys
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute

class TurtleTeleport(Node):
	def __init__(self):
		super().__init__('turtle_teleport')
		self.client=self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')
		while not self.client.wait_for_service(timeout_sec=1.0):
			self.get_logger().info('Waiting for service /turtle1/teleport_absolute...')
			
		self.req=TeleportAbsolute.Request()
		
		
	def send_request(self ,x,y,theta):
		self.req.x=x
		self.req.y=y
		self.req.theta=theta
		return self.client.call_async(self.req)
		
def main():
	rclpy.init()
	
	x=float(input('Enter the value for x: '))
	y=float(input('Enter the value for y: '))
	theta=float(input('Enter the value for theta: '))
	
	tur_tele=TurtleTeleport()
	future=tur_tele.send_request(x,y,theta)
	#future=tur_tele.send_request(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
	rclpy.spin_until_future_complete(tur_tele,future)
	
	if future.result():
	        print("Teleported Successfully")
	else:
	        print("Failed to teleport turtle")
	
	
	tur_tele.destroy_node()
	rclpy.shutdown()
	
if __name__=='__main__':
	main()
	

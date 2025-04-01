The workspace contains two scripts corresponding to the given two tasks.

The Hierarchy is of the following type -

ros_ws >
	build
	install
	log
	src >
		ros_tur_tele >
			resource
			ros_tur_tele >
				__init__.py
				tur_rot.py
				tur_tele.py
			test
			package.xml
			setup.cfg
			setup.py
			
The package name is ros_tur_tele.

The corresponding two nodes (scripts) are - 

1)tur_rot.py -

	What does it do? - makes the turtle move in a user defined speed and radius.

	Dependencies - a)rclpy
		       b)turtlesim
		       c)geometry_msgs
	
	Use ? - Upon running the script , The user will have to enter two parameters - 
	
			a)speed - linear speed of turtle(float)
			b)radius - radius of the circle(float)
			
		The script will then compute the required angular velocity (w) given as -
		
			w = speed/radius
			
2)tur_tele.py -
	
	What does it do? - Teleports turtle instantly to the given coordinates (x,y) and rotates it 		 about its own axis with an angle (theta).   
	
	Dependencies - a)rclpy
		       b)turtlesim
	
	Use ? - Upon running the script , The user will have to enter three parameters -
	
		a)x - the x coordinate for teleportation (float)
		a)y - the y coordinate for teleportation (float)
		a)theta - the angle (in radians) to rotate the turtle about its own axis (float)
		
		Upon successful teleportation , A message "Teleported Successfully" will get printed.
	
--------------------------------------------------------------------------------------------------------	
		
Running the scripts -

1) Open a terminal and launch the turtlesim in that using the command -

ros2 run turtlesim turtlesim_node

2) Open another terminal and go into the workspace directory , ros_ws -

cd ros_ws

3) Source your files - 

source install/setup.bash

4)Now run the nodes using the corresponding syntax -

ros2 run <package_name> <executable_name>

5) Package name - ros_tur_tele

6) Executables - 1)tur_tele
		 2)tur_rot
		 
7)Input the parameters and you are all set !



1)

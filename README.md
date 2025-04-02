# IGVC ROS Package Submission

Since the ROS package is uploaded as a `.zip` file, follow these steps to extract and set it up:

```bash
cd ~/ws_turtle/src                             # Navigate to your ROS workspace
unzip turtle_controller.zip                       # Extract the package
mv turtle_controller ~/ws_turtle/src/            # Move it to the workspace
cd ~/ws_turtle
colcon build --packages-select turtle_controller
source install/setup.bash
ros2 run turtle_controller teleport_turtle
ros2 run turtle_controller circular_motion

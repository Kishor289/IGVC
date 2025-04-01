# Prerequisites

Before using this project, ensure you have the following installed on your system:

1. **ROS 2 Humble Hawksbill**
    - Follow the official instructions to install the ROS 2 Humble desktop version on your system.
    - For Ubuntu Jammy (22.04 LTS), you can install it using the following commands:

```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository universe
sudo apt update &amp;&amp; sudo apt install curl gnupg lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release &amp;&amp; echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list &gt; /dev/null
sudo apt update
sudo apt install ros-humble-desktop
```

After installation, source the ROS 2 setup file:

```bash
source /opt/ros/humble/setup.bash
```

To make this step automatic, add the sourcing command to your shell configuration file:

```bash
echo "source /opt/ros/humble/setup.bash" &gt;&gt; ~/.bashrc
source ~/.bashrc
```

2. **Turtlesim Package**
    - Install the Turtlesim package for ROS 2 Humble:

```bash
sudo apt update
sudo apt install ros-humble-turtlesim
```

Verify that the package is installed by listing its executables:

```bash
ros2 pkg executables turtlesim
```

You should see a list of executables like `turtlesim_node`, `turtle_teleop_key`, etc.

# Usage

Build the project with colcon outside the src directory
```bash
colcon build
```
You should see new build and install directories parallel to src

Open a turtlesim window in a terminal
```bash
ros2 run turtlesim turtlesim_node
```

In a new terminal, source the setup files as follows
```bash
source install/setup.bash
```

To run the teleporter, use
```bash
ros2 run turtle_task turtle_teleporter
```

To run the circle node, use
```bash
ros2 run turtle_task turtle_circle
```


from launch import LaunchDescription
from launch_ros.actions import Node
import launch

def generate_launch_description():
    return LaunchDescription([
        # declaring parameters to take input while running launch file.
        launch.actions.DeclareLaunchArgument(
            'r,s',
            default_value='1,1',
            description='User-provided input for the node'
        ),
        # turtlesim node
        Node(
            package='turtlesim',
            namespace='turtlesim1',
            executable='turtlesim_node',
            name='sim'
        ),
        # circular trajectory node
        Node(
            package='assignment_1',
            namespace='assignment_1',
            executable='q2',
            name='q2',
            parameters=[{'r,s': launch.substitutions.LaunchConfiguration('r,s')}]
        )
    ])
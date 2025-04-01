import launch
import launch.actions
import launch.substitutions
from launch_ros.actions import Node

def generate_launch_description():
    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            'x,y,theta',
            default_value='5.544445,5.544445,0',
            description='User-provided input for the node'
        ),
        Node(
            package='turtlesim',
            namespace='turtlesim2',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='assignment_1',
            namespace='assignment_1',
            executable='q1',
            name='q1',
            parameters=[{'x,y,theta': launch.substitutions.LaunchConfiguration('x,y,theta')}]
        )
    ])
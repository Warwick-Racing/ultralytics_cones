from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.substitutions.path_join_substitution import PathJoinSubstitution
import launch

def generate_launch_description():
    ultralytics_dir =  get_package_share_directory('ultralytics_cones')

    mp4_node = Node(
            package='mp42ros',
            executable='runner',
            name='runner_node',
            output='screen',
            parameters=[{'mp4_file_path': PathJoinSubstitution([ultralytics_dir, 'media', 'demo.mp4']),
                         'loop': True,
                         'send_topic_name': '/image_node/input'}]
        )

    image_node = Node(
            package='ultralytics_cones',
            executable='image_node',
            name='image_node',
            output='screen',
            parameters=[{'model_path': PathJoinSubstitution([ultralytics_dir, 'models', 'cones_yolo11n_epochs10.pt'])}]
        )

    debug_viz = Node(
            package='rqt_image_view',
            executable='rqt_image_view',
            name='rqt_image_view',
            output='screen',
            arguments=['/image_node/debug'],
            on_exit=launch.actions.Shutdown()
        )

    return LaunchDescription([
        mp4_node,
        image_node,
        debug_viz
    ])

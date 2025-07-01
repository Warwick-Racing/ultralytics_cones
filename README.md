# ultralytics_cones

This package, `ultralytics_cones`, is designed to provide a ROS2 node that outputs messages of type `std_msgs` at a specified interval. 

## Package Structure

- `ultralytics_cones/`: The main package directory containing the Python code.
  - `__init__.py`: Marks the directory as a Python package.
  - `image_node.py`: Contains the implementation of the ROS2 node that publishes messages.
  
- `launch/`: Directory for launch files.
  - `demo.py`: A placeholder for a launch file that will be implemented in the future.

- `resource/`: Directory intended for resources related to the package.
  - `ultralytics_cones/`: This folder will eventually contain files such as `demo.mp4`.

- `package.xml`: Defines the package metadata, including dependencies and version information.

- `setup.py`: Used for packaging the Python project, specifying the package name, version, and entry points.

- `setup.cfg`: Contains configuration settings for the package, including metadata and options for packaging.

## Usage

To run the `image_node`, ensure that you have ROS2 installed and properly set up. You can then build the package and run the node using the appropriate ROS2 commands.

## Future Work

- Implement the functionality in `launch/demo.py`.
- Add resources such as `demo.mp4` in the `resource/ultralytics_cones` directory.
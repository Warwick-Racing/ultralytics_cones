# ultralytics_cones

## Overview
The `ultralytics_cones` package is a ROS (Robot Operating System) package designed to process images from a camera sensor. It subscribes to a `sensor_msgs::msg::Image` topic, processes the image data, and publishes the modified image to another `sensor_msgs::msg::Image` topic.

## Installation
To install the `ultralytics_cones` package, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the package directory:
   ```
   cd ultralytics_cones
   ```
3. Install the package using `rosdep`:
   ```
   rosdep install --from-paths src --ignore-src -r -y
   ```
4. Build the package:
   ```
   colcon build
   ```

## Usage
To run the image processing node, use the following command:
```
ros2 run ultralytics_cones image_node
```

## Dependencies
This package requires the following ROS 2 packages:
- `sensor_msgs`
- Any other dependencies specified in `package.xml`.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
# ultralytics_cones

This package provides a ROS2 node for processing images using the Ultralytics YOLO detection model. 
Published an output image with colored in bounding boxes.
Our usage is as a pre-processing step for a Reinforcement learning model.


## Usage

To run the `image_node`, ensure that you have ROS2 installed and properly set up. You can then build the package and run the node using the appropriate ROS2 commands.

### Node

```bash
ros2 run ultralytics_cones image_node
```


### Topics

Output topics are only published if subscribed to.

- /image_node/input: Input image topic (e.g., from a camera or video source).
- /image_node/output: Output image after processing.
- /image_node/output/grey: Output image as grayscale.
- /image_node/debug: Input image showing label and bounding box annotations.

*Only available if output_res parameter set*

- /image_node/output/resized: Output image resized to the specified dimensions.
- /image_node/output/resized/gray: Output image resized and converted to grayscale.

### Parameters

- model_path: Path to model file.
  - Local file, e.g. "models/cones_yolo11n_epochs10.pt"
  - If local file is not found will attempt to download the model from the Ultralytics repository.
  - Default: yolov8n.pt
- output_res: Output image resolution.
  - Expected format is "WIDTHxHEIGHT".
  - Default: "" (no resizing)
  
*TODO - parameter for setting colors of bounding boxes.*


## Demos

Demos depends on the mp42rosimg package to publish mp4 video to ROS2 image topic.

https://github.com/PINTO0309/mp42rosimg


```bash
ros2 launch ultralytics_cones demo.py
```

```bash
ros2 launch ultralytics_cones demo_resize.py
```

![](media/demo_debug.gif)

*/image_node/output/debug*
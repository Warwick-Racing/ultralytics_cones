from rclpy.node import Node
from sensor_msgs.msg import Image
import rclpy

import ultralytics

import cv2
from cv_bridge import CvBridge

class ImageNode(Node):
    def __init__(self):
        super().__init__('image_node')
        self.subscription = self.create_subscription(
            Image,
            'input_image_topic',
            self.listener_callback,
            10)
        self.publisher = self.create_publisher(Image, 'output_image_topic', 10)

        self._bridge = CvBridge()
        self._model = ultralytics.YOLO('yolov8n.pt')  # or your custom model

    def listener_callback(self, msg):
        # Process the incoming image message and publish it
        self.get_logger().info('Received an image message')

 

        cv_image = self._bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        results = self._model.predict(cv_image)

        # Here you can add image processing logic
        self.publisher.publish(msg)
        self.get_logger().info('Published an image message')

def main(args=None):
    rclpy.init(args=args)
    image_node = ImageNode()
    rclpy.spin(image_node)
    image_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
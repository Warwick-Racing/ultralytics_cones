from rclpy.node import Node
from sensor_msgs.msg import Image
import rclpy

import ultralytics
import numpy as np

import cv2
from cv_bridge import CvBridge

class ImageNode(Node):
    def __init__(self):
        super().__init__('image_node')
        self.subscription = self.create_subscription(
            Image,
            '~/input',
            self.listener_callback,
            10)
        
        self.publisher = self.create_publisher(Image, '~/output', 10)
        self.resized = self.create_publisher(Image, '~/output/resized', 10)
        self.gray = self.create_publisher(Image, '~/output/grey', 10)
        self.resizedgray = self.create_publisher(Image, '~/output/resized/gray', 10)
        self.debug = self.create_publisher(Image, '~/debug', 10)

        # ==== Parameters ===
        self.declare_parameter('model_path', 'yolov8n.pt')
        model_path = self.get_parameter('model_path').get_parameter_value().string_value

        self.declare_parameter('output_res', "")
        res = self.get_parameter('output_res').get_parameter_value().string_value
        try:
            width, height = map(int, res.lower().split('x'))
            self._output_size = (width, height)
        except Exception as e:
            if res != "":
                self.get_logger().warn(f"Invalid output_res format: '{res}'. Expected format 'WIDTHxHEIGHT'. Disabling resizing.")
            self._output_size = None

        self.declare_parameter('output_grey', False)
        self._output_grey = self.get_parameter('output_grey').get_parameter_value().bool_value
       
        self._colors = [(255, 0, 0), (0, 100, 255), (0, 255, 255)]

        self._bridge = CvBridge()
        self._model = ultralytics.YOLO(model_path)  # or your custom model
        self._outimg = None

    def listener_callback(self, msg):
        # Process the incoming image message and publish it
        self.get_logger().debug('Received an image message')

        cv_image = self._bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        result = self._model.predict(cv_image, save=False, verbose=False)[0]

        if self._outimg is None:
            self._outimg = np.zeros_like(cv_image)
        else:
            self._outimg.fill(0)
        
        boxes_sorted = sorted(result.boxes, key=lambda box: box.xywh[0][1])
        for box in boxes_sorted:
            # Get box coordinates (xyxy format)
            class_id = int(box.cls[0])
            if class_id >= len(self._colors): continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            # Draw rectangle on blank_img
            cv2.rectangle(self._outimg, (x1, y1), (x2, y2), self._colors[class_id], thickness=-1)

        # publish the full size, full color topic
        if self.publisher.get_subscription_count() > 0:
            out_msg = self._bridge.cv2_to_imgmsg(self._outimg, encoding='bgr8')
            self.publisher.publish(out_msg)
            self.get_logger().debug('Published an image message')

        # publish the full size grey topic
        if self.gray.get_subscription_count() > 0:
            gray_img = cv2.cvtColor(self._outimg, cv2.COLOR_BGR2GRAY)
            self.gray.publish(self._bridge.cv2_to_imgmsg(gray_img, encoding='mono8'))
            self.get_logger().debug('Published a grey image message')

        # if resize param has been set, resize and publish color and grey topics
        if self._output_size and (self.resized.get_subscription_count() > 0 or self.resizedgray.get_subscription_count() > 0):
            resized_img = cv2.resize(self._outimg, self._output_size, interpolation=cv2.INTER_LINEAR)

            if self.resized.get_subscription_count() > 0:
                self.resized.publish(self._bridge.cv2_to_imgmsg(resized_img, encoding='bgr8'))
                self.get_logger().debug('Published a resized image message')

            if self.resizedgray.get_subscription_count() > 0:
                resized_gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
                self.resizedgray.publish(self._bridge.cv2_to_imgmsg(resized_gray_img, encoding='mono8'))
                self.get_logger().debug('Published a resized grey image message')

        # publish the debug topic
        if self.debug.get_subscription_count() > 0:
            debug_img = result.plot()
            self.debug.publish(self._bridge.cv2_to_imgmsg(debug_img, encoding='bgr8'))


def main(args=None):
    rclpy.init(args=args)
    image_node = ImageNode()
    rclpy.spin(image_node)
    image_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
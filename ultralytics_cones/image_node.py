from rclpy.node import Node
from sensor_msgs.msg import Image
import rclpy
import ultralytics

class ImageNode(Node):
    def __init__(self):
        super().__init__('image_node')
        self.subscription = self.create_subscription(
            Image,
            'input_image_topic',
            self.listener_callback,
            10)
        self.publisher = self.create_publisher(Image, 'output_image_topic', 10)

    def listener_callback(self, msg):
        # Process the incoming image message and publish it
        self.get_logger().info('Received an image message')
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
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

class TestImageNode(Node):
    def __init__(self):
        super().__init__('test_image_node')
        self.subscriber = self.create_subscription(
            Image,
            'input_image_topic',
            self.listener_callback,
            10
        )
        self.publisher = self.create_publisher(Image, 'output_image_topic', 10)

    def listener_callback(self, msg):
        self.get_logger().info('Received an image!')
        # Here you would process the image and publish the result
        self.publisher.publish(msg)  # For now, just echoing the received image

def main(args=None):
    rclpy.init(args=args)
    node = TestImageNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()